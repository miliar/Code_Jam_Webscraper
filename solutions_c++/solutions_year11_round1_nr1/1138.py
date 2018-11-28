#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define popcount  __builtin_popcount
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define REP(var,ar)  for(int var=0,lim=(ar).size();var<lim;var++)
#define FOR(var,from,to) for(int var=(from),till=(to);var<=till;var++)
#define all(c)  (c).begin(),(c).end()
#define rall(c)  (c).rbegin(),(c).rend()
#define tr(c,i)  for(__typeof__((c).begin()) i=(c).begin(),till=(c).end(); i!=till; i++)
#define found(s,e)  ((s).find(e)!=(s).end())
#define mset(arr,val)  memset(arr,val,sizeof(arr))

typedef long long ll;

typedef pair<int,int> ii;
#define cons(x,y) make_pair((x),(y))
#define car(x) ((x).first)
#define cdr(x) ((x).second)
#define caar(x) (x).first.first
#define cdar(x) (x).first.second
#define cadr(x) (x).second.first
#define cddr(x) (x).second.second

ll gcd(ll m, ll n)
{
  if (m == 0 || n == 0) return 0;
  if (m == 1 || n == 1) return 1;
  if (m == n) return m;
  while (1) {
        if (m == 0) return n;
        if (n == 0) return m;
        if (m > n) m %= n; else n %= m;
  }
}

int main(){
  int T;cin>>T;
  rep(t,T){
    string s; cin>>s; ll N = strtoll(s.c_str(), 0, 10); // 1-1e15
    int Pd, Pg; cin>>Pd>>Pg; //1-100each
    ll gd = gcd(Pd,100), gg = gcd(Pg,100);
    if (gd==0) gd=100; if (gg==0) gg=100;
    ll wd = 100 / gd, wg = 100 / gg;
    ll md = Pd / gd, mg = Pg / gg;
    ll ld = wd - md, lg = wg - mg;
    // printf("[%d] {%lld,%d,%d} %lld/%lld %lld/%lld (%lld/%lld %lld/%lld)\n", 1+t, N,Pd,Pg, md,wd, mg,wg,  ld,wd, lg,wg);
    if (wd > N) goto ng;
    if (ld != 0 && lg == 0) goto ng;
    if (md != 0 && mg == 0) goto ng;
    
    
   ok: 
    printf("Case #%d: %s\n", 1+t, "Possible");
    continue;
   ng:
    printf("Case #%d: %s\n", 1+t, "Broken");
    continue;
  }
  return 0;
}
