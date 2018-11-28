#include <stdio.h>
#include <string.h>

int a[200][200];
int T,i,j,n,k,mi1,mi2,d1,d2,ok,t;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		memset(a,-1,sizeof(a));
		scanf("%d",&n);
		for(i=0;i<n;i++)
			for(j=n-1-i,k=0;k<=i;j+=2,k++)
				scanf("%d",&a[i][j]);
		for(i=n;i<2*n-1;i++)
			for(j=i-n+1,k=0;k<=2*n-2-i;j+=2,k++)
				scanf("%d",&a[i][j]);
		for(mi1=0;mi1<n;mi1++)
		{
			d1=n-1-mi1;
			ok=0;
			for(i=0;i<d1 && !ok;i++)
				for(j=0;j<2*n-1 && !ok;j++)
					if(a[i][j]>=0 && a[i][j]!=a[d1+d1-i][j])
					{
						ok=1;
						break;
					}
			if(!ok)
				break;
			d1=n-1+mi1;
			ok=0;
			for(i=2*n-2;i>d1 && !ok;i--)
				for(j=0;j<2*n-1 && !ok;j++)
					if(a[i][j]>=0 && a[i][j]!=a[d1+d1-i][j])
					{
						ok=1;
						break;
					}
			if(!ok)
				break;
		}
		for(mi2=0;mi2<n;mi2++)
		{
			d2=n-1-mi2;
			ok=0;
			for(j=0;j<d2 && !ok;j++)
				for(i=0;i<2*n-1 && !ok;i++)
					if(a[i][j]>=0 && a[i][j]!=a[i][d2+d2-j])
					{
						ok=1;
						break;
					}
			if(!ok)
				break;
			d2=n-1+mi2;
			ok=0;
			for(j=2*n-2;j>d2 && !ok;j--)
				for(i=0;i<2*n-1 && !ok;i++)
					if(a[i][j]>=0 && a[i][j]!=a[i][d2+d2-j])
					{
						ok=1;
						break;
					}
			if(!ok)
				break;
		}
		printf("Case #%d: %d\n",t,(mi1+mi2)*(mi1+mi2+n+n));
	}
	return 0;
}