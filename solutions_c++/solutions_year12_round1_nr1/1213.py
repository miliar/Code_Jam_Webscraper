#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define EPS 1e-9
#define LL long long

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )
#define rrep( i, a, b ) for( __typeof(b) i = ( a ); i >= ( b ); --i )
#define xrep( i, a, b ) _rep( i, a, b, 1 )

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

typedef vector <int> vi;

int tcase;

const int MAX = 100000+10;

double P[MAX];
int A, B;

double CP[MAX];

double solve(int pos, int mask)
{
	CP[0] = 1.0;
	xrep(i,1,A)
		CP[i] = CP[i-1] * P[i-1];

	double ret;
	double x;
	bool ok = false;

	xrep(i,1,A)
	{
		int rest = A - i;
		x = CP[rest] * (i + B - A + i + 1) + (1.0 - CP[rest]) * (i + B - A + i + 1 + B + 1);
		if (!ok || ret > x) ret = x, ok = true;

	}
	return ret;
}

int main()
{
	freopen("/home/user/codejam/r1p1b.txt", "r", stdin);
	freopen("/home/user/codejam/r1p1bo.txt", "w", stdout);
	scanf("%d", &tcase);

	xrep(caseno,1,tcase)
	{
		scanf("%d %d", &A, &B);
		double prod = 1.0;
		rep(i,A) scanf("%lf", &P[i]), prod *= P[i];
		double ans = solve(0,0);
		ans = min(ans, prod*(B-A+1) + (1-prod)*(B-A+2+B));
		ans = min(ans, 2.+B);
		printf("Case #%d: %.6lf\n", caseno, ans);
	}
}
