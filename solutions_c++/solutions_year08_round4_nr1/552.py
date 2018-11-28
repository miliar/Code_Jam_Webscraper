/*
ID: ferromr1
PROG:
LANG: C++
*/
#include<cstdio>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<algorithm>
#include<numeric>
#include<cstdlib>
#include<cmath>
#include<set>
#include<map>
#include<ctime>
#include<utility>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define clr(qq) memset((qq),0,sizeof(qq))
#define fill(qq) memset((qq),0x3F,sizeof(qq))
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep2(i,a,b) for(int (i)=(int)(a);i<(int)(b);i++)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define rint(qq) int(floor(qq+0.5))
#define sqr(qq) ((qq) * (qq))
#define ll long long
#define inf 999999999
#define fi first
#define se second
#define MX 200505

int t,n,v;
bool C[MX],LIST[MX];
int G[MX];
int V[MX];
int mem[MX][2];

void urob(int kde)
{
	if (V[kde]!=-1)
	{
		LIST[kde]=1;
		return;
	}
	urob(kde*2);
	urob(kde*2+1);
	if (G[kde]==1) V[kde]=V[kde*2]&&V[kde*2+1];
	else V[kde]=V[kde*2]||V[kde*2+1];
}

int prerob(int kde,int val)
{
	if (mem[kde][val]!=-1) return mem[kde][val];
	if (LIST[kde])
	{
		if (V[kde]!=val) return -2;
		return 0;
	}
	if (V[kde]==val) return 0;
	int res=-2;
	// AND
	{
		if (val==1)
		{
			int pom=prerob(kde*2,1);
			int pom2=prerob(kde*2+1,1);
			if (pom==-2||pom2==-2) res=-2;
			else res=pom+pom2;
		}
		else
		{
			int pom=prerob(kde*2,0);
			int pom2=prerob(kde*2+1,0);
			int ans=inf;
			if (pom!=-2) ans=pom;
			if (pom2!=-2) ans=min(ans,pom2);
			if (ans==inf) res=-2;
			else res=ans;
		}
	}
	int res2=res;
 	// OR
	{
		if (val==1)
		{
			int pom=prerob(kde*2,1);
			int pom2=prerob(kde*2+1,1);
			int ans=inf;
			if (pom!=-2) ans=pom;
			if (pom2!=-2) ans=min(ans,pom2);
			if (ans==inf) res=-2;
			else res=ans;
		}
		else
		{
			int pom=prerob(kde*2,0);
			int pom2=prerob(kde*2+1,0);
			if (pom==-2||pom2==-2) res=-2;
			else res=pom+pom2;
		}
	}
	swap(res,res2);
	if (res!=-2)
	{
		if (G[kde]!=1)
		{
			if (C[kde]) res++; else res=-2;
		}
	}
	if (res2!=-2)
	{
		if (G[kde]==1)
		{
			if (C[kde]) res2++; else res2=-2;
		}
	}
	if (res2!=-2)
	{
		if (res==-2) res=res2;
		else res=min(res,res2);
	}
	return mem[kde][val]=res;
}

int main ()
{
	scanf("%d",&t);
	rep(cases,t)
	{
		clr(LIST);
		clr(C);
		memset(V,-1,sizeof(V));
		printf("Case #%d: ",cases+1);
		cin>>n>>v;
		rep(i,(n-1)/2)
		{
			int a,b;
			cin>>a>>b;
			C[i+1]=b;
			G[i+1]=a;
		}
		rep(i,(n+1)/2)
		{
			int a;
			cin>>a;
			V[(n-1)/2+i+1]=a;
		}
		urob(1);
		memset(mem,-1,sizeof(mem));
		int ret=0;
		if (V[1]!=v)
		{
			ret=prerob(1,v);
		}
		if (ret==-2) puts("IMPOSSIBLE");
		else printf("%d\n",ret);
	}
	return 0;
}
