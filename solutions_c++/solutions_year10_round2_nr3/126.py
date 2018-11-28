const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef __int64 ll;

ll ii, nn;
ll n;
ll a[1000][1000];
ll c[1000][1000];

ll C(ll i, ll j)
{
	if (i>j)
		return c[i][j]=0;
	if (i==1)
		return c[i][j]=j;
	if (i==0)
		return c[i][j]=1;

	if (c[i][j] == -1)
		c[i][j] = (C(i-1, j-1) + C(i, j-1)) % 100003;
	
	return c[i][j];
}

ll A(ll i, ll j)
{
	if (i == j+1)
		return a[i][j]=1;
	if (i < j+1)
		return a[i][j]=0;

	if (a[i][j] == -1)
	{
		ll res = 0;

		for (int j1=0; j1<j; ++j1)
		{
			res += A(j,j1) * C(j-j1-1,i-j-1);
			res %= 100003;
		}

		a[i][j] = res;
	}
	return a[i][j];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	memset(a, -1, sizeof a);
	memset(c, -1, sizeof c);

	scanf("%I64d", &nn);
	for (ii=0; ii<nn; ++ii)
	{
		scanf("%I64d", &n);
		ll res = 0;
		for (ll i=1; i<=n; ++i)
		{
			res += A(n, i);
			res %= 100003;
		}

		printf("Case #%I64d: %I64d\n", ii+1, res);
	}
	return 0;
}
