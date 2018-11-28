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

int button[2],wait[2];
int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t,su = 0,n,k,b1,b2,mi,newbutton; string s;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		printf("Case #%d: ",Case); 
		su = 0; wait[0] = wait[1] = 0; button[0] = button[1] = 1; readn(k);
		while(k--)
		{
			reads(s); readn(n); newbutton = n; b1 = (s[0] == 'B') ? 1 : 0; b2 = (b1+1)%2;
			n = abs(button[b1] - n); mi = min(wait[b1], n); 
			n -= mi; n++; su += n; wait[b1] = 0; wait[b2] += n; button[b1] = newbutton;
		}		
		cout << su << endl;
	}
	return 0;
} 

