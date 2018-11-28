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
#ifdef WIN32
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int n;
int a[1004];

bool solve( )
{
	cin >> n;
	for ( int i = 0; i < n; i ++ )
		cin >> a[i];
	sort(a,a+n);
	int sum = 0;
	for ( int i = 1; i < n; i ++ )
		sum += a[i];
	int x = 0;
	for ( int i = 0; i < n; i ++ )
		x ^= a[i];
	if ( x )
		printf("NO\n");
	else
		printf("%d\n",sum);
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
		solve();
	}
	return 0;
}