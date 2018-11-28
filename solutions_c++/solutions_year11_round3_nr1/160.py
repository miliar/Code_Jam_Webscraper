#include <iostream>
using namespace std;

char g[110][110];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("2.out","w",stdout);
	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		int i,j,r,c;
		scanf("%d%d",&r,&c);
		memset(g,0,sizeof(g));
		for(i=0;i<r;++i)
		{
			scanf("%s",g[i]);
		}
		bool ok=true;
		for(i=0;i<r;++i)
		{
			for(j=0;j<c;++j)
			{
				if(g[i][j]=='#')
				{
					if(g[i][j+1]!='#'||g[i+1][j]!='#'||g[i+1][j+1]!='#')
					{
						ok=false;
						break;
					}
					else
					{
						g[i][j]=g[i+1][j+1]='/';
						g[i+1][j]=g[i][j+1]='\\';
					}
				}
			}
			if(!ok) break; 
		}
		printf("Case #%d:\n",cas);
		if(!ok) printf("Impossible\n");
		else 
		{
			for(i=0;i<r;++i)
				printf("%s\n",g[i]);
		}
	}

	return 0;
}