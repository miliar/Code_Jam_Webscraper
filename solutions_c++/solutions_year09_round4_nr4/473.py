#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <list>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i(a), _n(b); i<=_n; i++)
#define FR(i,b) FOR(i,0,b-1)
#define REP(i,a,b) for(int i(a), _n(b); i >= _n; i--)
#define _M(a) memset(a,0,sizeof(a))
#define IN scanf
#define OUT printf
#define sqr(q) ((q)*(q))
#define ll long long
#define ul unsigned ll
#define INF 1000000000

int KT;
int X[50];
int Y[50];
int Z[50];
int n;

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	IN("%d", &KT);
	
	FOR(test, 1, KT)
	{
		double ans;
		IN("%d", &n);
		FR(i,n) IN("%d%d%d", &X[i], &Y[i], &Z[i]);
		if (n == 1) ans = Z[0];
		else if (n == 2) ans = max(Z[0], Z[1]);
		else
		{
			double d1,d2,d3;
			d1 = sqrt((double)sqr(X[0] - X[1]) + sqr(Y[0] - Y[1])) + Z[0] + Z[1];
			d2 = sqrt((double)sqr(X[2] - X[1]) + sqr(Y[2] - Y[1])) + Z[2] + Z[1];
			d3 = sqrt((double)sqr(X[2] - X[0]) + sqr(Y[2] - Y[0])) + Z[2] + Z[0];
	//		OUT("%lf %lf %lf\n", d1,d2,d3);
			ans = INF;
			ans = min(max(d1,(double)Z[2]),ans);
			ans = min(max(d2,(double)Z[0]),ans);
			ans = min(max(d3,(double)Z[1]),ans);
			ans /=2;
		}
		
		OUT("Case #%d: %.7lf\n", test, ans);
		
	}
	

	return 0;
}
