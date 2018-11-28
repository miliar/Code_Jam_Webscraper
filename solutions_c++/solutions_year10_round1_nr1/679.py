// Rotate.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
using namespace std;

char map[51][51];
char mat[51][51];
int m,t;

bool legal(int x,int y)
{
	if(x<1||x>m||y<1||y>m)
		return false;
	return true;
}

bool check(int x,int y)
{
	int dir[4][2]={1,0,0,1,1,1,1,-1};
	int i,k,tx,ty;
	for(i=0;i<4;i++)
	{
		tx=x;
		ty=y;
		for(k=1;k>=1;k++)
		{
			tx+=dir[i][0];
			ty+=dir[i][1];
			if(!legal(tx,ty))
				break;
			if(mat[tx][ty]!=mat[x][y])
				break;
		}
		if(k==t)
			return true;
	}
	return false;
}

int main()
{
	freopen("debug\\in.txt","r",stdin);
	freopen("debug\\out.txt","w",stdout);
	int repeat;
	int i,j,k,x,y;
	char ch;
	int cases=1;
	cin>>repeat;
	while(repeat--)
	{
		cin>>m>>t;
		for(i=1;i<=m;i++)
			for(j=1;j<=m;j++)
				cin>>map[i][j];
		for(i=1;i<=m;i++)
			for(j=1;j<=m;j++)
				mat[i][j]='.';
		for(i=1;i<=m;i++)
			for(j=1;j<=m;j++)
			{
				x=j;
				y=m-i+1;
				mat[x][y]=map[i][j];
			}
		bool red,blue;
		red=blue=false;
		

		for(i=m;i>=1;i--)
		{
			for(j=1;j<=m;j++)
			{
				for(k=i+1;k<=m;k++)
					if(mat[k][j]!='.')
						break;
				k--;
				ch=mat[i][j];
				mat[i][j]='.';
				mat[k][j]=ch;
			}
		}
		
		
		for(i=1;i<=m;i++)
			for(j=1;j<=m;j++)
			{
				if(mat[i][j]=='.')
					continue;
				if(mat[i][j]=='R'&&check(i,j))
					red=true;
				if(mat[i][j]=='B'&&check(i,j))
					blue=true;
			}
			printf("Case #%d: ",cases++);
		if(!red&&!blue)
			printf("Neither\n");
		if(red&&blue)
			printf("Both\n");
		if(red&&!blue)
			printf("Red\n");
		if(blue&&!red)
			printf("Blue\n");
	}


	return 0;
}

