// GCJ Round X - Problem D
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

double cross_product(tComp a, tComp b)
{
	return real(a) * imag(b) - imag(a) * real(b);
}
double cramer1(tComp a, tComp b, tComp c)
{
	return cross_product(c, b) / cross_product(a, b);
}
tComp line_line_intersection(tComp a, tComp b, tComp c, tComp d)
{
	return a + cramer1(b-a, c-d, c-a) * (b-a);
}
tComp circumcircle(tComp a, tComp b, tComp c)
{
	return line_line_intersection((a+b)/2.0, (a+b)/2.0+(b-a)*tComp(0, 1), (b+c)/2.0, (b+c)/2.0+(c-b)*tComp(0, 1));
}
// code written during the competition follows
tComp solve(tComp z0, tComp z1, double r0, double r1)
{
	tComp z = (z0 + z1) * 0.5;
	if (abs(z0 - z) < EPS)
		return z;
	z0 += (z0 - z) / abs(z0 - z) * r0;	
	z1 += (z1 - z) / abs(z1 - z) * r1;	
	return (z0 + z1) * 0.5;
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		vector<tComp> center;
		vector<double> radius;
		printf("Case #%d: ", tkase+1);
		int n;
		cin >> n;
		for (int i=0; i<n; i++)
		{
			int x, y, r;
			cin >> x >> y >> r;
			center.push_back(tComp(x, y));
			radius.push_back(r);
		}
		vector<tComp> z = center;
		double res = 1e30;
		double ma = 0.0;
		for (int k=0; k<n; k++)
		{
			ma = max(ma, radius[k]);
		}
		if (n == 3)
		{
			for (int i=0; i<3; i++)
				for (int j=i+1; j<3; j++)
				{
					tComp z = solve(center[i], center[j], radius[i], radius[j]);
					res = min(res, max(abs(center[i]-z) + radius[i], abs(center[j]-z) + radius[j]));
				}
		}
		else
		{
			res = ma;
		}
		printf("%.7lf\n", max(res, ma));

	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
