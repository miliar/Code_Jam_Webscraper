// GCJ Round 3 - Problem A
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
const int N = 6006;
char a[2*N][2*N];
#define INSIDE(x, y) ((x) >= 0 && (y) >= 0 && (x) < 2*N && (y) < 2*N)
// clockwise (right, down, left, up)
const int X[] = {0, 1, 0, -1};
const int Y[] = {1, 0, -1, 0};

int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int len;
		cin >> len;
		memset(a, 0, sizeof a);
		int d = 0;
		int x = 0, y = 0;
		for (int i=0; i<len; i++)
		{
			string s;
			int t;
			cin >> s >> t;
			for (int j=0; j<t; j++)
			{
				FORIT(it, s)
				{
					if (*it == 'L')
					{
						d--;
						if (d < 0)
							d = 3;
					}
					else if (*it == 'R')
					{
						d++;
						if (d == 4)
							d = 0;
					}
					else
					{
						x += X[d], y += Y[d];
						a[x+N][y+N] = 1;
						x += X[d], y += Y[d];
						a[x+N][y+N] = 1;
					}
				}
			}
		}
		queue<PII> q;
		q.push(PII(0, 0));
		a[0][0] = 2;
		while (!q.empty())
		{
			PII act = q.front();
			q.pop();
			int x = act.first, y = act.second;
			for (int k=0; k<4; k++)
			{
				int nx = x + X[k], ny = y + Y[k];
				if (INSIDE(nx, ny) && a[nx][ny] == 0)
				{
					a[nx][ny] = 2;
					q.push(PII(nx, ny));
				}
			}
		}
		for (int k=0; k<2; k++)
		{
			for (int i=1; i<2*N-1; i++)
				for (int j=1; j<2*N-1; j++)
				{
					if (a[i][j] < 2)
						continue;
					int nx = i + X[k+2], ny = j + Y[k+2];
					if (a[nx][ny] != 1)
						continue;
					int x = i, y = j;
					bool good = false;
					while (x < 2*N && y <2*N)
					{
						if (a[x][y] == 1)
						{
							good = true;
							break;
						}
						x += X[k], y += Y[k];
					}
					if (good)
					{
						int x = i, y = j;
						while (x < 2*N && y <2*N)
						{
							assert(a[x][y]);
							if (a[x][y] == 1)
							{
								break;
							}
							a[x][y] = 3;
							x += X[k], y += Y[k];
						}
					}
				}
		}
		int cnt = 0;
		for (int i=1; i<2*N-1; i+=2)
			for (int j=1; j<2*N-1; j+=2)
				if (a[i][j] == 3)
					cnt++;
		printf("Case #%d: %d\n", tkase+1, cnt);
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
