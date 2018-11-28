// code jam.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

string map[4];
int n;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>n;	
	for(int T=0;T<n;T++)
	{
		for(int i=0;i<4;i++)
			cin>>map[i];
		bool xwin =false;
		bool owin = false;
		for(int i=0;i<4;i++)
		{
			if((map[i][0] =='X'||map[i][0] =='T') && (map[i][1] =='X'||map[i][1] =='T') && (map[i][2] =='X'||map[i][2] =='T') && (map[i][3] =='X'||map[i][3] =='T'))
			{
				xwin =true;
				break;
			}
			if((map[0][i] =='X'||map[0][i] =='T') && (map[1][i] =='X'||map[1][i] =='T') && (map[2][i] =='X'||map[2][i] =='T') && (map[3][i] =='X'||map[3][i] =='T'))
			{
				xwin = true;
				break;
			}
			if((map[i][0] =='O'||map[i][0] =='T') && (map[i][1] =='O'||map[i][1] =='T') && (map[i][2] =='O'||map[i][2] =='T') && (map[i][3] =='O'||map[i][3] =='T'))
			{
				owin =true;
				break;
			}
			if((map[0][i] =='O'||map[0][i] =='T') && (map[1][i] =='O'||map[1][i] =='T') && (map[2][i] =='O'||map[2][i] =='T') && (map[3][i] =='O'||map[3][i] =='T'))
			{
				owin = true;
				break;
			}
		}
		if((map[0][0] =='X'||map[0][0] =='T') && (map[1][1] =='X'||map[1][1] =='T') && (map[2][2] =='X'||map[2][2] =='T') && (map[3][3] =='X'||map[3][3] =='T'))
			xwin = true;
		if((map[0][3] =='X'||map[0][3] =='T') && (map[1][2] =='X'||map[1][2] =='T') && (map[2][1] =='X'||map[2][1] =='T') && (map[3][0] =='X'||map[3][0] =='T'))
			xwin = true;
		if((map[0][0] =='O'||map[0][0] =='T') && (map[1][1] =='O'||map[1][1] =='T') && (map[2][2] =='O'||map[2][2] =='T') && (map[3][3] =='O'||map[3][3] =='T'))
			owin = true;
		if((map[0][3] =='O'||map[0][3] =='T') && (map[1][2] =='O'||map[1][2] =='T') && (map[2][1] =='O'||map[2][1] =='T') && (map[3][0] =='O'||map[3][0] =='T'))
			owin = true;
		cout<<"Case #"<<T+1<<": ";
		if(xwin) cout<<"X won\n";
		if(owin) cout<<"O won\n";
		bool draw =false;
		bool comp = false;
		if(!xwin && !owin)
		{
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
				{
					if(map[i][j]=='.')
					{
						comp=true;
						break;
					}
				}
			if(comp)
			{
				cout<<"Game has not completed\n";
			}
			else
			{
				cout<<"Draw\n";
			}
		}
	}
	return 0;
}

