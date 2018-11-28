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

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t; Long pd,pg,su,i,N,mi;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		readl(N); readl(pd); readl(pg);	
		printf("Case #%d: ",Case);
		if((pd>0)&&(pg==0)){ cout << "Broken\n"; continue; }
		if((pd<100)&&(pg==100)){ cout << "Broken\n"; continue; }
		if(pd == pg)if(pd == 0 || pd == 100){ cout << "Possible\n"; continue; }
		mi = 100; if(N < 100)mi = N;
		fo(i,1,mi+1)
		{
			su = (i*pd); if(su % 100 != 0)continue;
			cout << "Possible\n"; break;
		}
		if(i > mi)cout << "Broken\n";
	}
	return 0;
} 

