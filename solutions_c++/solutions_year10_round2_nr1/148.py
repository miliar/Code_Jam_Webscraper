#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Dir
{
	string name;
	vector<Dir> child;

	Dir(string s="")
	{
		name=s;
	}

	int has(string s)
	{
		for (int i=0;i<(int)child.size();i++)
			if (child[i].name==s)
				return i;
		return -1;
	}
} root;

vector<string> parse(string path)
{
	vector<string> res;
	path.erase(0,1);
	path+="/";
	string cur="";
	for (int i=0;i<(int)path.length();i++)
	{
		if (path[i]=='/')
		{
			res.push_back(cur);
			cur="";
		} else
		{
			cur+=path[i];
		}
	}
	return res;
}

int add(vector<string> all)
{
	int cnt=0;
	Dir* cur=&root;
	for (int i=0;i<(int)all.size();i++)
	{
		int buf=cur->has(all[i]);
		if (buf==-1)
		{
			cur->child.push_back(Dir(all[i]));
			buf=cur->child.size()-1;
			++cnt;
		}
		cur=&cur->child[buf];
	}
	return cnt;
}

char buf[10000];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	scanf("%d\n",&T);
	for (int test=1;test<=T;test++)
	{
		int n,m;
		scanf("%d%d\n",&n,&m);
		root.child.clear();

		for (int i=0;i<n;i++)
		{
			gets(buf);
			add(parse(string(buf)));
		}

		int res=0;
		for (int i=0;i<m;i++)
		{
			gets(buf);
			res+=add(parse(string(buf)));
		}
		printf("Case #%d: %d\n",test,res);
	}
	return 0;
}