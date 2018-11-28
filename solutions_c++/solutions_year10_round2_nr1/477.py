#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdio>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<deque>
#include<cstdlib>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const int L = 100010;

int n,m,trie_sum;
string ats[L];

struct TRIE
{
	map<string,int>next;
	bool end;
}trie[L];

void trie_ins(string *now,int len)
{
	int pnt,i;
	pnt=1,i=1;
	while(i<=len)
	{
		if(trie[pnt].next.find(now[i])!=trie[pnt].next.end())
			pnt=trie[pnt].next[now[i]];
		else
		{
			trie[pnt].next[now[i]]=++trie_sum;
			pnt=trie_sum;
		}
		i++;
	}
	trie[pnt].end=true;
}

void myin()
{
	int i,j,k,tn,ans;
	string ss;
	for(i=1;i<=trie_sum;i++)
	{
		trie[i].next.clear();
		trie[i].end=false;
	}
	cin>>n>>m;
	trie_sum=1;
	for(i=0;i<n;i++)
	{
		cin>>ss;
		tn=0;
		for(j=1;j<ss.length();j=k+1)
		{
			for(k=j;k<ss.length()&&ss[k]!='/';k++){}
			ats[++tn]=ss.substr(j,k-j);
		}
		trie_ins(ats,tn);
	}
	ans=trie_sum;

	for(i=0;i<m;i++)
	{
		cin>>ss;
		tn=0;
		for(j=1;j<ss.length();j=k+1)
		{
			for(k=j;k<ss.length()&&ss[k]!='/';k++){}
			ats[++tn]=ss.substr(j,k-j);
		}
		trie_ins(ats,tn);
	}

	cout<<trie_sum-ans<<endl;
}

int main()
{
	freopen("t1.in","r",stdin);
	freopen("t1.out","w",stdout);
	int i,tests;
	cin>>tests;
	trie_sum=1;
	for(i=1;i<=tests;i++)
	{
		cout<<"Case #"<<i<<": ";
		myin();
	}
return 0;
}