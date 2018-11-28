

#include "stdafx.h"
#include <algorithm>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include <map>
#include<vector>
using namespace std;

int n,m;

map<string,int> hash;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		hash.clear();
		string tp;
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;++i)
		{
			cin>>tp;
			if(hash.find(tp) == hash.end())
			{
				hash.insert(map<string,int> ::value_type(tp,1));
			}
		}
		for(int i=1;i<=m;++i)
		{
			cin>>tp;
			if(hash.find(tp) == hash.end())
			{
				hash.insert(map<string,int> ::value_type(tp,1));
				int end = tp.length()-1;
				while(end > 0) 
				{
					while(tp[end] !='/')
					{
						tp.erase(end);
						--end;
					}
					tp.erase(end);
					if(!(tp == ""))
					{
						--end;
						hash.insert(map<string,int> ::value_type(tp,1));
					}
				}
			}
		}
		printf("Case #%d: %d\n",x,hash.size()-n);
	}
	return 0;
}