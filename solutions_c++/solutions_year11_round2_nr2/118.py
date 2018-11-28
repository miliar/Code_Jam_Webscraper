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
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int n;
double L[205];
double R[205];
double x[205];
int v[205];
double d;

bool good( double t )
{
	for ( int i = 0; i < n; i ++ )
	{
		L[i] = x[i] - t;
		R[i] = x[i] + t;
	}
	double pos = L[0];
	for ( int i = 0; i < n; i ++ )
	{
		pos = max(pos,L[i]);
		if ( pos > R[i] )
			return false;
		pos += d * v[i];
		if ( pos - d > R[i] )
			return false;
	}
	return true;
}

bool solve( )
{
	cin >> n >> d;
	for ( int i = 0; i < n; i ++ )
	{
		cin >> x[i] >> v[i];
	}
	double l = 0;
	double r = 10000000000000.0;
	double m,om;
	while (fabs(r-l)>1e-12)
	{
		m = (l + r) / 2.0;
		if (fabs(m-om)<1e-9)
			break;
		if (good(m))
			r = m;
		else
			l = m;
		om = m;
	}
	printf("%.9lf\n",l);
	return false;
}

int main()
{
	prepare( );
	int t;
	cin >> t;
	for ( int i = 0; i < t; i ++ )
	{
		cerr << i << endl;
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}