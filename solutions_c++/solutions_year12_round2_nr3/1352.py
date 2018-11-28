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

int t,n,ans,z,sip,dp[2000050];
bool benar;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d",&n);
		int bil[n];
		FORN(j,n)
			scanf("%d",&bil[j]);
		printf("Case #%d:\n",i+1);
		RES(dp,0);
		dp[0] = 1;
		ans = 0;
		benar = false;
		FORN(j,n)
			if (!ans)
				FORD(k,2000000,bil[j])
					if (dp[k-bil[j]])
					{
						if (!dp[k])
							dp[k] = bil[j];
						else
						{
							benar = true;
							ans = k;
							sip = bil[j];
							z = k;
							while (z-dp[z] > 0)
							{
								printf("%d ",dp[z]);
								z -= dp[z];
							}
							printf("%d\n",dp[z]);
							break;
						}
					}
		if (!benar)
		{
			printf("Impossible\n");
			continue;
		}
		if (ans-sip == 0)
		{
			printf("%d\n",sip);
			continue;
		}
		else
			printf("%d ",sip);
		z = ans-sip;
		while (z-dp[z] != 0)
		{
			printf("%d ",dp[z]);
			z -= dp[z];
		}
		printf("%d\n",dp[z]);
	}
}
