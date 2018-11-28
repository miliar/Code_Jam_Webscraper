#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>
using namespace std;

const int MAX = 205;

char mm[55][55];
int ans[55][55];
int a, b;

bool go()
{
	memset(ans, 0, sizeof(ans));
	for(int i = 0; i < a; i++)  for(int j = 0; j < b; j++)
	{
		if(ans[i][j])  continue;
		if(mm[i][j] == '#')
		{
			if(i == a - 1 || j == b - 1)  return false;
			if(mm[i + 1][j] != '#' || mm[i][j + 1] != '#'
				|| mm[i + 1][j + 1] != '#')
				return false;

			ans[i][j] = ans[i + 1][j + 1] = 1;
			ans[i + 1][j] = ans[i][j + 1] = 2;
		}
	}
	return true;
}

int main()
{
	freopen("d:\\Desktop\\GCJ\\A-large (1).in", "r", stdin);
	freopen("d:\\Desktop\\GCJ\\A-large (1).out", "w", stdout);
	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		printf("Case #%d:\n", ++c);
		scanf("%d%d", &a, &b);
		for(int i = 0; i < a; i++)
			scanf("%s", mm[i]);
		if(!go())  printf("Impossible\n");
		else
		{
			for(int i = 0; i < a; i++)
			{
				for(int j = 0; j < b; j++)
				{
					if(ans[i][j] == 0)  printf(".");
					else if(ans[i][j] == 1)  printf("/");
					else  printf("\\");
				}
				printf("\n");
			}
		}
	}
}