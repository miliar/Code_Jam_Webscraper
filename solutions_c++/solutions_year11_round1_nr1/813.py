#include "stdio.h"
#include "string.h"
#include "math.h"
#include <algorithm>
using namespace std;
#define M 10003

long long n,p,g;

int gcd(int a,int b)
{
	if(!b) return a;
	return gcd(b,a%b);
}

int main()
{
	int i,j,k,t,tc=1;
	int xp,xg;
	freopen("gcj/2011.5.21/A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lld%lld%lld",&n,&p,&g);
		if(n>100) n=100;
		xp=gcd(p,100);
		printf("Case #%d: ",tc++);
		if(g==100&&p<100)
		{
			printf("Broken\n");
			continue;
		}
		if(g==0&&p>0)
		{
			printf("Broken\n");
			continue;
		}
		if(n<100/xp)
		{
			printf("Broken\n");
			continue;
		}
		//i=n/(100/xp);
		//p/=xp;
		//g/=gcd(100,g);
		for(k=1;k<=n;k++)
		{
			if(k*p%100)
				continue;
			/*if((k*p)%g==0)
			{
				if(k*p/g>=k)
					break;
			}*/
			break;
		}
		if(k<=n)
			printf("Possible\n");
		else
			printf("Broken\n");
	}
	return 0;
}
/*
3
1 100 50
10 10 100
9 80 56
*/

