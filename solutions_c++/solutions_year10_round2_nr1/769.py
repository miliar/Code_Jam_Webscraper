//#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

struct TNode
{
	string val;
	vector<TNode> children;
};

void AddPath(string s, 	TNode& r)
{
	if (s=="" || s=="/")
		return;
	int i1=s.find('/');
	string ss=s.substr(i1+1);
	int i2=ss.find('/');
	string st=ss.substr(0, i2);
	string str="";
	if (i2>=0)
		str=ss.substr(i2);

	int index=-1;
	for (int i=0; i<r.children.size(); i++)
		if (r.children[i].val==st)
		{
			index=i;
			break;
		}
	if (index==-1)
	{
		index=r.children.size();
		TNode newnode;
		newnode.val=st;
		r.children.push_back(newnode);
	}
	AddPath(str, r.children[index]);
}

void MkPath(string s, TNode& r, int& c)
{
	if (s=="" || s=="/")
		return;
	int i1=s.find('/');
	string ss=s.substr(i1+1);
	int i2=ss.find('/');
	string st=ss.substr(0, i2);
	string str="";
	if (i2>=0)
		str=ss.substr(i2);

	int index=-1;
	for (int i=0; i<r.children.size(); i++)
		if (r.children[i].val==st)
		{
			index=i;
			break;
		}
	if (index==-1)
	{
		index=r.children.size();
		TNode newnode;
		newnode.val=st;
		r.children.push_back(newnode);
		c++;
	}
	MkPath(str, r.children[index], c);
}

int main()
{
	/*
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	*/
	/*
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	*/	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int testcase;
	scanf("%d", &testcase);
	for (int i=0; i<testcase; i++)
	{
		int n,m;
		scanf("%d%d", &n, &m);
		TNode root;
		root.val="";

		for (int j=0; j<n; j++)
		{
			char* st=new char[100];
			scanf("%s", st);
			string stt(st);
			AddPath(stt,root);
		}

		int count=0;

		for (int j=0; j<m; j++)
		{
			char* st=new char[100];
			scanf("%s", st);
			string stt(st);
			MkPath(stt, root, count);
		}

		printf("Case #%d: %d\n", i+1, count);
	}

	fflush(stdout);

	return 0;
}