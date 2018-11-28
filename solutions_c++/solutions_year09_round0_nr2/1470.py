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

int n, m;
vvi b;
vs res;

int move[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

void dfs(int x, int y, char & label)
{
	res[x][y] = '*';
	
	int bh = inf, bx = -1, by = -1;
	for (int dir = 0; dir < 4; ++dir)
	{
		int xx = x + move[dir][0];
		int yy = y + move[dir][1];
		if (xx < 0 || xx >= n || yy < 0 || yy >= m)
			continue;

		if (b[xx][yy] < b[x][y] && b[xx][yy] < bh)
		{
			bh = b[xx][yy];
			bx = xx;
			by = yy;
		}
	}

	if (bh != inf)
	{
		if (res[bx][by] != '.')
		{
			assert(res[bx][by] != '*');
			label = res[bx][by];
		}
		else
			dfs(bx, by, label);
	}

	res[x][y] = label;
}

int main()
{
	string _task = "B";
	//string _in = _task + "-small.in", _out = _task + "-small.out";
	string _in = _task + "-large.in", _out = _task + "-large.out";
	ifstream fin(_in.c_str());
	ofstream fout(_out.c_str());

	string ts;
	getline(fin, ts);
	int _N = atoi(ts.c_str());

	for (int _n = 1; _n <= _N; ++_n)
	{
		getline(fin, ts);
		vi t = split<int>(ts);
		n = t[0], m = t[1];

		b.assign(n, vi());
		for (int i = 0; i < n; ++i)
		{
			getline(fin, ts);
			b[i] = split<int>(ts);
			assert(sz(b[i]) == m);
		}
		
		res.assign(n, string(m, '.'));

		char label = 'a';
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (res[i][j] == '.')
				{
					dfs(i, j, label);
					for (int ii = 0; ii < n; ++ii)
						for (int jj = 0; jj < m; ++jj)
							if (res[ii][jj] != '.')
								label = max(label, res[ii][jj]);
					++label;
				}

		fout << "Case #" << _n << ":" << endl;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				fout << res[i][j];
				if (j != m - 1)
					fout << ' ';
			}
			fout << endl;
		}
	}	

	return 0;
}
