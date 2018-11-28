#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <map>
using namespace std;

map<string,bool> maps;

int m,n;

void add(string s)
{
	s+="/";
	int sn=s.size();
	for(int i=1;i<sn;i++)
	{
		if(s[i]!='/')
			continue;
		maps[s.substr(0,i)]=true;
	}
}
int test(string s)
{
	s+="/";
	int ret=0;
	int sn=s.size();
	for(int i=1;i<sn;i++)
	{
		if(s[i]!='/')
			continue;
		if(maps.find(s.substr(0,i))==maps.end())
		{
			ret++;
			maps[s.substr(0,i)]=true;
		}
	}
	return ret;
}
void solve()
{
	cin>>n>>m;
	string str;
	maps.clear();
	for(int i=0;i<n;i++)
	{
		cin>>str;
		add(str);
		//cout<<str<<endl;
	}
	int cnt=0;
	for(int i=0;i<m;i++)
	{
		cin>>str;
		cnt+=test(str);
		//cout<<str<<endl;
	}
	printf("%d\n",cnt);
	return;
}
int main()
{
	freopen("d://out.txt","w",stdout);
	int cs;
	cin>>cs;
	for(int ii=1;ii<=cs;ii++)
	{
		printf("Case #%d: ",ii);
		solve();
	}
	return 0;
}