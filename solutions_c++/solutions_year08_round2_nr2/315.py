//B. Number Sets.cpp 

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>

using namespace std;

const double pi=acos(-1.0);
const double eps=1e-11;

#define SZ(X) ((int)(X.size()))
#define MP(A,B) make_pair(A,B)
#define FOR(i,b,e) for(int i = b;i < e;++i)
#define RE(i,n) FOR(i,0,n)

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))>0)
#define containL(S,X) (((S)&twoL(X))>0)
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;} 
int64 toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;} 
string toString(int64 v){ostringstream sout;sout<<v;return sout.str();} 
string toString(int v){ostringstream sout;sout<<v;return sout.str();} 

template<class T> inline T countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline T sqr(T x){return x * x;}
template<class T> inline T gcd(T a,T b){if(a < 0) return gcd(-a,b); if(b < 0) return gcd(a,-b); return (b == 0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){return a*(b/gcd(a,b));}
template<class T> void out(T A[],int n){for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}
template<class T> void out(vector<T> A,int n = -1){if(n==-1) n = A.size();for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}

const int SCALE = 1010;
int res;
int a,b,p;
int ispri[SCALE];
int prime[SCALE];
int len;
void genprime()
{
	len = 0;
	RE(i,SCALE)ispri[i] = 1;
	for(int i = 4;i < SCALE;i += 2) ispri[i] = 0;
	for(int i = 3;i < SCALE;++i) if(ispri[i])
	{
		for(int j = i + i;j < SCALE;j += i)ispri[j] = 0;
	}
	FOR(i,2,SCALE)if(ispri[i])prime[len++] = i;
}
int pre[SCALE];
int findpre(int x)
{
	if(pre[x] != x) pre[x] = findpre(pre[x]);
	return pre[x];
}
void unionset(int x,int y)
{
	x = findpre(x);
	y = findpre(y);
	if(x != y)
	{
		pre[x] = pre[y];
		--res;
	}
}
void solve()
{
	cin >> a >> b >> p;
	res = b - a + 1;
	RE(i,res + 1)pre[i] = i;
	FOR(i,a,b + 1) FOR(j,i + 1,b + 1)
	{
		int g = gcd(i,j);
		int mx = 1;
		for(int k = 0;k < len && prime[k] <= g;++k)
			if(g%prime[k] == 0)mx = max(mx,prime[k]);
		if(mx >= p) 
		{
			unionset(i - a,j - a);
		}
	}
}
int main() 
{

	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);

	int ncase = 0;
	cin >> ncase;
	genprime();
	FOR(i,1,ncase + 1)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << res << endl;
	}
	return 0;
}
