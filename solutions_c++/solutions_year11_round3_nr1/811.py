#include <stdio.h>
#include <string.h>

#define maxn 55

char map[maxn][maxn];

bool solve()
{
	int n,m;
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;++i)
		scanf("%s",map[i]);
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)
			if(map[i][j] == '#')
			{
				if(i+1 == n || j+1 == m) return false;
				if(map[i+1][j] != '#' || map[i][j+1] != '#' 
						|| map[i+1][j+1] != '#')
					return false;
				map[i][j] = map[i+1][j+1] = '/';
				map[i][j+1] = map[i+1][j] = '\\';
			}
	for(int i=0;i<n;++i)
		puts(map[i]);
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d:\n",i+1);
		if(!solve())
			puts("Impossible");
	}
	return 0;
}

