// Task.cpp : Defines the entry point for the console application.
//

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

typedef string str;
typedef vector<str> vecstr;

typedef long long int lint;
typedef vector<lint> veclint;

typedef size_t sz;
typedef vector<sz> vecsz;

typedef long double ld;
typedef vector<ld> vecld;


template <typename To, typename From>
To cast(const From& from)
{
	stringstream strm;
	strm << from;
	To result = To();
	strm >> result;
	assert(strm.eof());
	return result;
}

template <>
str cast(const str& s)
{
	return s;
}

template <typename To, typename From>
vector<To> castvec(const vector<From>& vec)
{
	vector<To> result;
	result.reserve(vec.size());
	for (vecstr::const_iterator it = vec.begin(); it != vec.end(); ++it)
		result.push_back(cast<To>(*it));
	return result;
}

namespace dl
{
	vecstr split(const str& s1, char delimiter = ' ')
	{
		if (s1.empty())
			return vecstr();

		string s(s1);
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
}

template <typename T>
vector<T> getvec(const str& s, char delimiter = ' ')
{
	return castvec<T>(dl::split(s, delimiter));
}

template <typename T>
void getvec_ref(vector<T>& v, const str& s, char delimiter = ' ')
{
	v = getvec<T>(s, delimiter);
}

/////////////////////////////////////////////////

auto_ptr<ifstream> input_file;

template <typename T>
T readval()
{
	str s;
	getline(*input_file, s);
	return cast<T>(s);
}

template <typename T>
void readval_ref(T& t)
{
	t = readval<T>();
}

template <typename T>
vector<T> readvec(char delimiter = ' ')
{
	return castvec<T>(dl::split(readval<str>(), delimiter));
}

template <typename T>
void readvec_ref(vector<T>& v, char delimiter = ' ')
{
	v = readvec(delimiter);
}


// Прочитать vector из файла, в котором по элементу на строку (multiline)
template <typename T>
vector<T> readvec_ml(sz count)
{
	vector<T> result;
	result.reserve(count);	
	for (size_t i = 0; i < count; ++i)
		result.push_back(readval<T>());
	return result;
}

template <typename T>
void readvec_ml_ref(vector<T>& v, sz count)
{
	v = readvec_ml(count);
}


// Прочитать vector из файла, в котором на первой строке идет количество элементов, а потом по элементу на строку (multiline)
template <typename T>
vector<T> readvec_ml()
{	
	return readvec_ml<T>(readval<sz>());	
}

template <typename T>
void readvec_ml_ref(vector<T>& v)
{	
	v = readvec_ml<T>();
}

/////////////////////////////////////////////////

template <typename T>
string vec2str(const vector<T>& vec, const str& delimiter = " ")
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

#define PRINT(expr)							\
if (true)									\
{											\
	stringstream __strm__;					\
	__strm__ << expr;						\
	cout << __strm__.str();					\
	ofstream __f__("result.txt", ios::app);	\
	__f__ << __strm__.str();				\
} else (void)0

bool is_last(const str& s)
{
	for (sz i = 0; i < s.size() - 1; ++i)
		if (s[i] < s[i + 1])
			return false;

	return true;
}

sz find_b(const str& s)
{
	for (sz i = s.size() - 2; i >= 0 ; --i)
		if (s[i] < s[i + 1])
			return i;

	throw exception("zzz");
}

str count(const str& s)
{
	if (is_last(s))
	{
		str res = s;
		res.insert(1, "0");

		sort(res.begin(), res.end());

		if (res[0] == '0')
		{
			for (sz i = 1; i < res.size(); ++i)
			{
				if (res[i] != '0')
				{
					char b = res[i];
					res.erase(i, 1);
					res.insert(0, str(1, b));
					break;
				}
			}
		}

		return res;
	}

	sz b = find_b(s);
	str begin = s.substr(0, b);
	char m = s[b];
	str end = s.substr(b + 1);
	sort(end.begin(), end.end());

	char new_m = 0;
	for (sz i = 0; i < end.size(); ++i)
	{
		if (end[i] > m)
		{
			new_m = end[i];
			end.erase(i, 1);
			break;
		}
	}

	if (!new_m)
		throw exception("ddd");

	end.push_back(m);
	sort(end.begin(), end.end());

	str result = begin;
	result.push_back(new_m);
	result += end;
	return result;
}

int main(int argc, char* argv[])
{
	{
		ofstream result("result.txt");
	}

	input_file.reset(new ifstream(argc > 1 ? argv[1] : "input.in"));

	size_t count_tests = readval<size_t>();	

	for (size_t current_test = 1; current_test <= count_tests; ++current_test)
	{
		str s = readval<str>();

end:
		PRINT("Case #" << current_test <<": " << count(s) << endl);
	}

	return 0;
}

