#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<fstream>

using namespace std;

#define MAXN 55

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int R,C;

string map[MAXN];

bool judge(int x,int y)
{
	if(x+1>=R || y+1>=C) return false;
	else return map[x+1][y]=='#' && map[x][y+1]=='#' && map[x+1][y+1]=='#';
}

int main()
{
	int ct,text;
	fin>>text;
	for(ct=1;ct<=text;ct++)
	{
		int i,j;
		bool ok=true;
		fout<<"Case #"<<ct<<":"<<endl;
		fin>>R>>C;
		for(i=0;i<R;i++)
		{
			fin>>map[i];
		}
		for(i=0;i<R && ok;i++)
		{
			for(j=0;j<C;j++)
			{
				if(map[i][j]=='#')
				{
					if(judge(i,j))
					{
						map[i][j]='/';
						map[i][j+1]='\\';
						map[i+1][j]='\\';
						map[i+1][j+1]='/';
					}
					else
					{
						ok=false;
						break;
					}
				}
			}
		}
		if(ok)
		{
			for(i=0;i<R;i++) fout<<map[i]<<endl;
		}
		else
		{
			fout<<"Impossible"<<endl; 
		}
	}
	return 0;
}
