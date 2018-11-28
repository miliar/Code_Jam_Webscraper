#include <cstdio>
#include <cstdlib>
#define MAX 50
char map[MAX][MAX];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int nT,t=0;
	scanf("%d",&nT);
	while(nT--)
	{
		int row,col;
		scanf("%d%d",&row,&col);
		for(int i=0;i<row;++i)
		{
			for(int j=0;j<col;++j)
			{
				scanf(" %c",&map[i][j]);
			}	
		}
		bool ok=true;
		for(int i=0;i<row && ok;++i)
		{
			for(int j=0;j<col;++j)
			{
				if(map[i][j]=='#')
				{
					if(j!=col-1 && i!=row-1  &&
						map[i][j+1]=='#' &&
						map[i+1][j]=='#' && map[i+1][j+1]=='#')
					{
						map[i][j]=map[i+1][j+1]='/';
						map[i][j+1]=map[i+1][j]='\\';
					}	
					else
					{
						ok=false;
						break;
					}
				}
			}	
		}
		printf("Case #%d:\n",++t);
		if(!ok)
		{
			puts("Impossible");	
		}
		else
		{
			for(int i=0;i<row;++i)
			{
				for(int j=0;j<col;++j)
				{
					putc(map[i][j],stdout);	
				}
				putc('\n',stdout);
			}	
		}
	}
}
