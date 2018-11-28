

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <iostream>
using namespace std;
map <int  , char> M;
int Map[101][101];
int root[200001];
int b[101][101];
int dir[][2] = {-1, 0, 0 , -1, 0 , 1, 1, 0};
int find(int a)
{
	if (a != root[a])
		root[a] = find(root[a]);
	return root[a];
}
void merge(int a,int b)
{
	a = find(a);
	b = find(b);
	root[a] = b;
}
int main()
{
	int i , j , k , d , n , m , t , minx , tmp , cnt;
	char ch;
	//	freopen("E:\\B-small-attempt1.in" , "r"  ,stdin);
	//freopen("E:\\B-small-attempt1.out" , "w"  , stdout);
	scanf("%d" , &t);
	for (k = 1; k <= t;k ++)
	{
		scanf("%d %d" , &n , &m);
		cnt = 1;
		for (i = 1;i <= n;i ++)
			for (j = 1;j <= m;j ++)
			{
				scanf("%d" , &Map[i][j]);
				b[i][j] = cnt;
				root[cnt] = cnt;
				cnt ++;
			}
		for (i = 1;i <= n;i ++)
		{
			for (j = 1;j <= m;j ++)
			{
				minx = Map[i][j];
				for (d = 0;d < 4;d ++)
				{
					int x = i + dir[d][0];
					int y = j + dir[d][1];
					if (x < 1 || y < 1 || x > n || y > m) continue;
					if (Map[x][y] < minx)
					{
						tmp = b[x][y];
						minx = Map[x][y];
					}
				}
				if (minx == Map[i][j]) continue;
				merge(b[i][j] , tmp);
			}
		}

		for (i = 1;i <= n;i ++)
			for (j = 1;j <= m;j ++)
				b[i][j] = find(b[i][j]);

		M.clear();
		ch = 'a';
		printf("Case #%d:\n" , k);
		for (i = 1;i <= n;i ++)
		{
			for (j = 1;j <= m;j ++)
			{
				if (M[b[i][j]] == 0)
				{
					M[b[i][j]] = ch;
					ch = ch + 1;
				}
				printf("%c" , M[b[i][j]]);
				if (j != m) printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}