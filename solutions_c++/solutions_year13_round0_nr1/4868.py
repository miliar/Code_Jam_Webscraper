//============================================================================
// Name        : code_jam.cpp
// Author      : wfy
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int swap(char c)
{
	if(c=='T') return 1000;
	else if(c=='O') return 1;
	else if(c=='X') return 100;
	else if(c=='.') return 0;
}
int main()
{
	int map[5][5];
	char a[5];
	int T,flag,flago,flagx;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		flag=0;
		flago=0;
		flagx=0;
		for(int i=0;i<4;i++)
		{
			scanf("%s",a);
			for(int j=0;j<4;j++)
			{
				map[i][j]=swap(a[j]);
				if(map[i][j]==0) flag=1;
			}
		}
		int tmp;
		tmp=map[3][0]+map[2][1]+map[1][2]+map[0][3];
		if(tmp==400||tmp==1300) flagx=1;
		if(tmp==4||tmp==1003) flago=1;
		tmp=map[0][0]+map[1][1]+map[2][2]+map[3][3];
		if(tmp==400||tmp==1300) flagx=1;
		if(tmp==4||tmp==1003) flago=1;
		for(int i=0;i<4;i++)
		{
			tmp=map[i][0]+map[i][1]+map[i][2]+map[i][3];
			if(tmp==400||tmp==1300) flagx=1;
			if(tmp==4||tmp==1003) flago=1;
			tmp=map[0][i]+map[1][i]+map[2][i]+map[3][i];
			if(tmp==400||tmp==1300) flagx=1;
			if(tmp==4||tmp==1003) flago=1;
		}
		if(flagx==1)
		{
			if(flago==0) printf("X won\n");
			else printf("Draw\n");
		}
		else
		{
			if(flago) printf("O won\n");
			else if(flag) printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
	return 0;
}
