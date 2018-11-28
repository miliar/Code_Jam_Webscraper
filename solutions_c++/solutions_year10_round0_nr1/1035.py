#include<stdio.h>

int f[31];

int main()
{
	int t,p;
	int n,k;
	int i,j;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d%d",&n,&k);
		f[1]=1;
		for (i=2;i<=n;i++)
			f[i]=f[i-1]*2+1;
		if (k%(f[n]+1)==f[n]) printf("Case #%d: ON\n",p);
		else printf("Case #%d: OFF\n",p);
	}
	return 0;
}
