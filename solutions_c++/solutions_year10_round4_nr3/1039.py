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

const int MAXN = 1000;

int a[MAXN][MAXN], b[MAXN][MAXN];
int n;

void solvecase(int ntest)
{
	cout << "Case #" << ntest << ": ";
	CLR(a, 0);
	CLR(b, 0);
	cin >> n;
	int minx = INF, miny = INF;
	for (int i = 0; i < n; ++i)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		swap(x1, y1);
		swap(x2, y2);
		for (int x = x1; x <= x2; ++x)
			for (int y = y1; y <= y2; ++y)
				a[x][y] = 1;
		minx = min(minx, x1);
		miny = min(miny, y1);
	}
	int cnt = n;
	int res = 0;	
	while (cnt)
	{
		res++;
		for (int i = minx; i < MAXN; ++i)
			for (int j = miny; j < MAXN; ++j)
			{
				if (a[i][j] == 1)
				{
					if (a[i - 1][j] == 0 && a[i][j - 1] == 0)
						b[i][j] = 0;
					else
						b[i][j] = 1;
				}
				else
				{
					if (a[i - 1][j] == 1 && a[i][j - 1] == 1)
						b[i][j] = 1;
					else
						b[i][j] = 0;
				}
			}
		cnt = 0;
		int cminx = INF;
		int cminy = INF;
		for (int i = minx; i < MAXN; ++i)
		{
			for (int j = miny; j < MAXN; ++j) 
			{
				if (b[i][j] == 1)
				{
					cnt++;
					cminx = min(cminx, i);
					cminy = min(cminy, j);
				}
				a[i][j] = b[i][j];
			}
		}
		minx = cminx;
		miny = cminy;
	}
	cout << res << endl;
}

void solve()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
		solvecase(i);
}

int main()
{
	init();
	solve();
	return 0;
}
