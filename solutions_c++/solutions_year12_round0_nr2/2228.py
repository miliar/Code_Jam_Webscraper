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
int f[maxn][maxn];
int A[maxn][2];
vector<int> v;

void init(int n)
{
	int i,j,m = n/3,r = min(1,n%3); 
	A[n][0] = (m+r); A[n][1] = -1; r = n%3;
	if((n < 2) || (n > 28))return;
	if(r == 2) A[n][1] = (m+2);
	else A[n][1] = (m+1);
}

int memo(int pos,int rim,int p)
{
	int &res = f[pos][rim],val; if(res != -1)return res;
	res = -inf;
	if(pos >= sz(v))
	{
		if(rim == 0)return res = 0; return res;
	}
	if(rim > 0)if(A[v[pos]][1] >= 0)
	{
		val = memo(pos+1,rim-1,p);
		if(val >= 0)res = max(res,val+(A[v[pos]][1] >= p));
	}
	val = memo(pos+1,rim,p);
	if(val >= 0)res = max(res,val+(A[v[pos]][0] >= p));
	return res; 
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t,rim,i,n,p;
	fo(i,0,31)init(i);
	scanf("%d",&t);
	fo(Case,1,t+1)
	{		
		CLR(f,-1); cin >> n >> rim >> p; v.resize(n); foo(i,0,v)cin >> v[i];
		printf("Case #%d: ",Case);
		cout << memo(0,rim,p) << endl;
	}
	return 0;
} 

