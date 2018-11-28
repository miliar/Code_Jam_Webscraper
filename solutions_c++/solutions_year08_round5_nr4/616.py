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


int move[8][2] = { {2, 1}, {1, 2} };

vector<vector<ll> > b;
int n, m;

int get(int x, int y)
{
	ll & res = b[x][y];
	if (b[x][y] != -1)
		return res;

	if (x == n - 1 && y == m - 1)
	{
		return res = 1;
	}
	res = 0;
	for (int dir = 0; dir < 2; ++dir)
	{
		int xx = x + move[dir][0], yy = y + move[dir][1];
		if (xx < 0 || xx >= n || yy < 0 || yy >= m)
			continue;

		if (b[xx][yy] == inf) 
			continue;

		res += get(xx, yy);
	}
	res %= 10007;
	return res;

}

int main(int argc, char* argv[])
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
		

		//getline(fin, ts);
		//int n = atoi(ts.c_str());
		
		getline(fin, ts);
		vi t = split<int>(ts);
		n = t[0], m = t[1];
		int r = t[2];
		
		b.assign(n, vl(m, -1));

		vp obs;
		for (int i = 0; i < r; ++i)
		{
			getline(fin, ts);
			vi t1 = split<int>(ts);
			obs.push_back(pii(t1[0] - 1, t1[1] - 1));
			b[obs.back().first][obs.back().second] = inf;
		}
		
		int res = get(0, 0);
		

		fout << "Case #" << _n << ": ";
		
		fout << res;

		fout << endl;
	}	

	return 0;
}
