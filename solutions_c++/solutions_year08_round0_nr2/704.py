// Trains.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <set>
#include <memory>
#include <utility>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

struct time
{
	size_t hour;
	size_t minute;

	time() :
		hour(-1),
		minute(-1)
	{
	}

	time(size_t h, size_t m) :
		hour(h),
		minute(m)
	{
	}
};

typedef std::pair<time, time> Duration;

typedef std::multiset<Duration> TimeTable;

bool operator<(const time& lhs, const time& rhs)
{
	if (lhs.hour < rhs.hour)
		return true;

	if (lhs.hour > rhs.hour)
		return false;

	return lhs.minute < rhs.minute;
}

typedef std::pair<size_t, size_t> TrainsAB;
typedef std::multiset<time> FreeTimes;

TrainsAB GetNeedTrainsCount(TimeTable& a, TimeTable& b)
{
	TrainsAB result(std::make_pair(0, 0));

	FreeTimes existingA;
	FreeTimes existingB;

	while (!a.empty() || !b.empty())
	{
		Duration curA;
		if (!a.empty())
			curA = *a.begin();

		Duration curB;
		if (!b.empty())
			curB = *b.begin();

		if (curA < curB)
		{
			a.erase(a.begin());

			if (existingA.empty())
				++result.first;
			else if (*existingA.begin() < curA.first || existingA.begin()->hour == curA.first.hour && existingA.begin()->minute == curA.first.minute)
				existingA.erase(existingA.begin());
			else
				++result.first;

			existingB.insert(curA.second);
		}
		else
		{
			b.erase(b.begin());

			if (existingB.empty())
				++result.second;
			else if (*existingB.begin() < curB.first || existingB.begin()->hour == curB.first.hour && existingB.begin()->minute == curB.first.minute)
				existingB.erase(existingB.begin());
			else
				++result.second;

			existingA.insert(curB.second);
		}
	}

	return result;
}

size_t tosize_t(const std::string& str)
{
	std::stringstream strm(str);
	size_t result = 0;
	strm >> result;

	return result;
}

time fromstring(const std::string& str)
{
	size_t pos = str.find(':');
	std::string hs = str.substr(0, pos);
	std::string ms = str.substr(pos + 1);

	return time(tosize_t(hs), tosize_t(ms));
}

int _tmain(int argc, _TCHAR* argv[])
{
//	TimeTable a;
//
//	{
///*09:00 09:01
//12:00 12:02*/
//		a.insert(std::make_pair(time(9, 0), time(9, 3)));
//		a.insert(std::make_pair(time(12, 0), time(12, 4)));
//
//		//////////////////////////////////////////////////////////////////
//		/*a.insert(std::make_pair(time(9, 0), time(12, 5)));
//		a.insert(std::make_pair(time(10, 0), time(13, 5)));
//		a.insert(std::make_pair(time(11, 0), time(12, 35)));*/
//
//		/*09:00 12:00
//		10:00 13:00
//		11:00 12:30*/		
//	}
//
//	TimeTable b;
//	{
//		/*b.insert(std::make_pair(time(12, 2), time(15, 5)));
//		b.insert(std::make_pair(time(9, 0), time(10, 35)));*/
//		/*
//		12:02 15:00
//09:00 10:30
//
//		*/
//	}

	std::ifstream file("B-large.in");
	//std::ifstream file("B-small-attempt1.in");	
	std::ofstream result("result.txt");

	std::string str;
	std::getline(file, str);

	size_t countTests = tosize_t(str);

	for (size_t i = 1; i <= countTests; ++i)
	{
		std::getline(file, str);
		size_t t = tosize_t(str);

		std::getline(file, str);
		size_t pos = str.find(' ');
		size_t countA = tosize_t(str.substr(0, pos));
		size_t countB = tosize_t(str.substr(pos + 1));

		TimeTable a;
		for (size_t j = 0; j < countA; ++j)
		{
			std::getline(file, str);
			size_t pos = str.find(' ');
			time t1 = fromstring(str.substr(0, pos));
			time t2 = fromstring(str.substr(pos + 1));			
			t2.minute += t;
			if (t2.minute >= 60)
			{
				++t2.hour;
				t2.minute -= 60;
			}

			a.insert(std::make_pair(t1, t2));
		}

		TimeTable b;
		for (size_t j = 0; j < countB; ++j)
		{
			std::getline(file, str);
			size_t pos = str.find(' ');
			time t1 = fromstring(str.substr(0, pos));
			time t2 = fromstring(str.substr(pos + 1));			
			t2.minute += t;
			if (t2.minute >= 60)
			{
				++t2.hour;
				t2.minute -= 60;
			}

			b.insert(std::make_pair(t1, t2));
		}

		TrainsAB data = GetNeedTrainsCount(a, b);
		//Case #1: 2 2

		std::cout << "Case #" << i <<": " << data.first << " " << data.second << std::endl;
		result << "Case #" << i <<": " << data.first << " " << data.second << std::endl;
	}

	


	return 0;
}

