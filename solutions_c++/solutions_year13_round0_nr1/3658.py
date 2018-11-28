#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;

char map[5][5];

int judge()
{
	int i, j, en = 1;
	for(i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(map[i][j] == '.')
				en = 0;
			if(map[i][j] == 'X' || map[i][j] == 'T')
			{
				int f[4] = {1,1,1,1};
				for(int k=1;k<4;k++)
				{
					if(i + k > 4 || (map[i+k][j] != 'X' && map[i+k][j] != 'T') || (map[i][j] == 'T' && map[i+k][j] == 'T'))
						f[0] = 0;
					if(j + k > 4 || (map[i][j+k] != 'X' && map[i][j+k] != 'T') || (map[i][j] == 'T' && map[i+k][j] == 'T'))
						f[1] = 0;
					if((j + k > 4 && i + k > 4) || (map[i+k][j+k] != 'X' && map[i+k][j+k] != 'T') || (map[i][j] == 'T' && map[i+k][j+k] == 'T'))
						f[2] = 0;
					if((i + k > 4 && j - k < 0) || (map[i+k][j-k] != 'X' && map[i+k][j-k] != 'T') || (map[i][j] == 'T' && map[i+k][j-k] == 'T'))
						f[3] = 0;
				}
				if(f[0] || f[1] || f[2] || f[3])
					return 1;
			}
			if(map[i][j] == 'O' || map[i][j] == 'T')
			{
				int f[4] = {1,1,1,1};
				for(int k=1;k<4;k++)
				{
					if(i + k > 4 || (map[i+k][j] != 'O' && map[i+k][j] != 'T') || (map[i][j] == 'T' && map[i+k][j] == 'T'))
						f[0] = 0;
					if(j + k > 4 || (map[i][j+k] != 'O' && map[i][j+k] != 'T') || (map[i][j] == 'T' && map[i+k][j] == 'T'))
						f[1] = 0;
					if((j + k > 4 && i + k > 4) || (map[i+k][j+k] != 'O' && map[i+k][j+k] != 'T') || (map[i][j] == 'T' && map[i+k][j+k] == 'T'))
						f[2] = 0;
					if((i + k > 4 && j - k < 0) || (map[i+k][j-k] != 'O' && map[i+k][j-k] != 'T') || (map[i][j] == 'T' && map[i+k][j-k] == 'T'))
						f[3] = 0;
				}
				if(f[0] || f[1] || f[2] || f[3])
					return 2;
			}
		}
	}
	if(en != 0)
		return 3;
	return 4;
}

int main()
{
	int T, cas;
	scanf("%d" , &T);
	for(cas = 1; cas <= T; cas++)
	{
		for(int i=0;i<4;i++)
		{
			scanf("%s", map[i]);
		}
		int ans = judge();
		printf("Case #%d: ", cas);
		if(ans == 1)
			printf("X won");
		else if( ans == 2)
			printf("O won");
		else if( ans == 3)
			printf("Draw");
		else
			printf("Game has not completed");
		printf("\n");
	}
	return 0;
}
