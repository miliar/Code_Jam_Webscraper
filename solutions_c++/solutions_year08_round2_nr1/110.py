// GCJ Round 1B - Problem A
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
LL a[3][3];
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int n;
		LL A, B, C, D;
		LL x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		VPII v(n);
		LL X = x0, Y = y0;
		v[0] = PII(X, Y);
		for (int i=1; i<n; i++)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			v[i] = PII(X, Y);
		}
		for (int i=0; i<3; i++)
			for (int j=0; j<3; j++)
				a[i][j] = 0;
		FORIT(it, v)
		{
			int x = it->first % 3;
			int y = it->second % 3;
			a[x][y]++;
		}
		LL res = 0;
		FORIT(it, v)
		{
			int x = it->first % 3;
			int y = it->second % 3;
			a[x][y]--;
			for (int i=0; i<3; i++)
				for (int j=0; j<3; j++)
					for (int ii=0; ii<3; ii++)
						for (int jj=0; jj<3; jj++)
						{
							if (PII(i, j) < PII(ii, jj))
								continue;
							if ((x + i + ii) % 3 || (y + j + jj) % 3)
							{
								continue;
							}
							if (i != ii || j != jj)
							{
								res += a[i][j] * a[ii][jj];
							}
							else
							{
								res += (a[i][j] * (a[i][j] - 1)) / 2;
							}
						}
		}

		printf("Case #%d: ", tkase+1);
		cout << res << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
