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

vector<int> v,A;
Long getv(Long t,int L)
{
	A.clear(); int i,mi; Long su;
	foo(i,0,v)
	{
		if( t < (v[i]*2) ){ A.push_back(v[i] - ((int)(t/2))); i++; break; }
		t -= (v[i]*2);
	}
	foo(i,i,v)A.push_back(v[i]);
	sort(li(A)); reverse(li(A));
	mi = min(L,sz(A));
	fo(i,0,mi)su += A[i];
	return su;
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,tt,L,n,m,i,j; Long tmp,su;
	scanf("%d",&tt);
	fo(Case,1,tt+1)
	{		
		printf("Case #%d: ",Case); su = 0;
		readn(L); readl(tmp); readn(n); readn(m); v.resize(n); A.resize(m);
		foo(i,0,A)readn(A[i]); j = 0; foo(i,0,v){ v[i] = A[j]; su += A[j]; j++; j%=m; }
		su *= 2; if(tmp >= su){ L = 0; tmp = inf; }
		if(L > 0)su -= getv(tmp,L);
		printf("%I64d",su);		
		cout << endl;
	}
	return 0;
} 

