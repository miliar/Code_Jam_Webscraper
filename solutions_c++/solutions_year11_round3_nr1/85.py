#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
char pic[102][102];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ALarge.txt","w",stdout);
	int T, tcnt = 0;
	int r, c;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d%d",&r,&c);
		for(int i = 0; i < r; i++)
			scanf("%s", pic[i]);
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
			{
				if(pic[i][j] == '#')
				{
					if(i + 1 >= r || pic[i + 1][j] != '#' 
						|| j + 1 >= c || pic[i][j + 1] != '#'
						|| pic[i + 1][j + 1] != '#')
							goto imp;
					pic[i][j] = '/';
					pic[i + 1][j] = '\\';
					pic[i][j + 1] = '\\';
					pic[i + 1][j + 1] = '/';
				}
			}
		}
		printf("Case #%d:\n", ++tcnt);
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
				printf("%c",pic[i][j]);
			printf("\n");
		}
		continue;
imp:
		printf("Case #%d:\n", ++tcnt);
		printf("Impossible\n");
	
	}	
	return 0;
}
