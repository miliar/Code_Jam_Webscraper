// GCJ Round 3 - Problem C
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
string input[20];
int dp[11][1<<10];
int bad[1 << 10];
int main()
{
	for (int i=0; i<(1<<10); i++)
	{
		int tmp = 0;
		for (int j=0; j<10; j++)
		{
			if (i & (1 << j))
			{
				for (int z = -1; z<=1; z+=2)
				{
					int k = j + z;
					if (k < 0)
						continue;
					tmp |= 1 << k;
				}
			}
		}
		bad[i] = tmp;
	}
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int m, n;
		cin >> m >> n;
		for (int i=0; i<m; i++)
			cin >> input[i];
		memset(dp, 0, sizeof dp);
		int K = 1 << n;
		int res = 0;
		for (int i=m; i>=1; i--)
		{
			int z = 0;
			for (int j=0; j<n; j++)
				if (input[i-1][j] == 'x')
					z |= 1 << j;
			for (int j=0; j<K; j++)
			{
				if (j & z)
					continue;
				bool good = true;
				for (int k=0; k<n; k++)
					if ((j & ((1 << k) | (1 << k+1))) == ((1 << k) | (1 << k+1)))
					{
						good = false;
						break;
					}
				if (!good)
					continue;
				for (int k=0; k<K; k++)
				{
					if (bad[k] & j)
						continue;
					dp[i-1][j] >?= dp[i][k] + __builtin_popcount(j);
					res >?= dp[i-1][j];
				}
			}
		}
		printf("Case #%d: ", tkase+1);
		cout << res << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
