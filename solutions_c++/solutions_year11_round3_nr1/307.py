#include<stdio.h>

char g[51][51];

int main()
{
	freopen("gcja.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int Cas=1;Cas<=T;Cas++)
	{
		int R,C;
		scanf("%d%d",&R,&C);
		for (int i=0;i<R;i++)
			scanf("%s",&g[i]);
		int imin=0;
		int jmin=0;
		bool ok=true;
		while (ok)
		{			
			bool find=false;
			for (int i=imin;i<R;i++)
			{
				for (int j=jmin;j<C;j++)
					if (g[i][j]=='#')
					{
						find=true;
						g[i][j]='/';
						if (j<C-1&&g[i][j+1]=='#')
							g[i][j+1]='\\';
						else
							ok=false;
						if (i<R-1&&g[i+1][j]=='#')
							g[i+1][j]='\\';
						else
							ok=false;
						if (i<R-1&&j<C-1&&g[i+1][j+1]=='#')
							g[i+1][j+1]='/';
						else
							ok=false;
						if (!ok||find) break;
					}
				if (!ok||find) break;
			}
			if (!find) break;
		}		
		printf("Case #%d:\n",Cas);
		if (ok)
		{
			for (int i=0;i<R;i++)
				printf("%s\n",g[i]);
		}
		else
		{
			printf("Impossible\n");
		}
	}
}