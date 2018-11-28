#include <vector>
#include <string>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cassert>

using namespace std;

#define ll long long
#define ld long double
#define pii pair<int, int>
#define vs vector<string>
#define vi vector<int>
#define vvi vector<vi>
#define vl vector<ll>
#define vvl vector<vl>
#define vd vector<double>
#define vvd vector<vd>
#define vp vector<pii>
#define vvp vector<vp>
#define msi map<string, int>
#define mii map<int, int>

#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define twoLL(n) (1LL << (n))
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

inline ll abs(ll a) { return (a < 0) ? -a : a; }
inline ll pow(int a, int b) { ll res = 1; for (int i = 1; i <= b; ++i) res *= a; return res; }
template<typename T> inline vector<T> split(string const & str, string const & delim = "") { string s = str; for (size_t i = 0; i < delim.size(); ++i) replace(s.begin(), s.end(), delim[i], ' '); vector<T> res; istringstream iss(s); T t; while (iss >> t) res.push_back(t); return res; }
template<typename R, typename T> inline R cast(T const & t) { stringstream ss; ss << t; R r; ss >> r; return r; }

#define inf 2100000000
#define eps 1e-9

inline string toString(char ch)
{
	switch (ch)
	{
	case '0': return "0000";
	case '1': return "0001";
	case '2': return "0010";
	case '3': return "0011";
	case '4': return "0100";
	case '5': return "0101";
	case '6': return "0110";
	case '7': return "0111";
	case '8': return "1000";
	case '9': return "1001";
	case 'A': return "1010";
	case 'B': return "1011";
	case 'C': return "1100";
	case 'D': return "1101";
	case 'E': return "1110";
	case 'F': return "1111";
	default: return "";
	}
}

inline bool check(vs & b, int x, int y, int n)
{
	for (int i = x; i < x + n; ++i)
		for (int j = y; j < y + n; ++j)
			if (b[i][j] == '5')
				return false;

	for (int i = x; i < x + n; ++i)
		for (int j = y; j < y + n - 1; ++j)
			if (b[i][j] == b[i][j + 1])
				return false;

	for (int j = y; j < y + n; ++j)
		for (int i = x; i < x + n - 1; ++i)
			if (b[i][j] == b[i + 1][j])
				return false;

	for (int i = x; i < x + n; ++i)
		for (int j = y; j < y + n; ++j)
			b[i][j] = '5';

	return true;
}

int main()
{
	string _task = "C";
	string _in = _task + "-small.in", _out = _task + "-small.out";
	//string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	string ts;
	getline(fin, ts);
	int _N = atoi(ts.c_str());

	for (int _n = 1; _n <= _N; ++_n)
	{
		getline(fin, ts);
		vi t = split<int>(ts);
		int n = t[0], m = t[1];
		
		vs b(n);
		for (int i = 0; i < n; ++i)
		{
			string s;
			getline(fin, s);
			for (int j = 0; j < sz(s); ++j)
				b[i] += toString(s[j]);
		}

		vp res;
		int W = min(n, m);
		for (int w = W; w >= 1; --w)
		{
			int r = 0;
			for (int i = 0; i <= n - w; ++i)
				for (int j = 0; j <= m - w; ++j)
					if (check(b, i, j, w))
						++r;

			if (r != 0)
				res.push_back(pii(w, r));
		}

		fout << "Case #" << _n << ": ";
		fout << sz(res) << endl;
		for (int i = 0; i < sz(res); ++i)
			fout << res[i].first << " " << res[i].second << endl;
	}	

	return 0;
}
