//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
using namespace std;

int t,n,x,ans,maks;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d",&n);
		int d[n],l[n],dp[n];
		FORN(j,n)
		{
			dp[j] = 0;
			scanf("%d%d",&d[j],&l[j]);
		}
		scanf("%d",&x);
		printf("Case #%d:",i+1);
		ans = 0;
		FORN(j,n)
		{
			maks = 0;
			FORN(k,j)
				if (dp[k] >= d[j])
					maks = max(maks,d[j]+min(l[j],abs(d[j]-d[k])));
			if (j == 0)
				dp[j] = 2*d[j];
			else
				dp[j] = maks;
			ans = max(ans,dp[j]);
		}
		if (ans >= x)
			printf(" YES\n");
		else
			printf(" NO\n");
	}
}
