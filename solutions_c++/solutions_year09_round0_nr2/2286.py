// GCJ Qualification Round - Problem B
// -- strapahuulius

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
const int dx[] = {-1,0,0,1}, dy[] = {0,-1,1,0};
int h,w;
int field[128][128];
char label[128][128];

bool flows(int i, int j, int a, int b)
{
	int minimum = field[i][j];
	for (int d=0; d<4; d++)
	{
		int x = i+dx[d], y = j+dy[d];
		if (x<0 || x>=h || y<0 || y>=w)
			continue;
		minimum = min(minimum, field[x][y]);
	}
	if (minimum>=field[i][j] || field[a][b]!=minimum)
		return false;
	for (int d=0; d<4; d++)
	{
		int x = i+dx[d], y = j+dy[d];
		if (x<0 || x>=h || y<0 || y>=w)
			continue;
		if (field[x][y]==minimum)
			return x==a && y==b;
	}
	assert(false);
}

void dfs(int i, int j, char l)
{
	label[i][j] = l;
	for (int d=0; d<4; d++)
	{
		int x = i+dx[d], y = j+dy[d];
		if (x<0 || x>=h || y<0 || y>=w || label[x][y])
			continue;
		if (flows(i,j,x,y) || flows(x,y,i,j))
			dfs(x, y, l);
	}
}

int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		scanf("%d%d\n", &h, &w);
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++)
				scanf("%d ", &field[i][j]);
		memset(label, 0, sizeof(label));

		char cur = 'a';
		printf("Case #%d:\n", tkase+1);
		for (int i=0; i<h; i++)
		{
			for (int j=0; j<w; j++)
			{
				if (!label[i][j])
					dfs(i, j, cur++);
				if (j)
					putchar(' ');
				putchar(label[i][j]);
			}
			putchar('\n');
		}
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
