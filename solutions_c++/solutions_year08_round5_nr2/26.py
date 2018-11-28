// GCJ Round 3 - Problem B
// I can't tell you how proud I am,
// I'm writing down things that I don't understand.
// -- blackmath

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
const LL OO = 1000000000000000000LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}

// code written during the competition follows

char a[18][19];
int vis[18][18][18][18][18][18];
struct State
{
	int x, y, x0, y0, x1, y1;
	bool marked()
	{
		return vis[x][y][x0][y0][x1][y1];
	}
	void mark()
	{
		vis[x][y][x0][y0][x1][y1] = 1;
	}
};
const int X[] = {0, 1, 0, -1};
const int Y[] = {1, 0, -1, 0};
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		memset(vis, 0, sizeof vis);
		int m, n;
		scanf("%d %d ", &m, &n);
		for (int i=0; i<18; i++)
			for (int j=0; j<18; j++)
				a[i][j] = '#';
		for (int i=0; i<m; i++)
		{
			string s;
			cin >> s;
			for (int j=0; j<n; j++)
				a[i+1][j+1] = s[j];
		}
		int sx = 0, sy = 0, cx = 0, cy = 0;
		for (int i=0; i<18; i++)
			for (int j=0; j<18; j++)
			{
				if (a[i][j] == 'O')
				{
					sx = i, sy = j;
					a[i][j] = '.';
				}
				if (a[i][j] == 'X')
				{
					cx = i, cy = j;
					a[i][j] = '.';
				}
			}
		/*
		for (int i=0; i<18; i++)
			cout << a[i] << endl;
		*/
		State start;
		start.x = sx;
		start.y = sy;
		start.x0 = start.y0 = start.x1 = start.y1 = 0;
		queue<State> q;
		queue<State> next;
		q.push(start);
		start.mark();
		bool found = false;
		for (int i=0; !q.empty() && !found; i++)
		{
			while (!q.empty())
			{
				State act = q.front();
				q.pop();
				int x = act.x, y = act.y;
				if (x == cx && y == cy)
				{
					found = true;
					printf("Case #%d: %d\n", tkase+1, i);
					break;
				}
				for (int k=0; k<4; k++)
				{
					int nx = x + X[k], ny = y + Y[k];
					if (a[nx][ny] == '.')
					{
						State tmp = act;
						tmp.x = nx;
						tmp.y = ny;
						if (!tmp.marked())
						{
							tmp.mark();
							next.push(tmp);
						}
					}
				}
				for (int k=0; k<4; k++)
				{
					int tx = x, ty = y;
					while (a[tx][ty] == '.')
						tx += X[k], ty += Y[k];
					tx -= X[k], ty -= Y[k];
					State tmp0 = act;
					tmp0.x0 = tx;
					tmp0.y0 = ty;
					if (!tmp0.marked())
					{
						tmp0.mark();
						q.push(tmp0);
					}
					State tmp1 = act;
					tmp1.x1 = tx;
					tmp1.y1 = ty;
					if (!tmp1.marked())
					{
						tmp1.mark();
						q.push(tmp1);
					}
				}
				if (x == act.x0 && y == act.y0 && a[act.x1][act.y1] == '.')
				{
					State tmp = act;
					tmp.x = act.x1;
					tmp.y = act.y1;
					if (!tmp.marked())
					{
						tmp.mark();
						next.push(tmp);
					}
				}
				if (x == act.x1 && y == act.y1 && a[act.x0][act.y0] == '.')
				{
					State tmp = act;
					tmp.x = act.x0;
					tmp.y = act.y0;
					if (!tmp.marked())
					{
						tmp.mark();
						next.push(tmp);
					}
				}
			}
			swap(next, q);
		}
		if (!found)
			printf("Case #%d: THE CAKE IS A LIE\n", tkase+1);

	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
