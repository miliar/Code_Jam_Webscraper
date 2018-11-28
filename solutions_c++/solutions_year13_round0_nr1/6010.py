#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<stack>
#include<queue>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<assert.h>
#include<math.h>
#include<climits>
#include <iomanip> //forsetw()
using namespace std;


char * const ans[4]={"X won","O won","Draw","Game has not completed"};
char board[4][6];
bool state(char player)
{
	int i,x,y;
	//for rows
	for(i=0;i<4;i++)
	{
		int c=0;
		for(x=0;x<4;x++)
			if(board[i][x]==player || board[i][x]=='T')
				c++;
		if(c==4)
			return true;		
	}
	//for columns
	for(i=0;i<4;i++)
	{
		int c=0;
		for(x=0;x<4;x++)
			if(board[x][i]==player || board[x][i]=='T')
				c++;
		if(c==4)
			return true;		
	}	
	int c=0;
	for(x=0;x<4;x++)
		if(board[x][x]==player || board[x][x]=='T')
			c++;	
	if(c==4)
		return true;
	c=0;	
	for(x=0;x<4;x++)
		if(board[x][4-x-1]==player || board[x][4-x-1]=='T')
			c++;	
	if(c==4)
		return true;
	return false;			
}
bool draw()
{
	int x,y;
	for(x=0;x<4;x++)
		for(y=0;y<4;y++)
			if(board[x][y]=='.')
				return false;
	return true;			
}
char *solve()
{
	if(state('X'))
	{
		
		return ans[0];
	}
	if(state('O'))
	{
		return ans[1];
	}
	if(draw())
	{
		return ans[2];
	}
	return ans[3];
}
int main(int argc,char **argv)
{
	int t,i,x;
	//freopen("input.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		for(x=0;x<4;x++)
		{
			if(i!=0 && x==0)
				while(getchar()!='\n');
			while(getchar()!='\n');
			fgets(board[x],5,stdin);
			
		}
		printf("Case #%d: %s\n",i+1,solve());	
	}
	
	return 0;
}

