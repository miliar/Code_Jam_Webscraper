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
		int R = atoi(ts.c_str());

		vs b(110, string(110, '0'));
		for (int i = 0; i < R; ++i)
		{
			getline(fin, ts);
			vi t = split<int>(ts);
		
			for (int j = t[0]; j <= t[2]; ++j)
				for (int k = t[1]; k <= t[3]; ++k)
					b[k][j] = '1';
		}		

		int res = 0;
		while (true)
		{
			bool ok = false;

			vs next(110, string(110, '0'));
			for (int i = 1; i < sz(next); ++i)
				for (int j = 1; j < sz(next[0]); ++j)
				{
					if (b[i][j] == '1' && b[i - 1][j] == '0' && b[i][j - 1] == '0')
						next[i][j] = '0';
					else if (b[i][j] == '0' && b[i - 1][j] == '1' && b[i][j - 1] == '1')
						next[i][j] = '1';
					else 
						next[i][j] = b[i][j];

					if (next[i][j] == '1')
						ok = true;
				}

			++res;
			b = next;
			if (!ok)
				break;
		}

		fout << "Case #" << _n << ": ";	
		fout << res;
		fout << endl;
	}	

	return 0;
}
