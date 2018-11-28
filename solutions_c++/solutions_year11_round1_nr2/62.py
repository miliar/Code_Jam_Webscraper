#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;
typedef unsigned long long LLU;
typedef long long LL;
typedef pair<int,int> pii;
#define MP make_pair
const int INF=99999999;
const double PI=3.1415926535897932384626;
const double EPS=1E-11;
vector<string> twords;
map<string,int> tmap;
vector<string> words[11];
bool contains(string& s,char c)
{
	for(int i=0;i<s.size();i++)
		if(c==s[i])
			return true;
	return false;
}
string mod(const string& s,const string& p,char c)
{
	string t="";
	for(int i=0;i<s.size();i++)
	{
		if(c==s[i])
			t+=c;
		else
			t+=p[i];
	}
	return t;
}
pii process(int len,vector<string>& w,char str[100])
{
	int *dist=new int[w.size()];
	map<string,vector<int> > p,p2;
	map<string,vector<int> >::iterator it;
	{
		string temp="";
		for(int i=0;i<len;i++)
			temp+="_";
		//printf("%d\n",w.size());
		//fflush(stdout);
		for(int i=0;i<w.size();i++)
		{
			p[temp].push_back(i);
			dist[i]=0;
		}
	}
	for(int i=0;i<26;i++)
	{
		p2.clear();
		char c=str[i];
		for(it=p.begin();it!=p.end();it++)
		{
			//printf("pattern: %s\n",it->first.c_str());
			vector<int>& v=it->second;
			bool found=false;
			for(int j=0;j<v.size();j++)
			{
				//printf("%s\n",w[v[j]].c_str());
				if(contains(w[v[j]],c))
				{
					found=true;
					//break;
				}
			}
			if(found)
			{
				for(int j=0;j<v.size();j++)
				{
					if(contains(w[v[j]],c))
					{
						//printf("%s\n",w[v[j]].c_str());
						//fflush(stdout);
						string temp=mod(w[v[j]],it->first,c);
						//printf("%s\n",temp.c_str());
						//fflush(stdout);
						p2[temp].push_back(v[j]);
					}
					else
					{
						dist[v[j]]++;
						p2[it->first].push_back(v[j]);
					}
				}
			}
			else
			{
				for(int j=0;j<v.size();j++)
					p2[it->first].push_back(v[j]);
			}
		}
		swap(p,p2);
	}
	int best=-1,besti=-1;
	for(int i=0;i<w.size();i++)
	{
		//printf("%s %d\n",w[i].c_str(),dist[i]);
		if(dist[i]>best)
		{
			best=dist[i];
			besti=i;
		}
	}
	delete[] dist;
	if(besti==-1)
	{
		return make_pair(-1,-1);
	}
	return make_pair(best,tmap[w[besti]]);
}
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	char str[100];
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		twords.clear();
		for(int i=0;i<=10;i++)
			words[i].clear();
		tmap.clear();
		
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
		{
			scanf("%s",str);
			twords.push_back((string)str);
			tmap[(string)str]=i;
			//printf("len %d\n",strlen(str));
			words[strlen(str)].push_back((string)str);
		}
		printf("Case #%d:",tn);
		fflush(stdout);
		for(int i=0;i<m;i++)
		{
			scanf("%s",str);
			pii best=make_pair(-999,-999);
			for(int len=0;len<=10;len++)
			{
				pii t=process(len,words[len],str);
				if(t.first>best.first)
					best=t;
				else if(t.first==best.first && t.second<best.second)
					best=t;
			}
			printf(" %s",twords[best.second].c_str());
		}
		putchar('\n');
	}
}
