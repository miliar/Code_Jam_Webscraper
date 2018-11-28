
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

char map[200][200];

bool judge(int x,int y)
{
	if(map[x][y+1]=='#' && map[x+1][y]=='#' && map[x+1][y+1]=='#')
		return true;
	return false;
}

int main()
{
	int t;
	int n,m,i,j;
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	int d = 1;
	while(t--)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%s",map[i]);
		for(i=0;i<n;i++) {
			for(j=0;j<m;j++)
			{
				if(map[i][j] == '#')
				{
					if(!judge(i,j)) break;
					map[i][j] = '/';
					map[i][j+1] = '\\';
					map[i+1][j] = '\\';
					map[i+1][j+1] = '/';
					j++;
				}
			}
			if(j!=m) break;
		}
		printf("Case #%d:\n",d++);
		if(i != n) printf("Impossible\n");
		else
		{
			for(i=0;i<n;i++)
				printf("%s\n",map[i]);
		}
	}
	return 0;
}