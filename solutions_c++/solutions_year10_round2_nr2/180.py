#include <stdio.h>

int x[100];
int v[100];

int main()
{
	int n,k,b,t,i,j,p,ii=0;
	scanf("%d",&n);
	while (scanf("%d %d %d %d",&n,&k,&b,&t)==4)
	{
		for (i=0;i<n;++i) scanf("%d",x+i);
		for (i=0;i<n;++i) scanf("%d",v+i);
		j=0;p=0;
		for (i=n-1;i>=0 && k>0;--i)
		{
			if (x[i]+t*v[i]<b) ++p; else { j+=p; --k; }
		}
		if (k==0) printf("Case #%d: %d\n",++ii,j); else printf("Case #%d: IMPOSSIBLE\n",++ii); 
	}
	return 0;
}
