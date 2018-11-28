// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <fstream>
#include <limits>
#include <stdexcept>

#include <math.h>
static const double pi = 3.1415926535;

using namespace std;

struct Time
{
	Time(const int& hour, const int& minute): _hour(hour), _minute(minute) {};
	Time(const Time& time): _hour(time._hour), _minute(time._minute) {};
	Time(istream& stream);

	int _hour;
	int _minute;

	bool operator<(const Time& time) const;
	bool operator==(const Time& time) const;
	const Time& operator+=(const Time& time);
};

Time::Time(istream& stream)
{
	(stream >> _hour).ignore() >> _minute;
};

bool Time::operator<(const Time& time) const
{
	return ((_hour < time._hour) || (_hour == time._hour) && (_minute < time._minute));
}

bool Time::operator==(const Time& time) const
{
	return ((_hour == time._hour) && (_minute == time._minute));
}

const Time& Time::operator+=(const Time& time)
{
	_minute += time._minute;
	while (_minute >= 60)
	{
		_hour += 1;
		_minute -= 60;
	}
	while (_hour >= 24)
	{
		_hour -= 24;
	}

	return *this;
}

enum Point
{
	A,
	B
};

enum EventType
{
	Start,
	Stop
};

struct Event
{
	Event(const Time& time, const Point& point, const EventType& eventType): _time(time), _point(point), _eventType(eventType) {};
	Event(const Event& evnt): _time(evnt._time), _point(evnt._point), _eventType(evnt._eventType) {};

	Time _time;
	Point _point;
	EventType _eventType;

	bool operator<(const Event& evnt) const;
};

bool Event::operator<(const Event& evnt) const
{
	return ((_time < evnt._time) || ((_time == evnt._time) && (_eventType == Stop) && (evnt._eventType == Start)));
}

class QB
{
private:
	QB() {};

	int _turnAround;
	multiset<Event> _events;

	void Calculate(int& fromA, int& fromB);
public:
	static void go(string inputFilePath, string outputFilePath);
};

void QB::Calculate(int& fromA, int& fromB)
{
	fromA = 0;
	fromB = 0;

	int atA = 0;
	int atB = 0;
	int inTrip = 0;

	for (multiset<Event>::const_iterator it = _events.begin(); it != _events.end(); ++it)
	{
		switch (it->_eventType)
		{
		case Start:
			if (it->_point == A)
			{
				if (atA > 0)
					--atA;
				else
					++fromA;
			}
			else if (it->_point == B)
			{
				if (atB > 0)
					--atB;
				else
					++fromB;
			}
			++inTrip;
			break;
		case Stop:
			if (it->_point == A)
				++atA;
			else if (it->_point == B)
				++atB;
			++inTrip;
			break;
		}
	}
};

void QB::go(string inputFilePath, string outputFilePath)
{
	ifstream inpf(inputFilePath.c_str());
	ofstream outf(outputFilePath.c_str());

	if (!inpf.good() || !outf.good())
	{
		throw(std::invalid_argument("Can't open input or output file!"));
	}

	int N;
	inpf >> N;

	for (int n = 1; n <= N; ++n)
	{
		QB qB;

		int T;
		inpf >> T;

		int NA, NB;
		inpf >> NA >> NB;
		for (int i = 0; i < NA + NB; ++i)
		{
			Time start(inpf);
			Time stop(inpf);
			stop += Time(0, T);

			qB._events.insert(Event(start, (i < NA) ? A : B, Start)); 
			qB._events.insert(Event(stop, (i >= NA) ? A : B, Stop)); 
		}

		int A, B;
		qB.Calculate(A, B);
		outf << "Case #" << n << ": " << A << " " << B << endl;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	QB::go("input.txt", "output.txt");

	cout << endl;
	getchar();
	return 0;
}

