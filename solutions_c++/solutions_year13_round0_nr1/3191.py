#include <stdio.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>

using namespace std;

int N;
char input[10][10];
int searchDown(int x,int y)
{
	char c = input[x][y];
	if(c =='T'){c = input[++x][y];x++;}
	if(c == '.')
		return 0;
	
	while(x<4)
	{
		if(input[x][y] != c && input[x][y] != 'T')
			return 0;
		x++;
	}
	if(c == 'X')
		return 1;
	else
		return 2;
	
	
}
int searchWag(int x,int y)
{
	char c = input[x][y];
	if(c =='T'){c = input[x][++y];y++;}
	if(c == '.')return 0;
	
	while(y<4)
	{
		if(input[x][y] != c && input[x][y] != 'T')
			return 0;
		y++;
	}
	if(c == 'X')
		return 1;
	else
		return 2;
}

int searchDia(int x,int y)
{
	int laufx = 1,laufy = 1;
	
	if(x == 3)
		laufx = -1;
	if(y == 3)
		laufy = -1;
	
	char c = input[x][y];
	if(c =='T'){y+=laufy;x+=laufx;c = input[x][y];y+=laufy;x+=laufx;}
	if(c == '.')return 0;
	
	while(y<4 && y >=0)
	{

		if(input[x][y] != c && input[x][y] != 'T')
			return 0;
		y+=laufy;
		x+=laufx;
	}

	if(c == 'X')return 1;
	else return 2;	
	
}

int main()
{
	scanf("%d",&N);
	for(int i = 0; i<  N;i++)
	{
		for(int j = 0; j<4;j++)
				scanf("%s",input[j]);
		int result = 0;
		
		for(int j = 0; j < 4;j++)
		{
			for(int k = 0; k < 4;k++)
			{
				if(input[j][k] != '.')
				{
					if(j == 0)
					{
						int temp = searchDown(j,k);
						if(temp == 1) result = 2;
						if(temp == 2) result = 3;
						//printf("Down: %d %c",temp,input[j][k]);
					}
					if(k == 0)
					{
						int temp = searchWag(j,k);
						if(temp == 1) result = 2;
						if(temp == 2) result = 3;
						//printf("Wag: %d ",temp);
					}
					if((j == 0 || j == 3) && (k == 0 || k == 3))
					{
						int temp = searchDia(j,k);
						
						if(temp == 1) result = 2;
						if(temp == 2) result = 3;
						//printf("Dia: %d %c",temp,input[j][k]);
					}
				}
				else
				{
					if(!result)
						result = 1;
				}
				//printf("\n");
			}
		}
		if(result == 0)
			printf("Case #%d: Draw\n",i+1);
		if(result == 1)
			printf("Case #%d: Game has not completed\n",i+1);
		if(result == 2)
			printf("Case #%d: X won\n",i+1);
		if(result == 3)
			printf("Case #%d: O won\n",i+1);
	}
	return 0;
}

