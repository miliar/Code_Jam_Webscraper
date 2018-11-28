#include<cstdio>
#include<cstring>
int t,k,i,j,n,l,a[1000001];
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		for(i=1,j=0;i<=n;i++)
		{
			for(j++,l=i;l;j++)
			{
				if(j>n) j=1;
				if(!a[j]) l--;
			}
			j--;
			a[j]=i;
		}
		scanf("%d",&n);
		printf("Case #%d:",k);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&j);
			printf(" %d",a[j]);
		}
		printf("\n");
	}
	fclose(stdout);
	return 0;
}
