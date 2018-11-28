#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int inf = 2000 * 1000 * 1000;
const lint linf = 2000000000000000000LL;
const double eps = 1e-9;

void prepare( )
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

double x,s,r,t;
int n;
double a[1005];
double b[1005];
double v[1005];
pair < double , double > f[1005];

bool solve( )
{
	cin >> x >> s >> r >> t >> n;
	for ( int i = 0; i < n; i ++ )
	{
		cin >> a[i] >> b[i] >> v[i];
		x -= b[i] - a[i];
		f[i] = mp( v[i], b[i] - a[i] );
	}
	sort( f, f + n );
	double ans = 0;
	double tt = min(x / r,t);
	ans += tt;
	t -= tt;
	x -= tt * r;
	if ( fabs(x) > eps )
		ans += x / s;
	for ( int i = 0; i < n; i ++ )
	{
		//f[i].first *= -1;
		double tt = min(f[i].second / (r + f[i].first),t);
		ans += tt;
		t -= tt;
		f[i].second -= tt * (r + f[i].first);
		if (fabs(f[i].second) > eps)
			ans += f[i].second / (f[i].first + s);
	}
	printf("%0.9lf\n",ans);
	return false;
}

int main()
{
	prepare( );
	int t;
	cin >> t;
	for ( int i = 0; i < t; i ++ )
	{
		printf("Case #%d: ",i+1);
		solve( );
	}
	return 0;
}