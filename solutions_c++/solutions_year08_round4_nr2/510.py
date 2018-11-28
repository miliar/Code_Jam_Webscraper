#include "stdio.h"
int main()
{
	int tot,kase,m,n,a,i,k,j,l,p,q;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d%d%d",&m,&n,&a);
		printf("Case #%d:",kase);
		for(i=0;i<=m;i++)
			for(k=0;k<=i;k++)
				for(j=i;j<=m;j++)
					for(l=0;l<=n;l++)
						for(p=0;p<=n;p++)
						{
							q=j*l-k*p-i*l+i*p;
							if(q==a)
							{
								printf(" %d %d %d %d %d %d\n",i,0,k,l,j,p);
								goto loop;
							}
						}
loop:
		if(i==m+1)
			printf(" IMPOSSIBLE\n");
	}
	return 0;
}