#include<cstdio>
int n,mt,t,a,p,s,q;
int main()
{
	freopen("C1.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		scanf("%d",&n);
		p=s=0;q=1<<30;
		for(;n--;)
		{
			scanf("%d",&a);
			p^=a;
			s+=a;
			if (q>a) q=a;
		}
		if (p) printf("Case #%d: NO\n",mt);
		else printf("Case #%d: %d\n",mt,s-q);
	}
}
