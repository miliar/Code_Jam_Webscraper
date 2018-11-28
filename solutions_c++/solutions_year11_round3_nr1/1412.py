#include <stdio.h>
#define maxx 110

char map[maxx][maxx];
int n,m;

bool judge(int x,int y)
{
	if(x == n-1 || y == m-1) return false;
	if(map[x][y+1] != '#' || map[x+1][y+1] != '#' || map[x][y] != '#') return false;
	return true;
}

bool solve()
{
	int i,j;
	scanf("%d%d",&n,&m);
	gets(map[0]);
	for(i=0;i<n;i++) gets(map[i]);

	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(map[i][j] == '#')
			{
				if(judge(i,j))
				{
					map[i][j] ='/';
					map[i][j+1] = '\\';
					map[i+1][j] ='\\';
					map[i+1][j+1] ='/';
				}
				else
				{
					return false;
				}
			}
		}
	}
	return true;
}

int main ()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T,cas,i;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		printf("Case #%d:\n",cas);
		if(solve())
		{
			for(i=0;i<n;i++) printf("%s\n",map[i]);
		}
		else
		{
			printf("Impossible\n");
		}
	}


}