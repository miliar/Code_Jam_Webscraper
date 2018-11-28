#include <stdio.h>

int main()
{
	long long pd,pg,n,i,j,p,ca=0,vd,vt;
	scanf("%lld",&n);
	while (scanf("%lld %lld %lld",&n,&pd,&pg)==3)
	{
		p=0;
		for (i=1;i<=n && i<=100;++i) for (j=i;j<=100*i;++j)
		{
			if (((pd*i)%100)==0 && ((pg*j)%100)==0)
			{
				vt=((pg*j)/100);
				vd=((pd*i)/100);
				if (vd<=vt && (i-vd)<=(j-vt)) 
				{
					p=1;
				}
			}
		}
		if (p==1) printf("Case #%lld: Possible\n",++ca); else printf("Case #%lld: Broken\n",++ca);
	}
	return 0;
}
