#include<cstdio>
int t,mt,n,p1,p2;
int gcd(int a,int b)
{
	if (!b) return a;
	return  gcd(b,a%b);
}
int main()
{
	freopen("A0.in","r",stdin);
	freopen("A0.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		scanf("%d%d%d",&n,&p1,&p2);
		int d1=gcd(p1,100);
		int d2=gcd(p2,100);
		int a1=100/d1;
		int a2=100/d2;
		p1/=d1;
		p2/=d2;
		printf("Case #%d: ",mt);
		if (a1<=n)
		{
			int t1=p2;
			int t2=a2;
			int find=0;
			while(p2<p1||(a2-p2<a1-p1))
			{
				p2+=t1;
				a2+=t2;
				if(a2>100)
				{
					find=1;
					break;
				}
			}
			if (find) printf("Broken\n");
			else printf("Possible\n");
		}
		else
		{
			printf("Broken\n");
		}
	}
}
