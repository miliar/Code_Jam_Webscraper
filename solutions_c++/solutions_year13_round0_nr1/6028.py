//============================================================================
// Name        : tictoce.cpp
// Author      : Mostafa Shokrof
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;
struct point
{
	int x;
	int y;
	point(int a,int b){x=a;y=b;}
};
int main() {
	int t;
	cin>>t;
	char board[4][4];
	vector <vector<point> > diagonals;
	vector<point> d;


	d.push_back(point(0,0));
	d.push_back(point(1,1));
	d.push_back(point(2,2));
	d.push_back(point(3,3));
	diagonals.push_back(d);
	d.clear();

	d.push_back(point(3,0));
	d.push_back(point(2,1));
	d.push_back(point(1,2));
	d.push_back(point(0,3));
	diagonals.push_back(d);
	d.clear();

	for(int p=0;p<t;p++)
	{
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				board[i][j]='.';
		bool draw=true;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>board[i][j];
				if(board[i][j]=='.')
					draw=false;
			}
		//horizontal

		bool won=false;
		int xs=0,os=0,ts=0;
		for(int i=0;i<4&&!won;i++){
			xs=0,os=0,ts=0;
			for(int j=0;j<4&&!won;j++)
			{

				if(board[i][j]=='X')
					xs++;
				else if(board[i][j]=='O')
					os++;
				else if(board[i][j]=='T')
					ts++;
			}
			if(os==4||(ts==1&&os==3))
			{
				printf("Case #%d: O won\n",p+1);
				won=true;
				break;
			}
			if(xs==4||(ts==1&&xs==3))
			{
				printf("Case #%d: X won\n",p+1);
				won=true;
				break;
			}

		}
		if(won)
			continue;



		//vertical
		won=false;
		for(int j=0;j<4&&!won;j++)
		{
			xs=0,os=0,ts=0;
			for(int i=0;i<4&&!won;i++)
			{
				if(board[i][j]=='X')
					xs++;
				else if(board[i][j]=='O')
					os++;
				else if(board[i][j]=='T')
					ts++;
			}
			if(os==4||(ts==1&&os==3))
			{
				printf("Case #%d: O won\n",p+1);
				won=true;
				break;
			}
			if(xs==4||(ts==1&&xs==3))
			{
				printf("Case #%d: X won\n",p+1);
				won=true;
				break;
			}
		}
		if(won)
			continue;
		xs=0,os=0,ts=0;
		for(int i=0;i<diagonals.size();i++)
		{
			xs=0,os=0,ts=0;
			for(int j=0;j<diagonals[i].size();j++)
			{
				if(board[diagonals[i][j].y][diagonals[i][j].x]=='X')
					xs++;
				else if(board[diagonals[i][j].y][diagonals[i][j].x]=='O')
					os++;
				else if(board[diagonals[i][j].y][diagonals[i][j].x]=='T')
					ts++;
			}
			if(os==4||(ts==1&&os==3))
			{
				printf("Case #%d: O won\n",p+1);
				won=true;
				break;
			}
			if(xs==4||(ts==1&&xs==3))
			{
				printf("Case #%d: X won\n",p+1);
				won=true;
				break;
			}
		}
		if(won)
			continue;
		if(draw)
			printf("Case #%d: Draw\n",p+1);
		else
			printf("Case #%d: Game has not completed\n",p+1);

	}
	return 0;
}
