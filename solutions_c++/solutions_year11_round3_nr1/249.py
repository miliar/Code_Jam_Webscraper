#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

char in[100][100];

bool makeit(int l, int c)
{
	for (int i = 0; i < l; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			if (in[i][j] == '#')
			{
				if (i < l-1 && j < c-1)
				{
					if (in[i][j+1] == '#' && in[i+1][j+1] == '#' && in[i+1][j] == '#')
					{
						in[i][j] = '/';
						in[i][j+1] = '\\';
						in[i+1][j] = '\\';
						in[i+1][j+1] = '/';
						return makeit(l, c);
					}
					else
						return false;
				}
				else
					return false;
			}
		}
	}
	return true;
}

int main()
{
	int Q;
	scanf("%d", &Q);
	
	for (int q = 1; q <= Q; ++q)
	{
		printf("Case #%d:\n", q);
		
		int l, c;
		scanf("%d%d", &l, &c);
		for (int i = 0; i < l; ++i)
			scanf("%s", in[i]);
		
		bool good = makeit(l, c);
		if (!good)
			printf("Impossible\n");
		else
		{
			for (int i = 0; i < l; ++i)
			{
				
				for (int j = 0; j < c; ++j)
					printf("%c", in[i][j]);
				printf("\n");
			}
			//printf("\n");
		}
	}
	
	return 0;
}

