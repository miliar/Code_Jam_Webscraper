// a1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<memory>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
int t[101];
struct node
{
	int average;
	int remains;
	int max;
};
struct node mynode[101];
bool com(node a,node b)
{ return a.max>b.max; }
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("b.txt","w",stdout);
	int T,N,S,p;
	cin>>T;	
	
	for(int cases=1;cases<=T;cases++)
	{
		memset(t,0,101);
		
		cin>>N;
		if(N!=0)
		{
			cin>>S>>p;
			int i,num=0;
			memset(mynode,0,101);
			for(i=0;i<N;i++)
			{			
				cin>>t[i];
				mynode[i].average=t[i]/3;
				mynode[i].remains=t[i]%3;
				if(mynode[i].remains==0)
				{ mynode[i].max=mynode[i].average; }
				else
				{ mynode[i].max=mynode[i].average+1; }
			}
			sort(mynode,mynode+N,com);
			if(p==0)
			{ num=N;}
			else
			{
				for(i=0;i<N;i++)
				{
					if(mynode[i].max>=p)
					{ num++;}
					else
					{ break; }
				}
				for(int j=i;j<N;j++)
				{
					if(S>0&&mynode[j].remains!=1&&t[j]!=0)
					{
						if(p-mynode[j].max>1)
						{ break; }
						else
						{ num++; S--;}
					}
				}		
			}
			cout<<"Case #"<<cases<<": "<<num<<endl;		
		}
		else
		{
			cout<<"Case #"<<cases<<": "<<0<<endl;
		}
	}
	return 0;
}

