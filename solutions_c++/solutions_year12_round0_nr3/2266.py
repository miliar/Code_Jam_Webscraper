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

template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();} 
int toInt(string s){int n; sscanf(s.c_str(),"%d",&n); return n; }

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; } 
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

const int maxn = 2000000 + 10;
//const int maxn = 3000 + 10;
int A[maxn];
bool vis[maxn];
vector<int> v;
string s;
void doit(int n)
{	
	s = toString(n); v.clear(); v.push_back(n); int i; char ch;
	foo(i,1,s)
	{
		ch = s[0]; s.erase(0,1); s += ch; if(s[0] == '0')continue;
		n = toInt(s); if(n < maxn)v.push_back(n);
	}
	sort(li(v)); 
	foo(i,1,v)A[v[i-1]] = v[i]; A[v.back()] = v.back();
}

void init()
{
	int i; CLR(A,-1);
	fo(i,0,10)A[i] = i; 
	fo(i,10,maxn)if(A[i] == -1)
	{
		//cout << "processing for value : " << i << endl;
		doit(i);
	}
}

int getv(int n,int ma)
{
	int su = 1; vis[n] = true;
	while(A[n] != n)
	{		
		n = A[n]; if(n > ma)break;
		vis[n] = true; su++;  
	}
	return su;
}

Long calc(int a,int b)
{
	Long su = 0,cnt; int i;
	fo(i,a,b)if(!vis[i])
	{
		cnt = getv(i,b);
		su += (cnt * (cnt-1))/2;
	}
	return su;
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	init(); //cout << "Initiallize complete....\n";
	int Case,t,a,b;
	scanf("%d",&t); 
	fo(Case,1,t+1)
	{		
		CLR(vis,false); cin >> a >> b; 
		printf("Case #%d: ",Case);
		printf("%I64d",calc(a,b));
		cout << endl;
	}
	return 0;
} 

