// GCJ Round 2 - Problem A
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

const int MAX = 1024 * 1024;
int value[MAX];
int gate[MAX], change[MAX];
int dp[MAX][2];
int op(int a, int b, int o)
{
	if (o == 1)
		return a && b;
	return a || b;
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int m, v;
		cin >> m >> v;
		for (int i=1; i<=m; i++)
		{
			if (i <= m / 2)
			{
				cin >> gate[i] >> change[i];
			}
			else
			{
				cin >> value[i];
				dp[i][value[i]] = 0;
				dp[i][!value[i]] = oo;
			}
		}
		for (int i=m/2; i>=1; i--)
		{
			for (int j=0; j<2; j++)
				dp[i][j] = oo;
			for (int j=0; j<2; j++)
			{
				if (change[i] == 0 && gate[i] != j)
					continue;
				int tmp = (gate[i] != j);
				for (int jj=0; jj<2; jj++)
					for (int kk=0; kk<2; kk++)
					{
						dp[i][op(jj, kk, j)] <?= dp[2*i][jj] + dp[2*i+1][kk] + tmp;
					}
			}
		}
		/*
		for (int i=1; i<=m; i++)
		{
			cout << "(" << dp[i][0] << " " << dp[i][1] << ") ";
			if (__builtin_popcount(i+1) == 1)
				cout << endl;
		}
		cout << endl;
		*/
		printf("Case #%d: ", tkase+1);
		if (dp[1][v] < oo)
			cout << dp[1][v] << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
