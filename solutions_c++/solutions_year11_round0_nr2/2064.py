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

const int maxn = 101;
int good[maxn][maxn];
bool bad[maxn][maxn];
int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t,n,i,j; string s;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		CLR(good,0); CLR(bad,false);
		readn(n); while(n--){ reads(s); good[s[0]][s[1]] = good[s[1]][s[0]] = s[2]; }
		readn(n); while(n--){ reads(s); bad[s[0]][s[1]] = bad[s[1]][s[0]] = true; }
		readn(n); vector<char> v(0); reads(s);
		foo(j,0,s)
		{
			v.push_back(s[j]); if(sz(v) == 1)continue; n = sz(v) - 1;
			if(good[v[n]][v[n-1]] > 0)
				{ char ch = good[v[n]][v[n-1]]; v.resize(n-1); v.push_back(ch); continue; }
			fo(i,0,n)
			{
				if(bad[v[i]][v[n]]){ v.clear(); break; }
			}			
		}
		s = "["; if(sz(v) > 0) s += v[0]; foo(i,1,v){ s += ", "; s += v[i]; } s += "]";
		printf("Case #%d: ",Case);
		cout << s << endl;
	}
	return 0;
} 

