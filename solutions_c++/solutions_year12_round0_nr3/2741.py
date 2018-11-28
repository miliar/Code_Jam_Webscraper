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
int l,h;
LL possible(int n)
{
  if(n<10) return 0;
  int d=0,x=10,y=1,temp;
  temp=n;
  if(temp%10==0) temp++;
  while(temp) d++,temp/=10,y*=10;
  y/=10;
  set<int> ans;
  REP(i,d-1) 
    {
      int a=(n%x)*y+n/x;
      if(a>=l && a<=h && a!=n) ans.insert(a);
      x*=10,y/=10;
    }
  return (LL)ans.size();
}
int main()
{
  int t=GI,a,b,kase=1;
  while(t--)
    {
      cin>>a>>b;
      LL ans=0;
      l=a,h=b;
      FOR(i,a,b+1) ans+=possible(i);
      printf("Case #%d: %lld\n",kase++,ans/2);
    }
  return 0;
}
