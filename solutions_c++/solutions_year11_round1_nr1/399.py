#include <cstdio>

typedef long long s64;

inline s64 gcd(s64 a,s64 b)
{
	s64 t;
	do
	{
		t=a%b;
		a=b;
		b=t;
	}while(b!=0);
	return a;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		s64 N,Pd,Pg;
		scanf("%lld%lld%lld",&N,&Pd,&Pg);
		s64 d=gcd(Pd,100);
		if (N<100/d)
			printf("Broken\n");
		else if ((Pg==0 && Pd!=0) || (Pg==100 && Pd!=100))
			printf("Broken\n");
		else printf("Possible\n");
	}
	return 0;
}
