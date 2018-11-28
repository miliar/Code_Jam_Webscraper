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
#include <limits>
#include <queue>

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

vector<vecsz> alt;
vector<vector<char> > result;

bool is_basin(sz x, sz y)
{
	sz cur = alt[y][x];
	if (cur > alt[y - 1][x])
		return false;
	if (cur > alt[y + 1][x])
		return false;

	if (cur > alt[y][x - 1])
		return false;
	if (cur > alt[y][x + 1])
		return false;

	return true;
}

bool is_belong(sz x, sz y, sz to_x, sz to_y)
{
	sz to_alt = alt[to_y][to_x];
	sz alt_ = alt[y][x];
	
	// North, West, East, South.
	sz dx[] = {0, -1, 1, 0};
	sz dy[] = {-1, 0, 0, 1};
	
	sz best_x;
	sz best_y;
	sz best_alt = alt_;

	bool found = false;

	for (sz i = 0; i < 4; ++i)
	{
		sz cur_x = x + dx[i];
		sz cur_y = y + dy[i];
		sz cur_alt = alt[cur_y][cur_x];
		
		if (best_alt > cur_alt)
		{
			best_alt = cur_alt;
			best_x = cur_x;
			best_y = cur_y;
			found = true;
		}
	}

	return found && best_x == to_x && best_y == to_y;
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
		alt.clear();
		result.clear();

		vecsz hw = readvec<sz>();
		sz h = hw[0];
		sz w = hw[1];

		alt.push_back(vecsz(w + 2, numeric_limits<sz>::max()));
		for (sz i = 0; i < h; ++i)
		{
			alt.push_back(readvec<sz>());

			if (alt.back().size() != w)
				throw exception("fuck");

			alt.back().insert(alt.back().begin(), numeric_limits<sz>::max());
			alt.back().insert(alt.back().end(), numeric_limits<sz>::max());
		}
		alt.push_back(vecsz(w + 2, numeric_limits<sz>::max()));

		result.resize(h + 2, vector<char>(w + 2, 0));

		char cur_basin = 1;

		typedef pair<sz, sz> xy;
		typedef queue<xy> que;
		que to_process;

		sz dx[] = {0, -1, 1, 0};
		sz dy[] = {-1, 0, 0, 1};

		for (sz y = 1; y <= h; ++y)
			for (sz x = 1; x <= w; ++x)
			{
				if (result[y][x])
					continue;

				if (is_basin(x, y))
				{
					++cur_basin;
					result[y][x] = cur_basin;
					to_process.push(xy(x, y));
				}

				while (!to_process.empty())
				{
					xy p = to_process.front();
					to_process.pop();

					for (sz d = 0; d < 4; ++d)
					{
						sz cur_x = p.first + dx[d];
						sz cur_y = p.second + dy[d];
						if (cur_x >= 1 && cur_x <= w && cur_y >= 1 && cur_y <= h && !result[cur_y][cur_x] && is_belong(cur_x, cur_y, p.first, p.second))
						{
							result[cur_y][cur_x] = cur_basin;
							to_process.push(xy(cur_x, cur_y));
						}
					}
				}
			}

		vector<char> bas2ch(cur_basin + 1, 0);
		char cur_ch = 'a';

		for (sz y = 1; y <= h; ++y)
			for (sz x = 1; x <= w; ++x)
			{
				if (result[y][x] > cur_basin)
					continue;

				if (!bas2ch[result[y][x]])
				{
					bas2ch[result[y][x]] = cur_ch;
					++cur_ch;
				}

				result[y][x] = bas2ch[result[y][x]];
			}

end:
		PRINT("Case #" << current_test <<":" << endl);

		for (sz y = 1; y <= h; ++y)
		{
			vector<char> to_print(result[y].begin() + 1, result[y].end() - 1);
			if (find(to_print.begin(), to_print.end(), 0) != to_print.end())
				throw std::exception("fuck2");

			PRINT(vec2str(to_print) << endl);
		}
	}

	return 0;
}

