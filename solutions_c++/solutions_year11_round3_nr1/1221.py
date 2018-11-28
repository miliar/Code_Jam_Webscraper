#include <iostream>
#include <cstdio>
#include <memory.h>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;
char map[100][100];
int main()
{
	int i,j,k,m,n,t,cas = 1,num;
	bool find;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		printf("Case #%d:\n",cas++);
		scanf("%d %d",&n,&m);
		getchar();
		num = 0;
		for (i = 0;i < n;i++)
		{
			gets(map[i]);
			for (j = 0;j < m;j++)
			{
				if (map[i][j] == '#')
					num++;
			}
		}
		if (num % 4)
			printf("Impossible\n");
		else
		{
			find = true;
			for (i = 0;i < n - 1;i++)
			{
				for (j = 0;j < m - 1;j++)
				{
					if (map[i][j] == '#')
					{
						if (map[i][j + 1] == '#' && map[i + 1][j] == '#' && map[i + 1][j + 1] == '#')
						{
							map[i][j] = '\/';
							map[i][j + 1] = '\\';
							map[i + 1][j] = '\\';
							map[i + 1][j + 1] = '\/';
						}
						else
						{
							find = false;
							goto done;
						}
					}
				}
			}
			for (i = 0;i < n;i++)
			{
				if (map[i][m - 1] == '#')
					find = false;
			}
			for (i = 0;i < m;i++)
			{
				if (map[n - 1][i] == '#')
					find = false;
			}
done:
			if (!find)
				printf("Impossible\n");
			else
			{
				for (i = 0;i < n;i++)
					printf("%s\n",map[i]);
			}
		}
	}
	return 0;
}