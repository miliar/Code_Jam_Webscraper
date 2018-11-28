#include<math.h>
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<time.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

//typedef long long lld;
//typedef __int64 lld;//这里的时候要用long long
const int INF=1000000000;
const int MAX=51000;
char mat[5][5];
int bit[5][5];
int getres(int tmp)
{
	if((1<<3)&tmp)return -1;//有.
	if((3&tmp)==3||(3&tmp)==0)return -1;//没有X或者O
	if((1&tmp))return 0;
	return 1;
}
bool rwin(char x,int r)
{
	int i;
	for(i=0;i<4;i++)
	{
		if(mat[r][i]!=x&&mat[r][i]!='T')return false;
	}
	return true;
}
bool cwin(char x,int r)
{
	int i;
	for(i=0;i<4;i++)
	{
		if(mat[i][r]!=x&&mat[i][r]!='T')return false;
	}
	return true;
}
bool rdig(char x,int r)
{
	int i;
	for(i=0;i<4;i++)
	{
		if(mat[i][i]!=x&&mat[i][i]!='T')return false;
	}
	return true;
}
bool ldig(char x,int r)
{
	int i;
	for(i=0;i<4;i++)
	{
		if(mat[i][4-i-1]!=x&&mat[i][4-i-1]!='T')return false;
	}
	return true;
}
int main()
{
	int n;
	int i,j;
	int ans=INF;
	int T,CS=1;
	//freopen("E:\\ACM\\A-large.in","r",stdin);
	//freopen("E:\\ACM\\A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		int tot=0;
		for(i=0;i<4;i++)
		{
			scanf("%s",mat[i]);
			for(j=0;j<4;j++)tot+=(mat[i][j]=='.');
		}
		bool xwin=false,owin=false;
		int tmp;
		for(i=0;i<4;i++)
		{
			if(rwin('X',i))xwin=true;
			else if(rwin('O',i))owin=true;
		}
		for(i=0;i<4;i++)
		{
			if(cwin('X',i))xwin=true;
			else if(cwin('O',i))owin=true;
		}
		if(rdig('X',i))xwin=true;
		else if(rdig('O',i))owin=true;

		if(ldig('X',i))xwin=true;
		else if(ldig('O',i))owin=true;

		if(xwin)printf("Case #%d: X won\n",CS++);
		else if(owin)printf("Case #%d: O won\n",CS++);
		else if(tot>0)printf("Case #%d: Game has not completed\n",CS++);
		else printf("Case #%d: Draw\n",CS++);
	}
	return 0;
}
/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

*/
