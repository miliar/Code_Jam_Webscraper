#include <stdio.h>
char ss[10], str[10][10];

int calc()
{
	for(int i = 0; i < 4; i++)
		scanf("%s", &str[i][0]);
		
	for(int r = 0; r < 4; r++)
	{
		int c;
		for(c = 0; c < 4; c++)
			if(str[r][c] != 'O' && str[r][c] != 'T')
				break;
		if(c == 4) return 0;
		
		for(c = 0; c < 4; c++)
			if(str[r][c] != 'X' && str[r][c] != 'T')
				break;
		if(c == 4) return 1;
	}
	
	for(int c = 0; c < 4; c++)
	{
		int r;
		for(r = 0; r < 4; r++)
			if(str[r][c] != 'O' && str[r][c] != 'T') 
				break;
		if(r == 4) return 0;
		
		for(r = 0; r < 4; r++)
			if(str[r][c] != 'X' && str[r][c] != 'T') 
				break;
		if(r == 4) return 1;
	}
	
	int i;
	for(i = 0; i < 4; i++)
		if(str[i][i] != 'O' && str[i][i] != 'T') 
			break;
	if(i == 4) return 0;
	
	for(i = 0; i < 4; i++)
		if(str[i][i] != 'X' && str[i][i] != 'T') 
			break;
	if(i == 4) return 1;
	
	for(i = 0; i < 4; i++)
		if(str[i][3 - i] != 'O' && str[i][3 - i] != 'T')
			break;
	if(i == 4) return 0;
	
	for(i = 0; i < 4; i++)
		if(str[i][3 - i] != 'X' && str[i][3 - i] != 'T')
			break;
	if(i == 4) return 1;
	
	for(int r = 0; r < 4; r++)
	{
		for(int c = 0; c < 4; c++)
		{
			if(str[r][c] == '.')
				return 3;
		}
	}
	
	return 2;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 0; t < T; t++)
	{
		int r = calc();
		
		if(r == 0)
			printf("Case #%d: O won\n", t + 1);
		if(r == 1)
			printf("Case #%d: X won\n", t + 1);
		if(r == 2)
			printf("Case #%d: Draw\n", t + 1);
		if(r == 3)
			printf("Case #%d: Game has not completed\n", t + 1);
	
	}
	return 0;
}
