#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

using namespace std;

const int MAX = 100;

int main()
{
	int n, m, i, j, k, t;
	char place[MAX][MAX], c;
	bool ans;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for(k = 0; k < t; k++)
	{
		printf("Case #%d:\n", k + 1);
		ans = true;
		scanf("%d %d", &n, &m);
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
			{
				scanf("%c", &c);
				if(c == '\n')
					scanf("%c", &c);
				place[i][j] = c;
			}
		for(i = 0; i < n - 1; i++)
			for(j = 0; j < m; j++)
				if(place[i][j] == '#')
					if((place[i][j + 1] != '#') || (place[i + 1][j] != '#') || (place[i + 1][j + 1] != '#'))
						ans = false;
					else
					{
						place[i][j] = '/';
						place[i + 1][j + 1] = '/';
						place[i + 1][j] = '\\';
						place[i][j + 1] = '\\';
					}
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
				if(place[i][j] == '#')
					ans = false;
		if(!ans)
			printf("Impossible\n");
		else
		{
			for(i = 0; i < n; i++)
			{
				for(j = 0; j < m; j++)
					printf("%c", place[i][j]);
				printf("\n");
			}
		}
	}
    return 0;
}
