/*************************************************************************
    > File Name: a.cpp
    > Author: withwind
    > Mail: withwind93@gmail.com 
    > Created Time: 2013/4/13 10:09:37
 ************************************************************************/

#include <limits.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
using namespace std;
char s[5];
int a[5][5];
int flag =0;
void check(int x1,int y1,int x2,int y2)
{
	int count = 0;
	for(int i=x1;i<=x2;i++)
	{
		for(int j=y1;j<=y2;j++)
		  if(a[i][j] == 1 || a[i][j]==3)	count++;
	}
	if(count == 4)	{flag=1;return ;}
	
	count = 0;
	for(int i=x1;i<=x2;i++)
	{
		for(int j=y1;j<=y2;j++)
		  if(a[i][j] == 2 || a[i][j]==3)	count++;
	}
	if(count == 4)	{flag=2;return ;}
}
void xx()
{
	int count = 0;
	for(int i=1;i<=4;i++)
	{
		  if(a[i][i] == 1 || a[i][i]==3)	count++;
	}
	if(count == 4)	{flag=1;return ;}

	count = 0;
	for(int i=1;i<=4;i++)
	{
		  if(a[i][i] == 2 || a[i][i]==3)	count++;
	}
	if(count == 4)	{flag=2;return ;}
}
void yy()
{
	int count = 0;
	for(int i=1;i<=4;i++)
	{
		  if(a[i][5-i] == 1 || a[i][5-i]==3)	count++;
	}
	if(count == 4)	{flag=1;return ;}

	count = 0;
	for(int i=1;i<=4;i++)
	{
		  if(a[i][5-i] == 2 || a[i][5-i]==3)	count++;
	}
	if(count == 4)	{flag=2;return ;}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k;
	int t;
	int count = 0;
	scanf("%d",&t);
	for(int casen=1;casen<=t;casen++)
	{
		count = 0;
		for(i=1;i<=4;i++)
		{
			scanf("%s",s);
			for(j=0;j<4;j++)
			{
				if(s[j]=='X')	a[i][j+1]=1;
				else if(s[j]=='O')	a[i][j+1]=2;
				else if(s[j]=='T')	a[i][j+1]=3;
				else if(s[j]=='.')	
				{
					a[i][j+1]=4;
					count++;
				}
			}
		}
		flag = 0;
		for(i=1;i<=4;i++)
		{
			if(flag)	break;
			check(1,i,4,i);
		}
		for(i=1;i<=4 && flag==0;i++)
		{
			if(flag)	break;
			check(i,1,i,4);
		}
		if(!flag)	
		{
			xx();
			yy();
		}
		printf("Case #%d: ",casen);
		if(flag == 1)	printf("X won\n");
		else if(flag == 2)	printf("O won\n");
		else if(count)		printf("Game has not completed\n");
		else				printf("Draw\n");
	}
	return 0;
}
