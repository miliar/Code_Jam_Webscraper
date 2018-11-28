#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int T;
int N,K;
char allMap[55][55];
char rotateMap[55][55];
char gravityMap[55][55];
void rotate()
{
	for(int i = 0;i < N;i++)
		for(int j = N - 1;j >= 0;j--)
			rotateMap[i][N - 1 - j] = allMap[j][i];
}
void gravity()
{
	for(int i = 0;i < N;i++)
		for(int j = 0;j < N;j++)
			gravityMap[i][j] = '.';
	for (int i = 0;i < N;i++)
	{
		int index = N - 1;
		for(int j = N - 1;j >= 0;j--)
		{
			
			if(rotateMap[j][i] != '.')
				gravityMap[index--][i] = rotateMap[j][i];
		}
	}
}
void printMap(char myMap[55][55])
{
	for(int i = 0;i < N;i++)
	{
		for(int j = 0;j < N;j++)
			printf("%c", myMap[i][j]);
		printf("\n");
	}
}
bool findadj(char myMap[55][55], char color, int x,int y)
{
	bool flag = false;
	int sx = x;
	int sy = y;
	for(int i = 0;i < K;i++)
	{
		if(sx >= N || sx < 0) flag = true;
		if(sy >= N || sy < 0) flag = true;
		if(myMap[sx++][sy] != color) flag = true;
	}
	if(!flag) return true;

	flag = false;
	sx = x;
	sy = y;
	for(int i = 0;i < K;i++)
	{
		if(sx >= N || sx < 0) flag = true;
		if(sy >= N || sy < 0) flag = true;
		if(myMap[sx][sy++] != color) flag = true;
	}
	if(!flag) return true;


	flag = false;
	sx = x;
	sy = y;
	for(int i = 0;i < K;i++)
	{
		if(sx >= N || sx < 0) flag = true;
		if(sy >= N || sy < 0) flag = true;
		if(myMap[sx++][sy--] != color) flag = true;
	}
	if(!flag) return true;

	flag = false;
	sx = x;
	sy = y;
	for(int i = 0;i < K;i++)
	{
		if(sx >= N || sx < 0) flag = true;
		if(sy >= N || sy < 0) flag = true;
		if(myMap[sx++][sy++] != color) flag = true;
	}
	if(!flag) return true;
	return false;
}
bool findColor(char myMap[55][55], char color)
{
	for(int i = 0;i < N;i++)
	{
		for(int j = 0;j < N;j++)
			if(myMap[i][j] == color)
				if(findadj(myMap, color, i, j))
					return true;
	}
	return false;
}
int main()
{
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T;t++)
	{
		scanf("%d %d", &N, &K);
		for(int i = 0;i < N;i++)
			scanf("%s", allMap[i]);
		rotate();
		gravity();
		//printMap(gravityMap);
        bool flagR = findColor(gravityMap, 'R');
		bool flagB = findColor(gravityMap, 'B');
		if(flagB && flagR)
			printf("Case #%d: Both\n", t);
		else if(flagB && !flagR)
			printf("Case #%d: Blue\n", t);
		else if(!flagB && flagR)
			printf("Case #%d: Red\n", t);
		else
			printf("Case #%d: Neither\n", t);

	}
	return 0;
}