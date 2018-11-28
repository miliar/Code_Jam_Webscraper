#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <assert.h>
#include <stack>
#include <sstream>
#include <list>
#include <math.h>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <map>
using namespace std;

#define ll long long
#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))

const double eps = 1e-7;

#define fr(x,a,b) for( int x=a; x < b; ++x )
#define frr(x,a,b) for( int x=a;x>=b;--x)

#define pf printf
#define sf scanf

#define pb push_back
#define mp make_pair

const ll mod = 1000000007;

struct ft
{
	int d;
	int l;
}a[20000];

int dp[20000];

int main()
{
	int T;
	scanf("%d",&T);
	fr(c,0,T)
	{
		int n;
		int dest;
		scanf("%d",&n);
		fr(i,0,n) scanf("%d%d",&a[i].d,&a[i].l);
		scanf("%d",&dest);

		memset(dp,0,sizeof(dp));

		dp[0]=a[0].d;

		fr(i,0,n)
		{
			dp[i]=min(dp[i], a[i].l);
			fr(j,i+1,n)
			{
				if(a[j].d-a[i].d > dp[i])
					break;
				dp[j] = max( a[j].d-a[i].d, dp[j] );
			}
		}

		int ok=0;
		fr(i,0,n)
		{
			if(a[i].d+dp[i]>=dest)
			{
				ok=1;
				break;
			}
		}

		if(ok)
			printf("Case #%d: YES\n",c+1);
		else
			printf("Case #%d: NO\n",c+1);
	}
	return 0;
}

