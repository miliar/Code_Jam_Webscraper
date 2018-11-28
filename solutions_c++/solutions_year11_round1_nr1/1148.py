#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int T,pd,pg;
long long n;

long long gcd(long long a,long long b)
{
	if(!b)
		return a;
	return gcd(b,a%b);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		scanf("%I64d%d%d",&n,&pd,&pg);
		if(pg==100&&pd!=100||pg==0&&pd!=0)
			puts("Broken");
		else
		{
			long long t=100/gcd(pd,100);
			if(n>=t)
				puts("Possible");
			else
				puts("Broken");
		}
	}
	return 0;
}

