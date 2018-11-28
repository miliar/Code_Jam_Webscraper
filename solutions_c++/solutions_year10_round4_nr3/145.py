#include<stdio.h>

bool use[2][101][101];

int main()
{
	int tt,pp;
	int n,i,j,k;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&tt);
	for (pp=1;pp<=tt;pp++)
	{
		scanf("%d",&n);
		for (i=1;i<=100;i++)
			for (j=1;j<=100;j++)
				use[0][i][j]=false;
		for (k=1;k<=n;k++)
		{
			int x1,x2,y1,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (i=x1;i<=x2;i++)
				for (j=y1;j<=y2;j++)
					use[0][i][j]=true;
		}
		int p=0;
		int q=1;
		k=0;
		bool flag=true;
		while (flag)
		{
			flag=false;
			for (i=1;i<=100;i++)
				for (j=1;j<=100;j++)
					use[q][i][j]=false;
			for (i=1;i<=100;i++)
				for (j=1;j<=100;j++)
					if (use[p][i][j])
					{
						flag=true;
						if (i>1&&use[p][i-1][j]) use[q][i][j]=true;
						if (j>1&&use[p][i][j-1]) use[q][i][j]=true;
					}
					else
					{
						if (i>1&&use[p][i-1][j]&&j>1&&use[p][i][j-1]) use[q][i][j]=true;
					}
			p=1-p;
			q=1-q;
			k++;
		}
		printf("Case #%d: %d\n",pp,k-1);
	}
	return 0;
}
