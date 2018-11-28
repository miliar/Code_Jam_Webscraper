#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <memory.h>

using namespace std;
#define MAX 100
int R, C;
char matr[MAX][MAX];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++)
		{
			char s[100];
			scanf("%s", s);
			for (int j = 0; j < C; j++)
				matr[i][j] = s[j];
		}
		for (int i = 0; i < R-1; i++)
			for (int j = 0; j < C-1; j++)
			{
				if (matr[i][j] == '#' && matr[i][j+1] == '#' && matr[i+1][j] == '#' && matr[i+1][j+1] == '#')
				{
					matr[i][j] = '/';
					matr[i][j+1] = '\\';
					matr[i+1][j] = '\\';
					matr[i+1][j+1] = '/';
				}
			}
		bool f = true;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				if (matr[i][j] == '#')
					f = false;
		printf("Case #%d:\n", t+1);
		if (f)
		{
			for (int i = 0; i < R; i++)
			{
				matr[i][C] = 0;
				printf("%s\n", matr[i]);
			}
		}
		else
		{
			printf("Impossible\n");
		}
			
		
	}
	return 0;
}