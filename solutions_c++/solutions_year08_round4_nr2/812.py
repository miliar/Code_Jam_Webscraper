// Task.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <set>
#include <map>
#include <vector>
#include <memory>
#include <utility>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cassert>

using namespace std;

template <typename To, typename From>
To cast(const From& from)
{
	stringstream strm;
	strm << from;
	To result = To();
	strm >> result;
	return result;
}

typedef vector<string> vecstr;
typedef long long int lint;
typedef vector<lint> veclint;
typedef vector<size_t> vecsz;
typedef vector<int> vecint;
typedef long double ld;
typedef vector<ld> vecld;

vecstr split(const string& str, char delimiter = ' ')
{
	if (str.empty())
		return vecstr();

	string s(str);
	if (s[s.size() - 1] != delimiter)
		s.push_back(delimiter);

	vecstr result;

	size_t begin = 0;
	while (true)
	{
		size_t end = s.find(delimiter, begin);
		result.push_back(s.substr(begin, end - begin));

		if (end == s.size() - 1)
			break;

		begin = end + 1;
	}

	return result;
}

template <typename T>
string vec2str(const vector<T>& vec, const string& delimiter = " ")
{
	if (vec.empty())
		return "";

	vector<T>::const_iterator it = vec.begin();

	ostringstream result;
	result << *it;
	++it;

	for (; it != vec.end(); ++it)
		result << delimiter << *it;

	return result.str();
}

template <typename T>
vector<T> castvec(const vecstr& vec)
{
	vector<T> result;
	result.reserve(vec.size());
	for (vecstr::const_iterator it = vec.begin(); it != vec.end(); ++it)
		result.push_back(cast<T>(*it));
	return result;
}

template <typename T>
vector<T> getvec(const string& str)
{
	return castvec<T>(split(str));
}

#define PRINT(expr)							\
if (true)									\
{											\
	stringstream __strm__;					\
	__strm__ << expr;						\
	cout << __strm__.str();					\
	ofstream __f__("result.txt", ios::app);	\
	__f__ << __strm__.str();				\
} else (void)0


typedef size_t sz;

lint Square2(sz x1, sz y1, sz x2, sz y2, sz x3, sz y3)
{
	lint sq2 = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
	if (sq2 < 0)
		sq2 = -sq2;

	return sq2;
}

bool Find(lint A, sz N, sz M, sz& x1, sz& y1, sz& x2, sz& y2, sz& x3, sz& y3)
{
	x1 = 0;
	y1 = 0;

	//for (x1 = 0; x1 <= N; ++x1)
		for (y1 = 0; y1 <= M; ++y1)
			for (x2 = 0; x2 <= N; ++x2)
				for (y2 = 0; y2 <= M; ++y2)
					for (x3 = 0; x3 <= N; ++x3)
						for (y3 = 0; y3 <= M; ++y3)
						{
							lint sq2 = Square2(x1, y1, x2, y2, x3, y3);
							if (sq2 == A)
								return true;

							if (sq2 > A)
								break;
						}

	return false;				
}


int _tmain(int argc, _TCHAR* argv[])
{
	{
		ofstream result("result.txt");
	}

	ifstream file("B-small-attempt1.in");

	string str;
	getline(file, str);

	size_t count_tests = cast<size_t>(str);

	for (size_t ct = 1; ct <= count_tests; ++ct)
	{
		getline(file, str);
		veclint data = getvec<lint>(str);
		sz N = data[0];
		sz M = data[1];
		lint A = data[2];

		sz x1;
		sz y1;
		sz x2;
		sz y2;
		sz x3;
		sz y3;		

		bool f = Find(A, N, M, x1, y1, x2, y2, x3, y3);

		if (f)
		{
			PRINT("Case #" << ct <<": " << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << std::endl);
		}
		else
		{
			PRINT("Case #" << ct <<": " << "IMPOSSIBLE" << std::endl);
		}
	}

	return 0;
}

