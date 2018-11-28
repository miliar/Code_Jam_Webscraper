#include "stdafx.h"
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
#include <iostream>
#define PI 3.14159265358979323846264338327950288
#define _clr(a,b) memset(a,b,sizeof(a))
template<class T> T _abs(T a)
{ if(a<0) return -a;return a;}
template<class T> void get_min(T& a,T b)
{ if(a>b) a=b;}
template<class T> void get_max(T& a,T b)
{ if(a<b) a=b;}
using namespace std;
int M,N;
vector<string> CheckPath(char path[])
{
	vector<string> ans;
	for(int i=1;;i++)
	{
		if(path[i]=='/')
		{
			path[i]=0;
			ans.push_back(path);
			path[i]='/';
		}
		else if(path[i]==0)
		{
			ans.push_back(path);
			break;
		}
	}
	return ans;
}
int main()
{
	//freopen("e:\\1.in","r",stdin);
	
	//freopen("e:\\A-small-attempt1.in","r",stdin);
	freopen("e:\\A-large.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		char tmp[105];
		int ans=0;
		vector<string> dic;
		printf("Case #%d: ",t);
		scanf("%d%d",&M,&N);
		for(int i=0;i<M;i++)
		{
			scanf("%s",tmp);
			vector<string> k=CheckPath(tmp);
			for(int j=0;j<k.size();j++) dic.push_back(k[j]);
		}
		for(int i=0;i<N;i++)
		{
			scanf("%s",tmp);
			vector<string> pp=CheckPath(tmp);
			for(int j=0;j<pp.size();j++)
			{
				int k;
				if(dic.size()>0)
				{
					for(k=0;k<dic.size();k++)
					{
						if(dic[k]==pp[j]) break;
					}
					if(k==dic.size()) 
					{
						ans++;
						dic.push_back(pp[j]);
					}
				}
				else
				{
					ans++;
					dic.push_back(pp[j]);
				}
				
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
