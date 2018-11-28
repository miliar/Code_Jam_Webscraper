// GCJ Round 2 - Problem B
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
//(-x3*y2 + x2*y3) / 2;
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		printf("Case #%d: ", tkase+1);
		int A, m, n;
		cin >> n >> m >> A;
		bool good = false;
		for (int a=1; a<=n; a++)
		{
			if (A % a == 0 && A / a <= m)
			{
				cout << "0 0 " << a << " " << 0 << " " << 0 << " " << A/a << endl;
				good = true;
				break;
			}
		}
		if (!good)
			for (int c=1; c<=n && m * n >= A + c; c++)
			{
				for (int d=1; d<=m; d++)
				{
					int A0 = A + c * d;
					if (A0 > m * n || A0 / m > n || A0 / n > m)
						break;
					for (int a=n; a>=1; a--)
						if (A0 % a == 0)
						{
							int b = A0 / a;
							if (b <= m)
							{
								good = true;
								cout << "0 0 " << a << " " << d << " " << c << " " << b << endl;
								goto done;
							}
							else
								break;
						}
				}
			}
		done:;
		if (!good)
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
