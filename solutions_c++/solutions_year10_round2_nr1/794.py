#include<math.h> 
#include "stdafx.h"
#include<ctype.h>
#include<stdlib.h> 
#include<stack>
#include<queue> 
#include<list>
#include<map>

#include<string.h> 
#include<algorithm> 
#include<iostream>
#include<sstream> 
#include<vector> 
#include<string> 

using namespace std; 

#define vi vector<int>
#define vd vector<double>
#define vs vector<string>

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) for(i=j;i<(int)v.size();++i)
#define Foo(i,j,v) for(i=(int)v.size()-1;i>=j;--i)
#define li(v) v.begin(),v.end()
#define sz(v) (int)v.size()
#define co continue;
#define re return
#define inf 1000005

#define pi (2*acos(0))

typedef __int64 Long;
//typedef long long Long;

map<string,bool> mp;
char tmp[inf];
string s;
int main()
{
	freopen("c://Codejam//A.in","r",stdin);
	freopen("c://Codejam//A.out","w",stdout);
	int T,t,N,M,su,i,j;
	scanf("%d",&T);
	fo(t,1,T+1)
	{
		scanf("%d%d",&N,&M); mp.clear(); s = ""; su = 0;
		fo(i,0,N){ scanf("%s",tmp); s = tmp; mp[s]=true; }
		fo(i,0,M)
		{
			s = ""; scanf("%s",tmp); s = tmp; 
			while(sz(s)>0)
			{
				if(mp.count(s)==1)break;
				su++; mp[s]=true;
				Foo(j,0,s)if(s[j]=='/'){ s.resize(j); break; }
			}
		}
		printf("Case #%d: %d\n",t,su);
	}
} 

