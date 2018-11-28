// codeforces.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
//#include <map>
#include <queue>
#include <vector>
#include <stdlib.h>
#include <set>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#define MAX 2100000000
#define eps 1e-9
using namespace std;

struct node
{
	char ch;
	int index,step;
	int x,y;
};
int dp[101][101][101];
node a[101];


int main()
{
	 freopen("C:\\Users\\tkdsheep\\Desktop\\out.txt","w",stdout);
	int cases=1;
	int d[3]={-1,0,1};
	int repeat,i,j,k,m;
	cin>>repeat;
	node ss,tt;
	while(repeat--)
	{
		cin>>m;
		for(i=0;i<m;i++)
			cin>>a[i].ch>>a[i].index;
		cout<<"Case #"<<cases++<<": "; 
		queue <node> q;
		memset(dp,-1,sizeof(dp));
		ss.x=1;
		ss.y=1;
		ss.step=0;
		ss.index=0;
		while(!q.empty())
			q.pop();
		dp[1][1][0]=0;
		q.push(ss);
		while(!q.empty())
		{
			ss=q.front();
			q.pop();
			//cout<<ss.x<<" "<<ss.y<<" "<<ss.index<<" "<<ss.step<<endl;
			if(ss.index==m)
			{
				cout<<ss.step<<endl;
				break;
			}
			if(a[ss.index].ch=='O'&&a[ss.index].index==ss.x)//x push
			{
				tt.x=ss.x;
				tt.step=ss.step+1;
				tt.index=ss.index+1;
				for(i=0;i<3;i++)
				{
					tt.y=ss.y+d[i];
					if(tt.y<1||tt.y>100)
						continue;
					if(dp[tt.x][tt.y][tt.index]==-1)
					{
						dp[tt.x][tt.y][tt.index]=tt.step;
						q.push(tt);
					}
				}
			}

			if(a[ss.index].ch=='B'&&a[ss.index].index==ss.y)//y push
			{
				tt.y=ss.y;
				tt.step=ss.step+1;
				tt.index=ss.index+1;
				for(i=0;i<3;i++)
				{
					tt.x=ss.x+d[i];
					if(tt.x<0||tt.x>100)
						continue;
					if(dp[tt.x][tt.y][tt.index]==-1)
					{
						dp[tt.x][tt.y][tt.index]=tt.step;
						q.push(tt);
					}
				}
			}


			for(i=0;i<3;i++)
				for(j=0;j<3;j++)
				{
					tt.x=ss.x+d[i];
					tt.y=ss.y+d[j];
					if(tt.x<1||tt.x>100||tt.y<1||tt.y>100)
						continue;
					tt.step=ss.step+1;
					tt.index=ss.index;
					if(dp[tt.x][tt.y][tt.index]==-1)
					{
						dp[tt.x][tt.y][tt.index]=tt.step;
						q.push(tt);
					}
				}


		}

		





	}
}