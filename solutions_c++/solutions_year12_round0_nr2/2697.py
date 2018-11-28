#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iomanip>
#include <bitset>

using namespace std;
 
typedef unsigned long long ULL;
typedef long long LL;
typedef vector< int > vi;

#define pb push_back
#define mp make_pair
#define MAX 50
#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LLt;scanf("%lld",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define INF (int)1e9
#define EPS (double)1e-9
#define fii freopen("ip.txt","r",stdin)
#define fio freopen("out.txt","w",stdout)
#define ALL(x) x.begin(),x.end()
int n,s,p;
vector<int> t;
int surprise(int in)
{
  int ans=0;
  REP(i,10)
    {
      if(i+2>10) break;
      FOR(j,2,5) if(3*i+j==t[in]) ans=max(ans,i+2);
    }
  return ans;
}
int best(int in)
{
  int ans=0;
  REP(i,11)
    {
      if(3*i==t[in]) ans=max(ans,i);
      if(3*i+1==t[in] && i+1<=10) ans=max(ans,i+1);
      if(3*i+2==t[in] && i+1<=10) ans=max(ans,i+1);
    }
  return ans;
}
int main()
{
  int test=GI,kase=1;
  while(test--)
    {
      t.clear();
      cin>>n>>s>>p;
      REP(i,n) t.pb(GI);
      sort(ALL(t));
      int ret=0;
      REP(i,1<<n)
	{
	  if(__builtin_popcount(i)!=s) continue;
	  int sd=s,ans=0;
	  REP(j,n)
	    {
	      int x=surprise(j);
	      if(x && sd && i&(1<<j)) ans+=(x>=p),sd--;
	      else ans+=(best(j)>=p);
	    }
	  if(!sd) ret=max(ret,ans);
	}
      printf("Case #%d: %d\n",kase++,ret);
    }
  return 0;
}
