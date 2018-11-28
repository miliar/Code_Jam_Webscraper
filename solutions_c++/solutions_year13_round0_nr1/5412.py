#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
using namespace std;
#define LL long long
ofstream fout("ap.txt");
char g[10][10];
int solve()	//1:x win;  2:o win; 3:draw 4:Game has...
{
	int i,j,k;
	for(i=0;i<4;i++)
	{
		int x=0,o=0,t=0;
		for(j=0;j<4;j++)
		{
			if(g[i][j]=='X')
				x++;
			else if(g[i][j]=='O')
				o++;
			else if(g[i][j]=='T')
				t++;
		}
		if(x==4||(x==3&&t==1))
			return 1;
		if(o==4||(o==3&&t==1))
			return 2;
	}
	int ok=0;
	for(i=0;i<4;i++)
	{
		int x=0,o=0,t=0;
		for(j=0;j<4;j++)
		{
			if(g[j][i]=='X')
				x++;
			else if(g[j][i]=='O')
				o++;
			else if(g[i][j]=='T')
				t++;
			if(g[i][j]=='.')
				ok=1;
		}
		if(x==4||(x==3&&t==1))
			return 1;
		if(o==4||(o==3&&t==1))
			return 2;
	}
	int x=0,o=0,t=0;
	for(i=0;i<4;i++)
	{			
			if(g[i][i]=='X')
				x++;
			else if(g[i][i]=='O')
				o++;
			else if(g[i][j]=='T')
				t++;
	}
	if(x==4||(x==3&&t==1))
		return 1;
	if(o==4||(o==3&&t==1))
		return 2;

	x=0,o=0,t=0;
	for(i=0;i<4;i++)
	{		
		j=4-i-1;
			if(g[i][j]=='X')
				x++;
			else if(g[i][j]=='O')
				o++;
			else if(g[i][j]=='T')
				t++;
	}
	if(x==4||(x==3&&t==1))
		return 1;
	if(o==4||(o==3&&t==1))
		return 2;
	
	if(ok)
		return 4;
	return 3;
}
int main()
{
	int i,j,k;
	int t,cas;
	cin>>t;
	for(cas=1;cas<=t;cas++)
	{
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%c",&g[i][j]);
			//scanf("%s",g[i]);
		int res=solve();				
		//printf("Case #%d: ");	
		fout<<"Case #"<<cas<<": ";
		if(res==1)
			fout<<"X won\n";
			//printf("X won\n");
		if(res==2)
			fout<<"O won\n";
			//printf("O won\n");
		if(res==3)
			fout<<"Draw\n";
			//printf("Draw\n");
		if(res==4)
			fout<<"Game has not completed\n";
			//printf("Game has not completed\n");
	}
	
	return 0;	
}
