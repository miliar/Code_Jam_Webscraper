// Task.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

//#include <set>
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

#define PRINT(expr)							\
if (true)									\
{											\
	stringstream __strm__;					\
	__strm__ << expr;						\
	cout << __strm__.str();					\
	ofstream __f__("result.txt", ios::app);	\
	__f__ << __strm__.str();				\
} else (void)0


typedef pair<long long int, long long int> coord;
typedef vector<coord> trees;

bool valid_c(coord& c1, coord& c2, coord& c3)
{
	if ((c1.first + c2.first + c3.first) % 3 || (c1.second + c2.second + c3.second) % 3)
		return false;
	return true;

}


int _tmain(int argc, _TCHAR* argv[])
{
	{
		ofstream result("result.txt");
	}

	ifstream file("A-small-attempt1.in");

	string str;
	getline(file, str);

	size_t count_tests = cast<size_t>(str);

	for (size_t ct = 1; ct <= count_tests; ++ct)
	{
		getline(file, str);
		vector<long long int> val = castvec<long long int>(split(str));
		long long int n = val[0];
		long long int A = val[1];
		long long int B = val[2];
		long long int C = val[3];
		long long int D = val[4];
		long long int x0 = val[5];
		long long int y0 = val[6];
		long long int M = val[7];

		trees trs;

		long long int X = x0;
		long long int Y = y0;
		trs.push_back(make_pair(X, Y));


		for (int i = 1; i <= n-1; ++i)
		{
			  X = (A * X + B) % M;
			  Y = (C * Y + D) % M;
			  trs.push_back(make_pair(X, Y));
		}

		size_t count = 0;
		for (size_t i = 0; i < trs.size() - 2; ++i)
		{
			for (size_t j = i + 1; j < trs.size() - 1; ++j)
			{
				for (size_t k = j + 1; k < trs.size(); ++k)
				{
					if (valid_c(trs[i], trs[j], trs[k]))
						++count;
				}
			}
		}

		PRINT("Case #" << ct <<": " << count << std::endl);
	}

	return 0;
}

