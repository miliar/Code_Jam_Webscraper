#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

int t,r,c;
char map[60][60];
int i,j;

bool test()
{
	int i,j;
	for (i=0;i<r;i++)
		for (j=0;j<c;j++)
			if (map[i][j]=='#')
		{
			if (map[i][j+1]=='#' && map[i+1][j]=='#' && map[i+1][j+1]=='#')
			{
				map[i][j]='/';
				map[i+1][j+1]='/';
				map[i][j+1]='\\';
				map[i+1][j]='\\';
			}
			else return true;
		}
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		memset(map,0,sizeof(map));
		scanf("%d%d",&r,&c);
		for (i=0;i<r;i++)scanf("%s",map[i]);
		
		printf("Case #%d:\n",id);
		if (test())printf("Impossible\n");
		else for (i=0;i<r;i++)printf("%s\n",map[i]);

	}
	return 0;
}