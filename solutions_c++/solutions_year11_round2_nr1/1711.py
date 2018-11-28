#include "stdafx.h"

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector>

using namespace std; 

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
//typedef long long Long;
typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; } 
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

const int maxn = 105;
double Win[maxn],Total[maxn];
double v1[maxn],v2[maxn],v3[maxn];
vector<string> g;
void call1()
{
	int i,j;
	foo(i,0,g)
	{
		double w=0,t=0;
		foo(j,0,g[i])
		{ 
			if(g[i][j] == '.')continue; t = t + 1; 
			if(g[i][j] == '1')w = w + 1;
		}
		v1[i] = w/t;
		Win[i] = w; Total[i] = t;
	}
}
void call2()
{
	int i,j;
	foo(i,0,g)
	{
		double w=0,t=0;
		foo(j,0,g[i])
		{ 
			if(g[i][j] == '.')continue; t = t + 1; 
			int extra = 0; if(g[i][j] == '0')extra = 1;
			w = w + ((Win[j]-extra)/(Total[j]-1));
		}
		v2[i] = w/t;
	}
}
void call3()
{
	int i,j;
	foo(i,0,g)
	{
		double w=0,t=0;
		foo(j,0,g[i])
		{ 
			if(g[i][j] == '.')continue; t = t + 1; 
			w = w + v2[j];
		}
		v3[i] = w/t;
	}
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t,n,i;
	
	scanf("%d",&t);
	fo(Case,1,t+1)
	{		
		printf("Case #%d:\n",Case);
		readn(n);  g.resize(n); foo(i,0,g)reads(g[i]);
		call1(); call2(); call3(); 
		foo(i,0,g)
		{
			double su = (0.25*v1[i]) + (0.50*v2[i]) + (0.25*v3[i]);
			printf("%.9lf\n",su);
		}
	}
	return 0;
} 

