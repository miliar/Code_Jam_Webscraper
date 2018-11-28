
#include "StdAfx.h"
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <algorithm>
using namespace std;


string word[10001];
bool use[10001];
bool mark[10001][26];
string list[101];
int n,m;
bool on[26];
int gao(int index,string s,string t)
{
	memset(on,0,sizeof(on));
	string x=s;
	int i,j,k;
	for(i=0;i<x.size();i++)
		x[i]=' ';
	int ans=0;
	int tmp=0;
	//cout<<s<<" "<<t<<endl;
	for(i=0;i<t.size();i++)
	{
		
		if(mark[index][t[i]-'a'])//right
		{
			on[t[i]-'a']=true;
			for(j=0;j<s.size();j++)
				if(s[j]==t[i])
				{
					tmp++;
					x[j]=t[i];
				}
				if(tmp==s.size())
					return ans;
			continue;

		}
		bool ff=false;
		for(j=1;j<=n;j++)
		{
			if(use[j])
				continue;
			
			//cout<<word[j].size()<<" "<<s.size()<<endl;
			if(word[j].size()!=s.size())
				continue;
			if(!mark[j][t[i]-'a'])
				continue;
			
			for(k=0;k<s.size();k++)
			{
				if(x[k]==' ')
				{
					if(on[word[j][k]-'a'])
						break;
					continue;
				}
				if(word[j][k]!=x[k])
					break;
			}
			//cout<<k<<endl;
			if(k<s.size())
				continue;
			//will guess
			//cout<<t[i];
			ff=true;
			

		}
		
		if(ff)
			ans++;
		for(j=1;j<=n;j++)
		{
			if(mark[j][t[i]-'a'])
				use[j]=true;
		}


			

	}
	//cout<<endl<<x<<" "<<ans<<endl;
	return ans;

}
int main()
{
	freopen("out.txt","w",stdout);
	int cases=1;
	int repeat,i,j,index,mn;
	cin>>repeat;
	while(repeat--)
	{
		
		cin>>n>>m;
		for(i=1;i<=n;i++)
		{
			cin>>word[i];
		}
		for(i=1;i<=m;i++)
			cin>>list[i];
		memset(mark,0,sizeof(mark));
		for(i=1;i<=n;i++)
		{
			for(j=0;j<word[i].size();j++)
				mark[i][word[i][j]-'a']=true;
		}
		printf("Case #%d:",cases++);
		for(i=1;i<=m;i++)
		{
			
			mn=-1;
			index=-1;
			for(j=1;j<=n;j++)
			{
				memset(use,0,sizeof(use));
				
				int tmp=gao(j,word[j],list[i]);
				//cout<<tmp<<endl;
				if(tmp>mn)
				{
					mn=tmp;
					index=j;
				}

			}
			cout<<" "<<word[index];


		}
		cout<<endl;
	}


}
// Powered by FileEdit
// Powered by TZTester 1.01 [25-Feb-2003]
// Powered by CodeProcessor
