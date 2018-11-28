#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define MAX 64

char mat[MAX][MAX];

int main()
{
	int cas, casos;
	int n, m;
	int i, j, imp;
	
	scanf("%d", &casos);
	
	for (cas = 1; cas <= casos; cas++)
	{
		printf("Case #%d:\n", cas);
		
		scanf("%d %d", &n, &m);
		
		for (i=0; i<n; i++)
		{
			scanf("%s", mat[i]);
		}
		
		imp = 0;
		for (i=0; i<n && !imp; i++)
		{
			for (j=0; j<m && !imp; j++)
			{
				if (mat[i][j] == '#')
				{
					if (j == m-1 || i == n-1)
					{
						imp = 1;
						break;
					}
					if (mat[i+1][j] != '#' || mat[i][j+1] != '#' || mat[i+1][j+1] != '#')
					{
						imp = 1;
						break;
					}
					mat[i][j] = '/';
					mat[i+1][j] = '\\';
					mat[i][j+1] = '\\';
					mat[i+1][j+1] = '/';
				}
			}
		}
		if (imp)
		{
			printf("Impossible\n");
		}
		else
		{
			for (i=0; i<n; i++)
			{
				printf("%s\n", mat[i]);
			}
		}
	}
	
	return 0;
}
