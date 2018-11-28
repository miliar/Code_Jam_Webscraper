#include <cstdio>
#include <cstdlib>
int main()
{
	int t,r,c,ti,i,j,cov;
	char geo[111][111];
	freopen("d:\\gcj\\r1c\\A-small-attempt0(1).in","r",stdin);
	freopen("d:\\gcj\\r1c\\alout.txt","w",stdout);
	scanf("%d",&t);
	for (ti=0;ti<t;ti++)
	{
		scanf("%d%d",&r,&c);
		for (i=0;i<r;i++)
			scanf("%s",geo[i]);
		for (i=0;i<r;i++)
		{
			for (j=0;j<c;j++)
			{
				if (geo[i][j]=='#')
				{
					if (i+1<r && j+1<c && geo[i+1][j]=='#' && geo[i][j+1]=='#' && geo[i+1][j+1]=='#')
					{
						geo[i][j]='/';
						geo[i][j+1]='\\';
						geo[i+1][j+1]='/';
						geo[i+1][j]='\\';
					}
				}
			}
		}
		cov=1;
		for (i=0;i<r;i++)
		{
			for (j=0;j<c;j++)
				if (geo[i][j]=='#')
				{
					cov=0;
					break;
				}
			if (cov==0) break;
		}
		printf("Case #%d:\n",ti+1);
		if (cov==0) printf("Impossible\n");
		else
		{
			for (i=0;i<r;i++)
				printf("%s\n",geo[i]);
		}
	}


	return 0;
}

