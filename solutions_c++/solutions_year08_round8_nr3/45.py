#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define rep(i,n) for(i=0; i<n; ++i)
#define forr(i,a,b) for(i=a; i<=b; ++i)
#define ford(i,a,b) for(i=a; i>=b; --i)
#define X first
#define Y second
template<class T> inline void smin(T& a, const T& b) { if(a>b) a=b; }
template<class T> inline void smax(T& a, const T& b) { if(a<b) a=b; }
template<class T> T gcd(T a, T b) { return (b!=0) ? gcd(b,a%b) : a; }
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

const int m=1000000009;
int i,j, n,k, a,b, U,N;
VI r[600];

ll f(int v, int p, int z)
{
   if(sz(r[v])==1) return 1;  
   if(z>k)return 0;
   int i;
   ll res=1;
   rep(i,sz(r[v])-1) res=(res*(k-z-i)) %m;
   rep(i,sz(r[v])) if(r[v][i]!=p) res=(res* f(r[v][i],v,sz(r[v])) )%m;
   return res;
}

int main()
{
	freopen("c-large.in","r",stdin);//large-small-attempt0
	freopen("c-large.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
		cin>>n>>k;
		forr(i,1,n) r[i].clear();
		rep(i,n-1)
		{
      cin>>a>>b;
      r[a].pb(b); r[b].pb(a);
    }
    i=1; while(sz(r[i])!=1) ++i;
		printf("Case #%d: %d\n",U+1, int( (f(r[i][0],i,1)*k) %m ));
	}
	return 0;
}
