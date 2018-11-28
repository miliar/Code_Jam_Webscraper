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
#include <limits>

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


bool is_ugly(lint v)
{
	if ((v % 2 == 0) || (v % 3 == 0) || (v % 5 == 0) || (v % 7 == 0))
		return true;

	return false;
}


lint count(const string& num, lint init)
{
	lint res = is_ugly(_atoi64(num.c_str()) + init) ? 1 : 0;
	for (lint i = 1; i < num.size(); ++i)
	{
		string snum1(num.substr(0, i));
		string snum2(num.substr(i));

		res += count(snum2, init + _atoi64(snum1.c_str()));
		res += count(snum2, init - _atoi64(snum1.c_str()));
	}

	return res;
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
		lint res = count(str, 0);
		PRINT("Case #" << ct <<": " << res << std::endl);
	}

	return 0;
}

