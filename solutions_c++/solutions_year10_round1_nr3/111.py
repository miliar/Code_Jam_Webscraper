#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>

using namespace std;

map<pair<int,int>,bool> T;

bool dfs(int a,int b)
{
	if(a<b) swap(a,b);
	if(b==0) return true;
	if(T.find(make_pair(a,b))!=T.end()) return T[make_pair(a,b)];
	for(int k=a/b;k>0;k--)
		if(!dfs(a-b*k,b))
			return T[make_pair(a,b)]=true;
	return T[make_pair(a,b)]=false;
}

int st[10000001];
int ed[10000001];

void init()
{
	ed[1] = 1;
	ed[2] = 3;
	st[1] = 1;
	st[2] = 2;
	int k=1;
	for(int i=3;i<=10000000;i++)
	{
		while(ed[k+1]<i) k++;
		ed[i] = i + k;
		st[i] = k+1;
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int ntest;
	init();
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		long long ans = (a2-a1+1ll)*(b2-b1+1ll);
		for(int a=a1;a<=a2;a++)
		{
			int l = st[a], r = ed[a];
			if(r>=b2) r=b2;
			if(l<b1) l=b1;
			if(l<=r) ans-=(r-l+1);
		}
		printf("Case #%d: %I64d\n",test,ans);
	}
	return 0;
}
