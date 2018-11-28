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
	int ave;
	int remain;
	int max1;
};
struct node mynode[101];
bool com(node a,node b)
{ return a.max1>b.max1; }
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("b.txt","w",stdout);
	int T,N,S,p;
	cin>>T;	
	
	for(int caseId=1;caseId<=T;caseId++)
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
				mynode[i].ave=t[i]/3;
				mynode[i].remain=t[i]%3;
				if(mynode[i].remain==0)
				{ mynode[i].max1=mynode[i].ave; }
				else
				{ mynode[i].max1=mynode[i].ave+1; }
			}
			sort(mynode,mynode+N,com);
			if(p==0)
			{ num=N;}
			else
			{
				for(i=0;i<N;i++)
				{
					if(mynode[i].max1>=p)
					{ num++;}
					else
					{ break; }
				}
				for(int j=i;j<N;j++)
				{
					if(S>0&&mynode[j].remain!=1&&t[j]!=0)
					{
						if(p-mynode[j].max1>1)
						{ break; }
						else
						{ num++; S--;}
					}
				}		
			}
			cout<<"Case #"<<caseId<<": "<<num<<endl;		
		}
		else
		{
			cout<<"Case #"<<caseId<<": "<<0<<endl;
		}
	}
	return 0;
}

