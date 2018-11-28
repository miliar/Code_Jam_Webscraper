#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
//#include <cmath>
//#include "lcgrand.c"

using namespace std;

const int nmax=20000;

int N;
map<string,int>children[nmax];

int addDir(int cur,string&dirName)
{
	if (children[cur].find(dirName)==children[cur].end())
	{
		children[N].clear();
		children[cur][dirName]=N++;
		return 1;
	}
	return 0;
}

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,n,m,i,j,cur,ans;
	char s[200];
	string q;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n>>m;
		gets(s);
		N=1;
		children[0].clear();
		ans=0;
		
		for(i=0;i<n;i++)
		{
			gets(s);
			for(j=0;s[j];j++);
			s[j]='/';
			s[j+1]=0;
			q="";
			cur=0;
			for(j=1;s[j];j++)
			{
				if (s[j]=='/')
				{
					addDir(cur,q);
					cur=children[cur][q];
					q="";
				} else q+=s[j];
			}
		}

		while(m--)
		{
			gets(s);
			for(j=0;s[j];j++);
			s[j]='/';
			s[j+1]=0;
			q="";
			cur=0;
			for(j=1;s[j];j++)
			{
				if (s[j]=='/')
				{
					ans+=addDir(cur,q);
					cur=children[cur][q];
					q="";
				} else q+=s[j];
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	

	return 0;
}