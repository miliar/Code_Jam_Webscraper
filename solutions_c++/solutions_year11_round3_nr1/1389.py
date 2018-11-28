// 3A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<memory>
using namespace std;
struct node
{
	int blue;
	int white;
};
int T,R,C;
char piece[52][52];
bool visit[52][52];
void main()
{
	freopen("A-large.in","r",stdin);
	freopen("b.txt","w",stdout);
	cin>>T;
	int caseId,i,j,k;
	for(caseId=1;caseId<=T;caseId++)
	{
		cin>>R>>C;
		node pnode;
		pnode.blue=0;
		pnode.white=0;
		for(i=1;i<=R;i++)
		{
			for(j=1;j<=C;j++)
			{
				cin>>piece[i][j];
				visit[i][j]=false;
				if(piece[i][j]=='#')
					pnode.blue++;
			}
		}
		if(pnode.blue%4!=0)
			cout<<"Case #"<<caseId<<":"<<endl<<"Impossible"<<endl;
		else if(pnode.blue==0)
		{
			cout<<"Case #"<<caseId<<":"<<endl;
			for(i=1;i<=R;i++)
			{
				for(j=1;j<=C;j++)
				{ cout<<piece[i][j]; }
				cout<<endl;
			}
		}
		else
		{
			for(i=1;i<R;i++)
			{
				for(j=1;j<C;j++)
				{
					if(piece[i][j]=='#')
					{
						if(!visit[i][j])
						{
							if(piece[i][j+1]=='#'&&piece[i+1][j]=='#'&&piece[i+1][j+1]=='#'&&!visit[i][j+1]&&!visit[i+1][j]&&!visit[i+1][j+1])
							{ visit[i][j]=true; visit[i][j+1]=true; visit[i+1][j]=true; visit[i+1][j+1]=true; continue; }
							else
							{ cout<<"Case #"<<caseId<<":"<<endl<<"Impossible"<<endl; break; }
						}
					}
				}
				if(j!=C)
					break;
			}
			/*for(i=1;i<=R;i++)
				for(j=1;j<=C;j++)
					visit[i][j]=false;*/
			memset(visit,0,sizeof(visit));
			if(i==R)
			{
				cout<<"Case #"<<caseId<<":"<<endl;
				for(i=1;i<=R;i++)
				{
					
					for(j=1;j<=C;j++)
					{
						if(piece[i][j]=='#'&&!visit[i][j])
						{ 
							piece[i][j]='/'; visit[i][j]=true;
							piece[i][j+1]='\\'; visit[i][j+1]=true;
							piece[i+1][j]='\\'; visit[i+1][j]=true;
							piece[i+1][j+1]='/'; visit[i+1][j+1]=true;
						}
						cout<<piece[i][j];
					}
					cout<<endl;
				}
			}
		}
	}
}