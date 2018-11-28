#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int map[4][4];
char w;

int test(int c)
{
	if((map[0][0] == c || map[0][0] == 3) && (map[1][1] == c || map[1][1] == 3) && (map[2][2] == c || map[2][2] == 3) && (map[3][3] == c || map[3][3] == 3)) return 1;
	else if((map[0][3] == c || map[0][3] == 3) && (map[1][2] == c || map[1][2] == 3) && (map[2][1] == c || map[2][1] == 3) && (map[3][0] == c || map[3][0] == 3)) return 1;
	
	else if((map[0][0] == c || map[0][0] == 3) && (map[0][1] == c || map[0][1] == 3) && (map[0][2] == c || map[0][2] == 3) && (map[0][3] == c || map[0][3] == 3)) 
		return 1;
	else if((map[1][0] == c || map[1][0] == 3) && (map[1][1] == c || map[1][1] == 3) && (map[1][2] == c || map[1][2] == 3) && (map[1][3] == c || map[1][3] == 3)) return 1;
	else if((map[2][0] == c || map[2][0] == 3) && (map[2][1] == c || map[2][1] == 3) && (map[2][2] == c || map[2][2] == 3) && (map[2][3] == c || map[2][3] == 3)) return 1;
	else if((map[3][0] == c || map[3][0] == 3) && (map[3][1] == c || map[3][1] == 3) && (map[3][2] == c || map[3][2] == 3) && (map[3][3] == c || map[3][3] == 3)) return 1;
	
	else if((map[0][0] == c || map[0][0] == 3) && (map[1][0] == c || map[1][0] == 3) && (map[2][0] == c || map[2][0] == 3) && (map[3][0] == c || map[3][0] == 3)) return 1;
	else if((map[0][1] == c || map[0][1] == 3) && (map[1][1] == c || map[1][1] == 3) && (map[2][1] == c || map[2][1] == 3) && (map[3][1] == c || map[3][1] == 3)) return 1;
	else if((map[0][2] == c || map[0][2] == 3) && (map[1][2] == c || map[1][2] == 3) && (map[2][2] == c || map[2][2] == 3) && (map[3][2] == c || map[3][2] == 3)) return 1;
	else if((map[0][3] == c || map[0][3] == 3) && (map[1][3] == c || map[1][3] == 3) && (map[2][3] == c || map[2][3] == 3) && (map[3][3] == c || map[3][3] == 3)) return 1;

	return 0;
}

int main()
{
/**#ifndef ONLINE_JUDGE
freopen("D:\\in.txt","r",stdin);
freopen("D:\\out.txt", "w", stdout);
#endif*/

	int k;
	scanf("%d", &k);
	int th = 1;
	while(k--)
	{
		int i, j, x=0, o=0, t=0, p=0;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				//scanf("%c", &w);
				cin>>w;
				if(w == 'X')
				{
					map[i][j] = 1;
					x++;
				}
				else if(w == 'O')
				{
					map[i][j] = 2;
					o++;
				}
				else if(w == 'T')
				{
					map[i][j] = 3;
					t++;
				}
				else if(w == '.')
				{
					map[i][j] = 0;
					p++;
				}
			}
		}
		printf("Case #%d: ", th++);
		if(o<3 && x<3)
		{
			printf("Game has not completed\n");
			continue;
		}
		else if(test(2))
		{
			printf("O won\n");
		}
		else if(test(1))
		{
			printf("X won\n");
		}
		else if(x+o+t == 16)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}
	}
	return 0;
}

