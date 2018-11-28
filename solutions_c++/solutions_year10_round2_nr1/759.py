#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
using namespace std;


typedef struct
{
	bool isnew;
	string name;
	map<string,int> child;
}
tDir;
tDir dirs[11000];
int cdir=0;

vector<string> split(string x)
{
	string tnew = "";
	vector<string> res;
	for(int i=0;i<x.length();i++)
	{
		if(x[i]=='/')
		{
			if(tnew.length()>0)	res.push_back(tnew);
			tnew="";
		}
		else
		{
			tnew += x[i];
		}
	}
	if(tnew.length()>0)	res.push_back(tnew);
	return res;
}
void solve()
{
	int OLD,NEW;
	char strpath[110];
	scanf("%d%d",&OLD,&NEW);
	dirs[0].isnew = false;
	int cold,cnew;
	for(int i=0;i<OLD;i++)
	{
		scanf("%s",strpath);

		vector<string> tpath = split(strpath);

		int p=0;
		for(int j=0;j<tpath.size();j++)
		{
			if(dirs[p].child.find(tpath[j]) == dirs[p].child.end())
			{
				dirs[p].child[tpath[j]] = ++cdir;
				dirs[cdir].isnew = false;
			}
			p = dirs[p].child[tpath[j]];
		}
	}
	cold = cdir;

	for(int i=0;i<NEW;i++)
	{
		scanf("%s",strpath);

		vector<string> tpath = split(strpath);

		int p=0;
		for(int j=0;j<tpath.size();j++)
		{
			if(dirs[p].child.find(tpath[j]) == dirs[p].child.end())
			{
				dirs[p].child[tpath[j]] = ++cdir;
				dirs[cdir].isnew = true;
			}
			p = dirs[p].child[tpath[j]];
		}
	}
	cnew = cdir;

	printf("%d\n",cnew-cold);
}
int main()
{
	int Ti,T;
	scanf("%d",&T);
	for(Ti = 1; Ti <= T; Ti++)
	{
		printf("Case #%d: ",Ti);
		solve();
		for(int i=0;i<=cdir;i++)
			dirs[i].child.clear();
		cdir = 0;
	}
}
