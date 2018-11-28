#include<cstdio>
#include<stdlib.h>
#include<memory.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int a[1002][2];
	int T,i,j,k,l,m,n;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		int count=0;
		scanf("%d",&n);
		for (i=0;i<n;i++) scanf("%d%d",&a[i][0],&a[i][1]);
		for (i=0;i<n-1;i++)
			for (j=i+1;j<n;j++)
			{
				if ((a[i][0]>a[j][0] && a[i][1]<a[j][1]) || (a[i][0]<a[j][0] && a[i][1]>a[j][1]))
					count++;
			}
		printf("Case #%d: %d\n",cas,count);
	}
}
