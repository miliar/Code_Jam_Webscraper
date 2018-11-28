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

//./\..
//.\/
vector<string> g;
bool ok(int n,int m)
{
	int i,j; n--; m--;
	fo(i,0,n)fo(j,0,m)
	{
		if(g[i][j] != '#')continue;
		if(g[i+1][j] != '#')return false; 
		if(g[i][j+1] != '#')return false;
		if(g[i+1][j+1] != '#')return false;
		g[i][j] = '/'; g[i][j+1] = '\\'; g[i+1][j] = '\\'; g[i+1][j+1] = '/';
	}
	foo(i,0,g)foo(j,0,g[i])if(g[i][j] == '#')return false;
	return true;
}
int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t,n,m,i;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{		
		printf("Case #%d:\n",Case);
		readn(n); readn(m); g.resize(n); foo(i,0,g)reads(g[i]);
		if(!ok(n,m))cout << "Impossible\n";
		else
		{
			foo(i,0,g)cout<<g[i]<<endl;
			
		}
		//cout << endl;
	}
	return 0;
} 

