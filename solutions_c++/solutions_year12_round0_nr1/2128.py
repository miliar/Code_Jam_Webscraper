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

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char s[200];
void doit()
{
	int i; s2 = "";
	foo(i,0,s1)
	{
		if(s1[i] == ' '){ s2 += ' '; continue; }
		if(s[s1[i]] == -1){ s2 += s1[i]; continue; }
		s2 += s[s1[i]];
	}
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int i,k; CLR(s,-1); char ch1,ch2;
	fo(k,'a','z'+1)
	{
		foo(i,0,s1)if(s1[i] == k)
		{
			if(s[k] == -1)s[k] = s2[i];
		}
	}
	fo(k,'a','z'+1)if(s[k] == -1){ ch1 = k; break; }
	fo(k,k+1,'z'+1)if(s[k] == -1){ ch2 = k; break; }
	s[ch1] = ch2; s[ch2] = ch1;

	int Case,t;
	scanf("%d",&t); readln(s1);
	fo(Case,1,t+1)
	{		
		readln(s1); doit();
		printf("Case #%d: ",Case);
		cout << s2;
		cout << endl;
	}
	return 0;
} 

