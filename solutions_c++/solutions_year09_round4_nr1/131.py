#include <cstdio>
#include <cstring>
int a[50];
bool vi[50];
int n,i,j,k,T;
char st[50];
int b[50];
main()
{
	int I=0;
	scanf("%d",&T);
	while (T--)
	{
		int ans=0;
		scanf("%d",&n);
		for (i=0;i<n;++i)
		{
			scanf("%s",st);
			k=0;
			for (j=0;j<n;++j)
				if (st[j]=='1') k=j;
			a[i]=k;
			//printf("%d %d\n",i,a[i]);
		}
		memset(vi,0,sizeof vi);
		for (i=0;i<n;++i)
		{
			for (j=0;j<n;++j)
				if (a[i]<=j && !vi[j])
				{
					vi[j]=1;
					b[i]=j;
					//printf("%d %d\n",i,j);
					//if (j>i) ans+=j-i;
					break;
				}
		}
		for (i=0;i<n;++i)
			for (j=i+1;j<n;++j)
				if (b[i]>b[j]) ++ans;
		printf("Case #%d: %d\n",++I,ans);
	}
	return 0;
}
