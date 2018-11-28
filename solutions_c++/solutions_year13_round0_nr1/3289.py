#include<cstdio>
#include<cstring>

using namespace std;

int T, boo, br;
char s[10][10];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &T);
	for (int g = 0; g < T; g++)
	{              
		for (int i = 0; i < 5; i++)
			gets(s[i]);
		br = 0;
		for (int i = 0; i < 4; i++)
		{
			boo = 0;
    		for (int j = 0; j < 4; j++)
			{
				if (s[i][j] == '.' || s[i][j] == 'O')
					boo = 1;
			}
			if (boo == 0)
			{
				printf("Case #%d: X won\n", g + 1);
				br = 1;
				break;
			}         
		} 
		if (br == 1)
			continue;
		for (int i = 0; i < 4; i++)
		{
			boo = 0;
    		for (int j = 0; j < 4; j++)
			{
				if (s[j][i] == '.' || s[j][i] == 'O')
					boo = 1;
			}
			if (boo == 0)
			{
				printf("Case #%d: X won\n", g + 1);
				br = 1;
				break;
			}
		}
		if (br == 1)
			continue;
		if ((s[0][0] == 'X' || s[0][0] == 'T') && (s[1][1] == 'X' || s[1][1] == 'T') 
		&& (s[2][2] == 'X' || s[2][2] == 'T') && (s[3][3] == 'X' || s[3][3] == 'T'))
		{
			printf("Case #%d: X won\n", g + 1);
			continue;
		}	
		if ((s[0][3] == 'X' || s[0][3] == 'T') && (s[1][2] == 'X' || s[1][2] == 'T') 
		&& (s[2][1] == 'X' || s[2][1] == 'T') && (s[3][0] == 'X' || s[3][0] == 'T'))
		{
			printf("Case #%d: X won\n", g + 1);
			continue;
		}	       
		for (int i = 0; i < 4; i++)
		{
			boo = 0;
    		for (int j = 0; j < 4; j++)
			{
				if (s[i][j] == '.' || s[i][j] == 'X')
					boo = 1;
			}
			if (boo == 0)
			{
				printf("Case #%d: O won\n", g + 1);
				br = 1;
				break;
			}         
		} 
		if (br == 1)
			continue;
		for (int i = 0; i < 4; i++)
		{
			boo = 0;
    		for (int j = 0; j < 4; j++)
			{
				if (s[j][i] == '.' || s[j][i] == 'X')
					boo = 1;
			}
			if (boo == 0)
			{
				printf("Case #%d: O won\n", g + 1);
				br = 1;
				break;
			}
		}
		if (br == 1)
			continue;
		if ((s[0][0] == 'O' || s[0][0] == 'T') && (s[1][1] == 'O' || s[1][1] == 'T') 
		&& (s[2][2] == 'O' || s[2][2] == 'T') && (s[3][3] == 'O' || s[3][3] == 'T'))
		{
			printf("Case #%d: O won\n", g + 1);
			continue;
		}	
		if ((s[0][3] == 'O' || s[0][3] == 'T') && (s[1][2] == 'O' || s[1][2] == 'T') 
		&& (s[2][1] == 'O' || s[2][1] == 'T') && (s[3][0] == 'O' || s[3][0] == 'T'))
		{
			printf("Case #%d: O won\n", g + 1);
			continue;
		}
		boo = 0; 
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (s[i][j] == '.')
					boo = 1;
	   	if (boo == 1)
	   	{
	   		printf("Case #%d: Game has not completed\n", g + 1);
	   		continue;
	   	}
	   	printf("Case #%d: Draw\n", g + 1);
	}
	return 0;
}
