#include <iostream>
using namespace std;
long long gcd(long long a,long long b)
{
	if(b==0)return a;
	else return gcd(b,a%b);
}
int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	int cnt=0;
	long long temp;
	scanf("%d",&T);
	long long n;
	int pd,pg;
	while(T--)
	{
		cnt++;
		scanf("%lld%d%d",&n,&pd,&pg);
		printf("Case #%d: ",cnt);
		if(pg==0)
		{
			if(pd==0)
			printf("Possible\n");
			else printf("Broken\n");
			continue;
		}
		if(pg==100)
		{
			if(pd==100)
			{
				printf("Possible\n");
			}
			else printf("Broken\n");
			continue;
		}
		temp=gcd(pd,100);
		temp=100/temp;
	//	printf("-----------%d-----------\n",temp);
		if(temp<=n)printf("Possible\n");
		else printf("Broken\n");
	}
}