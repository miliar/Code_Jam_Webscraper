// bac small.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("C-small-attempt2.in");
ofstream fout("outdata.txt");
int c;
int r;
int map[101][101];

bool die()
{
	for(int i=1;i<=100;i++)
		for(int j=1;j<=100;j++)
			if(map[i][j]==1)
				return false;
	return true;
}


int _tmain(int argc, _TCHAR* argv[])
{
	fin>>c;
	for(int t=1;t<=c;t++)
	{
		fin>>r;
		for(int i=1;i<=100;i++)
			for(int j=1;j<=100;j++)
				map[i][j]=0;
		for(int k=0;k<r;k++)
		{
			int x1,x2,y1,y2;
			fin>>x1>>y1>>x2>>y2;
			for(int i=y1;i<=y2;i++)
				for(int j=x1;j<=x2;j++)
					map[i][j]=1;
		}

		int time=0;

		while(!die())
		{
			for(int i=100;i>0;i--)
				for(int j=100;j>0;j--)
					if(map[i][j]==0)
					{
						if(i>1&&j>1
							&&map[i-1][j]==1&&map[i][j-1]==1)
							map[i][j]=1;
					}
					else
					{
						if((i==1||map[i-1][j]==0)
							&&(j==1||map[i][j-1]==0))
							map[i][j]=0;
					}
			time++;
		}
		fout<<"Case #"<<t<<": "<<time<<endl;
	}
	return 0;
}

