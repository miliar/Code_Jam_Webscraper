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

vecstr words;
sz len;

bool less_begin(const str& lhs, const str& rhs)
{
	sz min_sz = min(lhs.size(), rhs.size());
	return lhs.compare(0, min_sz, rhs) < 0;
}

bool check_begin(const str& beg)
{
	if (beg.empty())
		return true;

	str new_beg = beg;
	new_beg.resize(len, 'a');

	vecstr::const_iterator it = lower_bound(words.begin(), words.end(), new_beg);
	return it != words.end() && !it->compare(0, beg.size(), beg);
}

sz gen(const str& pat)
{
	sz beg = pat.find("(");
	if (beg == pat.npos)
	{
		if (pat.size() != len)
			throw exception("fuck 2");
		
		return std::binary_search(words.begin(), words.end(), pat);
	}

	sz end = pat.find(")", beg);

	str beg_pat = pat.substr(0, beg);
	if (!check_begin(beg_pat))
		return 0;

	str end_pat = pat.substr(end + 1);

	str mid = pat.substr(beg + 1, end - beg - 1);
	if (mid.empty())
		throw exception("fuck 3");

	sz res = 0;
	for (sz i = 0; i < mid.size(); ++i)
		res += gen(beg_pat + mid[i] + end_pat);
	return res;
}

int main(int argc, char* argv[])
{
	{
		ofstream result("result.txt");
	}

	input_file.reset(new ifstream(argc > 1 ? argv[1] : "input.in"));

	vecsz info_tests = readvec<sz>();
	len = info_tests[0];
	
	for (sz w = 0; w < info_tests[1]; ++w)
	{
		words.push_back(readval<str>());

		if (words.back().size() != len)
			throw std::exception("fuck");
	}

	sort(words.begin(), words.end());

	for (sz current_test = 1; current_test <= info_tests[2]; ++current_test)
	{
end:
		PRINT("Case #" << current_test <<": " << gen(readval<str>()) << endl);
	}

	return 0;
}

