#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int N=10;
char adj[N][N];
bool no_end,X_win,O_win;
void judge(int type,int ind)
{
	bool x=0,o=0,em=0;
	if(type==0)
	{
		for(int i=0;i<4;i++) 
		{
			if(adj[ind][i]=='X') x=1;
			else if(adj[ind][i]=='O') o=1;
			else if(adj[ind][i]=='.') em=1;
		}
	}
	else if(type==1)
	{
		for(int i=0;i<4;i++)
		{
			if(adj[i][ind]=='X') x=1;
			else if(adj[i][ind]=='O') o=1;
			else if(adj[i][ind]=='.') em=1;
		}
	}
	else if(type==2)
	{
		for(int i=0;i<4;i++) 
		{
			if(adj[i][i]=='X') x=1;
			else if(adj[i][i]=='O') o=1;
			else if(adj[i][i]=='.') em=1;
		}
	}
	else 
	{
		for(int i=0;i<4;i++) 
		{
			if(adj[3-i][i]=='X') x=1;
			else if(adj[3-i][i]=='O') o=1;
			else if(adj[3-i][i]=='.') em=1;
		}
	}
	if(em==1) o=0,x=0;
	if(!x&&o) O_win=1;
	if(!o&&x) X_win=1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,t_cnt=0;
	scanf("%d",&t);
	while(t--)
	{
		no_end=0,X_win=0,O_win=0;
		for(int i=0;i<4;i++) 
		{
			scanf("%s",adj[i]);
			for(int j=0;j<4;j++) if(adj[i][j]=='.') no_end=1;
			judge(0,i);
		}
		for(int i=0;i<4;i++) judge(1,i);
		judge(2,-1);	judge(3,-1);
	
		printf("Case #%d: ",++t_cnt);
		if(X_win) puts("X won");
		else if(O_win) puts("O won");
		else if(no_end) puts("Game has not completed");
		else puts("Draw");
	}
	return 0;
}
