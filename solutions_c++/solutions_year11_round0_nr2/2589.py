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

int com[26][26];
int del[26][26];
vector <char> list;
int main()
{
	 freopen("C:\\Users\\tkdsheep\\Desktop\\out.txt","w",stdout);
	int cases=1;
	int repeat,i,j,m,n;
	char x,y,z;
	cin>>repeat;
	while(repeat--)
	{
		printf("Case #%d: ",cases++);
		memset(com,-1,sizeof(com));
		memset(del,0,sizeof(del));
		list.clear();
		cin>>m;
		while(m--)
		{
			cin>>x>>y>>z;
			com[x-'A'][y-'A']=z-'A';
			com[y-'A'][x-'A']=z-'A';

		}
		cin>>n;
		while(n--)
		{
			cin>>x>>y;
			del[x-'A'][y-'A']=del[y-'A'][x-'A']=1;
		}
		cin>>m;
		while(m--)
		{
			cin>>x;
			//cout<<x<<endl;
			if(list.empty())
			{
				list.push_back(x);
				continue;
			}
			if(com[list[list.size()-1]-'A'][x-'A']!=-1)
			{
				list[list.size()-1]=com[list[list.size()-1]-'A'][x-'A']+'A';
				continue;
			}

			for(i=0;i<list.size();i++)
			{
				if(del[list[i]-'A'][x-'A'])
				{
					list.clear();
					break;
				}
			}

			
			if(!list.empty())
				list.push_back(x);
		}
		cout<<"[";
		for(i=0;i<list.size();i++)
		{
			if(i)
				cout<<", ";
			cout<<list[i];

		}
		cout<<"]"<<endl;

	}
}