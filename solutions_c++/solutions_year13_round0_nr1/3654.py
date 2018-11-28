#include<stdio.h>
char map[5][5];
int site[2];
int judge(char ch)
{
	int i;
	for( i = 0; i < 4; i ++)
	{
		if(  
			(map[i][0] & map[i][1] & map[i][2] & map[i][3]) == ch 
			|| (map[0][i] & map[1][i] & map[2][i] & map[3][i]) == ch
			 )
		{
			return 1;
		}

	}
	if( (map[0][0] & map[1][1] & map[2][2] & map[3][3]) == ch)
	{
		return 1;
	}
	if( (map[0][3] & map[1][2] & map[2][1] & map[3][0]) == ch)
	{
		return 1;
	}
	return 0;
}
int existPoint()
{
	int i, j;
	for(i = 0; i < 4; i ++)
	{
		for(j = 0; j < 4; j ++)
			if( map[i][j] == '.' )
				return 1;
	}
	return 0;
}

int main()
{
	int n, i, j, k;
	scanf("%d", &n);
	for(i = 1; i <= n; i ++)
	{
		for(j = 0; j < 4; j ++)
			scanf("%s", map[j]);
		site[0] = -1;
		for(j = 0; j < 4; j ++)
		{
			for(k = 0; k < 4; k ++)
			{
				if( map[j][k] == 'T')
				{
					site[0] = j;
					site[1] = k;
					break;
				}
			}
		}
		if( site[0] != -1)
			map[ site[0] ][ site[1] ] = 'X';
		if( judge('X') == 1 )
		{
			printf("Case #%d: X won\n", i);
			continue;
		}
		if( site[0] != -1)
			map[ site[0] ][ site[1] ] = 'O';
		if( judge('O') == 1 )
		{
			printf("Case #%d: O won\n", i);
			continue;
		}
		if(existPoint() == 1)
			printf("Case #%d: Game has not completed\n", i);
		else
			printf("Case #%d: Draw\n", i);
	}
	return 0;
}
