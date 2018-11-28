#include <cstdio>
using namespace std;
int test,Pd,Pg;
long long n;

int Gcd(int a,int b)
{
	if (!b) return a; else return Gcd(b,a%b);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		printf("Case #%d: ",kase);
		scanf("%I64d%d%d",&n,&Pd,&Pg);
		if (Pg==100)
		{
			if (Pd!=100) printf("Broken\n");
				else printf("Possible\n");
		}	else
		if (Pd==0) printf("Possible\n"); else
		if (Pg==0) printf("Broken\n"); else
		{
			if (n<100/Gcd(Pd,100)) printf("Broken\n"); else printf("Possible\n");
		}
	}
	
	return 0;
}
