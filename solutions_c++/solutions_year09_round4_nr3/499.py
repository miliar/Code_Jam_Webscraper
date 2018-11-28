#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <math.h>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define DFOR(i, a, b) for (int (i) = (a) - 1; (i) >= (b); (i)--)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define VI vector <int>
#define VS vector <string>
#define PB push_back
#define MP make_pair
#define SS stringstream
#define INF 1073741824
#define PII pair <int, int>
#define ALL(a) a.begin(), a.end()
#define SZ(x) (int)x.size()

#define LL long long
#define X first
#define Y second

void init()
{
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
}

const int MAXN = 110;

int T;
int n, k;
int a[MAXN][MAXN];
bool g[MAXN][MAXN];
vector < int > c[MAXN];
int p[MAXN];

int sign(int x)
{
	if (x > 0)
		return 1;
	if (x < 0)
		return -1;
	return 0;
}

bool good (int x, vector < int > y)
{
	FOR(i, SZ(y)) if (g[x][y[i]])
		return false;
	return true;
}

bool intersect(int a, int b, int c, int d)
{
	if (a <= c && b >= d)
		return true;
	if (c <= a && d >= b)
		return true;
	return false;
}

int calcperm()
{
	FOR(i, n) c[i].clear();
	int m = 0;
	FOR(i, n) {
		bool ok = false;
		FOR(j, m) {
			if (good(p[i], c[j]))
			{
				c[j].PB(p[i]);
				ok = true;
				break;
			}
		}
		if (!ok) {
			m++;
			c[m - 1].PB(p[i]);
		}
	}
	return m;
}

void genperm()
{
	CLR(p, 0);
	FOR(i, n) {
		p[i] = i;
		int j = rand() % (i + 1);
		swap(p[i], p[j]);				
	}
}

void solvecase(int test)
{
	cout << "Case #" << test << ": ";
	cin >> n >> k;
	CLR(a, 0);
	CLR(g, 0);
	FOR(i, n) FOR(j, k) 
		cin >> a[i][j];
	FOR(i, n) for (int j = i + 1; j < n; ++j)
	{
		bool ok = true;
		FOR(t, k) {
			if (a[i][t] == a[j][t])
			{
				ok = false;
				break;
			}
			if (t + 1 < k && intersect(a[i][t], a[i][t + 1], a[j][t], a[j][t + 1]))
			{
				ok = false;
				break;
			}
		}
		g[i][j] = g[j][i] = !ok; // есть ребро, значит нельзя, чтобы были в одной компоненте
	}

	int res = 10000;
	FOR(i, 25000)
	{
		genperm();
		res = min(res, calcperm());
	}
	cout << res << endl;
}

void solve()
{
	cin >> T;
	FOR(i, T) solvecase(i + 1);
}

int main()
{
	init();
	solve();
	return 0;
}