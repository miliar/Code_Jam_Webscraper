#include<stdio.h>
#include<string>
#include<queue>
#include<cstring>
#include<assert.h>
#include<iostream>
#include<map>
#include<algorithm>
#define sf scanf
#define pf printf
#define clr(key) memset(key,0,sizeof(key))
using namespace std;
#define ll long long

int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}
int main()
{
	//freopen("a.in","r",stdin);
	int T;
	scanf("%d",&T);
	int ca=0;
	while(T--)
	{
		ll n;
		int pd,pg;
		scanf("%lld%d%d",&n,&pd,&pg);
		
		int dd = 100-pd;
		int gg = 100-pg;
		printf("Case #%d: ",++ca);

		if( gg == 100 & dd != 100 || gg == 0 && dd != 0 )
		{
			printf("Broken\n");
			continue;
		}
		else
		{
			int flag = 0;
			for(ll i=1;i<=min((ll)100,n);++i)
			{
				if( ( pd * i ) % 100 == 0 )//&& ( pg * i ) % 100 == 0 )
				{
					flag = 1;
					break;
				}
			}
			if( flag )
				printf("Possible\n");
			else
				printf("Broken\n");
		}
		//printf(" dd = %d gg = %d\n",dd,gg);
	}
}

