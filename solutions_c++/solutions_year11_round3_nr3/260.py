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

typedef vector<int> Vi;
typedef vector<vector<int> > VVi;

typedef pair<int,int> ii;
#define cons(x,y) make_pair((x),(y))
#define car(x) ((x).first)
#define cdr(x) ((x).second)
#define caar(x) (x).first.first
#define cdar(x) (x).first.second
#define cadr(x) (x).second.first
#define cddr(x) (x).second.second

typedef long long ll;

int main(){
  int T;cin>>T;
  rep(t,T){
    ll N, L, H; cin>>N>>L>>H; //10000, 1e16,1e16
    vector<ll> fq(N); rep(n,N) cin>>fq[n];
    for(int f=L;f<=H;f++) {
      bool ok=true;
      rep(n,N){
        int g=fq[n];
        if (f<g) {
          if (g % f) {ok=false;break;}
        } else if (f==g) {
          continue;
        } else {
          if (f % g) {ok=false;break;}
        }
      }
      if (ok) {
        printf("Case #%d: %d\n", 1+t, f);
        goto next;
      }
    }
    printf("Case #%d: NO\n", 1+t);
  next:;
  }
  return 0;
}
