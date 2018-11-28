#include <stdio.h>

char s[1000][1000];
int y[1000];

int main()
{
	int ni=1,n,i,j,k,l,r;
	scanf("%d",&n);
	while (scanf("%d",&n)==1)
	{
		for (i=0;i<n;++i) scanf("%s",s[i]);
		r=0;
		for (i=0;i<n;++i)
		{
			k=0;
			for (j=0;j<n;++j) if (s[i][j]=='1') k=j+1;
			y[i]=k;
		}
		while (1)
		{
			for (i=0;i<n;++i) if (y[i]>i+1)
			{
				for (j=i+1;j<n;++j) if (y[j]<=i+1) break;
				k=y[j];
				for (l=j-1;l>=i;--l) y[l+1]=y[l];
				y[i]=k;
				r+=j-i;
				break;
			}
			if (i==n) break;
		}
		printf("Case #%d: %d\n",ni++,r);
	}
	return 0;
}