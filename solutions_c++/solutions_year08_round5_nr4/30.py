// GCJ Round 3 - Problem D
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
int X[20], Y[20];
/*
int solve(int x, int y)
{
	if (x < 0 || y < 0)
		return 0;
	int z = x + y;
	if (z % 3)
		return 0;
	int m = z / 3;
	int a = x0 
}*/
const int MOD = 10007;
int a[128][128];
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int H, W, R;
		cin >> H >> W >> R;
		memset(a, 0, sizeof a);
		for (int i=0; i<R; i++)
		{
			cin >> X[i] >> Y[i];
		}
		a[1][1] = 1;
		for (int i=1; i<=H; i++)
			for (int j=1; j<=W; j++)
			{
				bool good = true;
				for (int k=0; k<R; k++)
					if (i == X[k] && j == Y[k])
						good = false;
				if (!good)
					continue;
				a[i][j] %= MOD;
				a[i+2][j+1] += a[i][j];
				a[i+1][j+2] += a[i][j];
			}
		printf("Case #%d: %d\n", tkase+1, a[H][W]);
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
