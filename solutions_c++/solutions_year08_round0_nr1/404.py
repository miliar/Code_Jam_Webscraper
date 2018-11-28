#include <cstdio>
#include <cstring>
#define smax 100
#define qmax 1001

int ans[qmax][smax];
char name[smax][200];
char tmp[200];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,s,q,i,j,k,l;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&s);
		gets(tmp);
		for(i=0;i<s;i++) gets(name[i]);

		for(i=1;i<qmax;i++)
			for(j=0;j<s;j++) ans[i][j]=1000000;
		for(i=0;i<s;i++) ans[0][i]=0;

		scanf("%d",&q);
		gets(tmp);
		for(i=1;i<=q;i++)
		{
			gets(tmp);
			for(k=0;k<s;k++)
				if (!strcmp(name[k],tmp)) break;
			for(j=0;j<s;j++)
				for(l=0;l<s;l++)
				{
					if (l==k) continue;
					if (ans[i][l]>ans[i-1][j]+(l==j?0:1))
						ans[i][l]=ans[i-1][j]+(l==j?0:1);
				}
		}
		k=10000;
		for(i=0;i<s;i++)
			if (ans[q][i]<k) k=ans[q][i];
		printf("Case #%d: %d\n",t,k);
	}
	return 0;
}