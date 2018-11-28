
#include <iostream>
#include <cstdio>
long long n;
int t,pg,pd;
using namespace std;

int gcd(int a,int b)
{
	if(b==0)
		return a;
	else 
		return gcd(b,a%b);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	int cnt=0;
	while(t--)
	{
		scanf("%lld%d%d",&n,&pd,&pg);
		printf("Case #%d: ",++cnt);
		int a=gcd(pd,100);
		int b=gcd(pg,100);
		int aa=100/a;
		int bb=100/b;
		if(pg==100&&pd!=100||(pg==0&&pd!=0)||(pg==100&&pd==0)||(pg==0&&pd==100))
		{
			printf("Broken\n");
			continue;
		}
		if(pg==100&&pd==100||(pg==0&&pd==0))
		{
			printf("Possible\n"); 
			continue;
		}
		else if(aa<=n)
			printf("Possible\n");
		else 
			printf("Broken\n");
	}

	return 0;
}

/*
Case #1: Possible
Case #2: Broken
Case #3: Possible
*/
