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

inline double rdist(double x1, double y1, double x2, double y2) { return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)); }

int main()
{
	string _task = "D";
	string _in = _task + "-small.in", _out = _task + "-small.out";
	//string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	string ts;
	getline(fin, ts);
	int _N = atoi(ts.c_str());

	for (int _n = 1; _n <= _N; ++_n)
	{
		// don't forget to clear all global objects!
		

		getline(fin, ts);
		int n = atoi(ts.c_str());

		vi x, y, r;
		for (int i = 0; i < n; ++i)
		{
			getline(fin, ts);
			vi t = split<int>(ts);
			x.push_back(t[0]);
			y.push_back(t[1]);
			r.push_back(t[2]);
		}
		
		double res = inf;
		if (n == 1)
			res = r[0];
		else if (n == 2)
			res = max(r[0], r[1]);
		else if (n == 3)
		{
			for (int i = 0; i < n; ++i)
				for (int j = i + 1; j < n; ++j)
					for (int k = 0; k < n; ++k)
						if (k != i && k != j)
						{
							double re = max((double)r[k], (rdist(x[i], y[i], x[j], y[j]) + r[i] + r[j]) / 2);
							res = min(res, re);
						}
		}
		else
			assert(false);
		fout << "Case #" << _n << ": ";
		fout << res;
		fout << endl;
	}	

	return 0;
}
