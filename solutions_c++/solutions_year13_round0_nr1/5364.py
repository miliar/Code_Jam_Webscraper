// File Name: a3.cpp
// Author: gonewithsin
// Created Time: 2013/4/13 22:52:33

#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<queue>
using namespace std;

int mark;
int map[5][5];

bool f(int x)
{
	map[mark / 4 + 1][mark % 4 + 1] = x;
	for(int i = 1; i <= 4; i++)
		if(map[1][i] == x && map[1][i] == map[2][i] && 
				map[1][i] == map[3][i] && map[1][i] == map[4][i])
					return 1;
	for(int i = 1; i <= 4; i++)
		if(map[i][1] == x && map[i][1] == map[i][2] && 
				map[i][1] == map[i][3] && map[i][1] == map[i][4])
					return 1;
	if(map[1][1] == x && map[1][1] == map[2][2] && map[1][1] == map[3][3]
			&& map[1][1] == map[4][4])
		return 1;
	if(map[4][1] == x && map[4][1] == map[3][2] && map[4][1] == map[2][3]
			&& map[4][1] == map[1][4])
		return 1;
	return 0;
}

int main()
{
	int t, cases = 0,count;
	char s[5];
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);	
	scanf("%d", &t);
	while(t--)
	{
		mark = -1;
		cases++;
		count = 0;
		for(int i = 0; i < 4; i++)
		{
			scanf("%s", s );
			for(int j = 0;j < 4;j++)
			{
				if(s[j] == 'X')	map[i + 1][j + 1] = 1;
				if(s[j] == 'O')	map[i + 1][j + 1] = 2;
				if(s[j] == '.')	map[i + 1][j + 1] = 0, count++;
				if(s[j] == 'T')	map[i + 1][j + 1] = 3, mark = i * 4 + j;
			}
		}
		printf("Case #%d: ", cases);
		if(f(1))
		{
			printf("X won\n");
			continue;
		}
		if(f(2))
		{
			printf("O won\n");
			continue;
		}
		if(count==0) printf("Draw");
		else printf("Game has not completed");
		puts("");
	}
	return 0;
}


