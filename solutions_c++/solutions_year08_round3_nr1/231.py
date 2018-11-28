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
typedef vector<long long int> vecsz;
typedef vector<int> vecint;
typedef vector<long double> vecldbl;

vecstr split(const string& str, char delimiter = ' ')
{
	if (str.empty())
		return vecstr();

	string s(str);
	if (s[s.size() - 1] != delimiter)
		s.push_back(delimiter);

	vecstr result;

	long long int begin = 0;
	while (true)
	{
		long long int end = s.find(delimiter, begin);
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


typedef pair<long long int, long long int> freq2num;
typedef vector<freq2num> lets;
typedef vector<lets> keys;

long long int count(long long int p, long long int k, lets& ls)
{
	keys ks(k);

	sort(ls.begin(), ls.end());

	long long int cur_key = 0;

	for (lets::const_reverse_iterator it = ls.rbegin(); it != ls.rend(); ++it)
	{
		ks[cur_key].push_back(*it);

		++cur_key;
		cur_key = cur_key % k;
	}

	long long int result = 0;
	for (long long int i = 0; i < ks.size(); ++i)
	{
		for (long long int j = 0; j < ks[i].size(); ++j)
		{
			result += ks[i][j].first * (j + 1);
		}
	}

	return result;
	
}


int _tmain(int argc, _TCHAR* argv[])
{
	{
		ofstream result("result.txt");
	}

	ifstream file("A-large.in");

	string str;
	getline(file, str);

	long long int count_tests = cast<long long int>(str);

	for (long long int ct = 1; ct <= count_tests; ++ct)
	{
		getline(file, str);
		vecsz p = getvec<long long int>(str);

		getline(file, str);
		vecsz l = getvec<long long int>(str);

		lets ls;
		ls.reserve(l.size());

		for (long long int i = 0; i < l.size(); ++i)
			ls.push_back(make_pair<long long int, long long int>(l[i], i));

		long long int result = count(p[0], p[1], ls);

		PRINT("Case #" << ct <<": " << result << std::endl);
	}

	return 0;
}

