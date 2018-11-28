//A. Cheating a Boolean Tree .cpp 

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

const int SCALE = 10010 ;
const int INF = 1000000;
int f[SCALE][2];
int mem[SCALE][2];
int m,v;
int ans;

void input()
{
	int i = 1;
	for(i = 1;i <= (m-1)/2; ++i) 
		cin >> f[i][0] >> f[i][1];
	for(i = i;i <= m;++i)
		cin >> f[i][0],f[i][1] = 0;
	memset(mem,-1,sizeof(mem));
}

int recs(int x,int whi)
{
	if(x > (m-1)/2)
	{
		if(whi == f[x][0]) return 0;
		else return INF;
	}
	if(mem[x][whi] != -1) return mem[x][whi];
	int & res = mem[x][whi];

	
	int t1= INF,t2 = INF,r1 = INF,r2 = INF,r3 = INF,r4 = INF;
	
	if(f[x][1] == 1)
	{
		if(whi == 0)
		{
				r1 = min(recs(x + x,0),recs(x + x + 1,0));//f[x][0] == 1;
			
				r2 = recs(x + x,0) + recs(x + x + 1,0);//f[x][0] == 0;
				if(f[x][0] == 0)
				{
					return res = min(r1 + 1,r2);
				}
				else return res = min(r1,r2 + 1);
			
		}
		if(whi == 1)
		{
				r1 = min(recs(x + x,1),recs(x + x + 1,1));//f[x][0] == 0;
			
				r2 = recs(x + x,1) + recs(x + x + 1,1);//f[x][0] == 1;
				if(f[x][0] == 0)
				{
					return res = min(r1,r2 + 1);
				}
				else return res = min(r1 + 1,r2);
		}
		
	}
	else
	{
		if(whi == 0)
		{
			if(f[x][0] == 1)//and
			{
				return res = min(recs(x + x,0),recs(x + x + 1,0));
			}
			else//or
			{
				return res = recs(x + x,0) + recs(x + x + 1,0);
			}
		}
		if(whi == 1)
		{
			if(f[x][0] == 0)//or
			{
				return res = min(recs(x + x,1),recs(x + x + 1,1));
			}
			else//and
			{
				return res = recs(x + x,1) + recs(x + x + 1,1);
			}
		}
	}
}
void solve()
{
	ans = INF;
	ans = recs(1,v);/*
	if(f[1][1] == 1)
	{
		int r1 = recs(1,v);
		int r2 = recs(1,1) + 1;
		ans = min(r1,r2);
	}
	else ans = recs(1,v);*/
}
int main() 
{

	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);

	/*freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);*/

	int ncase;
	cin >> ncase;
	FOR(i,1,ncase + 1)
	{
		
		cout << "Case #" << i << ": ";
		cin >> m >> v;
		input();
		solve();
		if(ans < INF)cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
