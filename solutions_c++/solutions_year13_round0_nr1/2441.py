/*
 * mian.cpp
 *
 *  Created on: 2013-4-13
 *      Author: bu540402
 */
#include<iostream>
using namespace std;
char adj[5][5];
int used[5][5];
int dir[4][2]={{0,1},{1,0},{1,1},{1,-1}};
int owin,xwin;
int cheak(int x,int y)
{
	if(x<0||x>3||y<0||y>3)return 0;
	return 1;
}
int findx(int x,int y)
{
	int xx=x,yy=y;
	for(int i=0;i<4;i++)
	{
		xx=x;yy=y;
		int cnt=0;
		while(adj[xx][yy]=='T'||adj[xx][yy]==adj[x][y])
		{
			cnt++;
			xx=xx+dir[i][0];
			yy=yy+dir[i][1];
			if(!cheak(xx,yy))break;
		}
		if(cnt>=4)return 1;
	}
	return 0;
}
int judge()
{
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	{
		if(adj[i][j]=='X'&&!xwin)
		{
			xwin=findx(i,j);
		}
		if(adj[i][j]=='O'&&!owin)
		{
			owin=findx(i,j);
		}
	}
}
int main()
{
	//freopen("data.in","r",stdin);
	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		int cnt=0;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			cin>>adj[i][j];
			if(adj[i][j]=='.')cnt++;
		}
		owin=xwin=0;
		judge();
		printf("Case #%d: ",cas);
		if(owin&&xwin||!owin&&!xwin&&!cnt)cout<<"Draw"<<endl;
		if(owin&&!xwin)cout<<"O won"<<endl;
		if(!owin&&xwin)cout<<"X won"<<endl;
		if(!owin&&!xwin&&cnt)cout<<"Game has not completed"<<endl;

	}
}
