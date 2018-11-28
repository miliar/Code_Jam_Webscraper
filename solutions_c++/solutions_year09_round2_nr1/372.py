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


// ��������� vector �� �����, � ������� �� �������� �� ������ (multiline)
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


// ��������� vector �� �����, � ������� �� ������ ������ ���� ���������� ���������, � ����� �� �������� �� ������ (multiline)
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


struct node
{
	node() :
		w(0),
		true_(0),
		false_(0)
	{
	}

	str name;
	double w;
	node* true_;
	node* false_;
};

node* parse(str& s, sz b)
{
	sz begin = s.find("(", b);
	if (begin == s.npos)
		return 0;

	node* result = new node();
	sz end = s.find(")", begin + 1);
	sz b2 = s.find("(", begin + 1);

	if (b2 < end)
	{
		result->true_ = parse(s, b2);
		result->false_ = parse(s, b2);
	}

	end = s.find(")", begin + 1);
	vecstr ss = dl::split(s.substr(begin + 1, end - begin - 1));
	ss.erase(remove(ss.begin(), ss.end(), ""), ss.end());
	if (ss.size() == 2)
	{
		result->w = cast<double>(ss[0]);
		result->name = ss[1];
	}
	else if (ss.size() == 1)
	{
		result->w = cast<double>(ss[0]);
	}
	else
		throw exception("fuck");

	s.erase(begin, end - begin + 1);
	return result;
}

double count(node* n, const vecstr& ff, double res)
{
	res *= n->w;
	if (n->name.empty())
		return res;

	bool fnd = find(ff.begin(), ff.end(), n->name) != ff.end();
	return count(fnd ? n->true_ : n->false_, ff, res);
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
		sz l = readval<sz>();
		str strt;
		for (sz i = 0; i < l; ++i)
			strt += readval<str>();

		node* n = parse(strt, 0);

		sz a = readval<sz>();
		PRINT("Case #" << current_test <<":" << endl);

		for (sz i = 0; i < a; ++i)
		{
			vecstr ss = readvec<str>();
			if (cast<sz>(ss[1]) != ss.size() - 2)
				throw exception("shit 2");

			ss.erase(ss.begin());
			ss.erase(ss.begin());
			PRINT(count(n, ss, 1) << endl);
		}
	}

	return 0;
}

