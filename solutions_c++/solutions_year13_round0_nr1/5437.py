#include <iostream>
#include <string>
#include <math.h>

#include <stdlib.h>
#include <stdio.h>

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(v,p,k) for(int v=p;v<=k;v++)

using namespace std;

char board[4][4];
bool some_pt;

char test(int x,int y,int vx,int vy)
{
	char pl='T';
	while(x>=0 && x<4 && y>=0 && y<4)
	{
		if(board[x][y]=='.')some_pt=true;
		if(pl=='T')
		{
			pl=board[x][y];
			if(pl=='.')return '.';
		}
		else if(board[x][y]!=pl && board[x][y]!='T')return '.';
		x+=vx;
		y+=vy;
	}
	return pl;
}

void mod(char &s,char sb)
{
	if(s=='.')s=sb;
}

int main()
{
	int t;
	some_pt;
	char res;
	cin>>t;
	FOR(c,1,t)
	{
		res='.';
		some_pt=false;
		FOR(i,0,3)
		{
			FOR(j,0,3)
			{
				cin>>board[i][j];
			}
		}
		FOR(x,0,3)
		{
			mod(res,test(x,0,0,1));
		}
		mod(res,test(0,0,1,1));
		FOR(y,0,3)
		{
			mod(res,test(0,y,1,0));
		}
		mod(res,test(0,3,1,-1));
		string res_st;
		if(res=='O')res_st="O won";
		else if(res=='X')res_st="X won";
		else if(some_pt)res_st="Game has not completed";
		else res_st="Draw";
		printf("Case #%d: %s\n",c,res_st.c_str());
	}
}
