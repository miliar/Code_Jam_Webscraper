using namespace std;

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

#define EPS 1e-11 
#define inf ( 1LL << 31 ) - 1
#define LL double

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

const int MAX = 1005;
int tc[MAX][3];
LL memo[MAX][3];
LL D[MAX];
int a[MAX];
int L, T, n, c;
int kase;
LL solve(int pos, int boost)
{

	if (pos == 0) 
	{
		return 0;
	}
	LL &ret = memo[pos][boost];
	if (tc[pos][boost] == kase) return ret;
	tc[pos][boost] = kase;
	ret = 10000000000000000000000LL;
	LL x;

	if (boost > 0)
	{
		x = solve(pos-1, boost-1);
		if (x > T)
			ret = min(ret, D[pos] + x);
		else if (2*D[pos] + x > T)
		{
			double dt = T - x;
			ret = min(ret, dt + x + D[pos] - dt/2);
		}
	}
	x = solve(pos-1, boost);
	ret = min(ret, D[pos] * 2 + x);
	return ret;
}

int main()
{
	freopen("d:/input.txt", "r", stdin);
	freopen("d:/output.txt", "w", stdout);

    int t, n, l, h;
    scanf("%d", &t);
    xrep(ncase,1,t)
    {
	 kase = ncase;
     scanf("%d %d %d %d", &L, &T, &n, &c);
	 rep(i,c)
		scanf("%d", &a[i]);
	 rep(i,n) 
			D[i+1] = a[i%c]; 
	 printf("Case #%d: ",ncase);	 
     printf("%.0lf\n", solve(n, L));

	}
	 
}
