#include<stdio.h>
#include<string.h>

int b;
int a[8];
bool use[8][10];
int res;

void dfs(int x,int y)
{
	int i,j,k,r;
	int bb,yy;
	if (y==0) res++;
	if (x<y) k=x;
	else k=y;
	for (i=k;i>=1;i--)
	{
		j=i;
		bb=1;
		yy=y;
		for (k=0;j>0;k++)
		{
			if (!use[k][j%b]) break;
			use[k][j%b]=false;
			yy=yy-(j%b)*bb;
			j=j/b;
			bb=bb*b;
		}
		if (j==0) dfs(i-1,yy);
		j=i;
		for (r=0;r<k;r++)
		{
			use[r][j%b]=true;
			j=j/b;
		}
	}
}

int main()
{
	int tt,pp;
	int n;
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	scanf("%d",&tt);
	for (pp=1;pp<=tt;pp++)
	{
		scanf("%d%d",&n,&b);
		memset(use,true,sizeof(use));
		res=0;
		dfs(n,n);
		printf("Case #%d: %d\n",pp,res);
	}
	return 0;
}