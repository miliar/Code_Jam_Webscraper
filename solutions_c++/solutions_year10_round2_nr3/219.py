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
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define REP(var,ar)  for(int var=0,lim=(ar).size();var<lim;var++)
#define FOR(var,from,to) for(int var=(from),till=(to);var<=till;var++)
#define all(c)  (c).begin(),(c).end()
#define rall(c)  (c).rbegin(),(c).rend()

#define found(s,e)  ((s).find(e)!=(s).end())
#define mset(arr,val)  memset(arr,val,sizeof(arr))

typedef long long ll;
typedef vector<int> Vi;
typedef vector<vector<int> > VVi;
typedef pair<int,int> ii;
typedef pair<ll,ll> ll2;

#define cons(x,y) make_pair((x),(y))
#define car(x) ((x).first)
#define cdr(x) ((x).second)
#define cadr(x) (x).second.first
#define cddr(x) (x).second.second

map<ii,ll> mm;
map<ll2,ll> cmm;

static const ll MODVAL = 100003ll;

ll add(ll x, ll y) { return (x + y) % MODVAL; }
ll sub(ll x, ll y) { return (x - y) % MODVAL; }
ll mul(ll x, ll y) { return (x * y) % MODVAL; }
ll pow(ll x, ll y) {
  ll v = 1;
  for(;y;x=mul(x,x),y>>=1)
    if(y&1) v = mul(v, x);
  return v;
}
ll divi(ll x, ll y) { return mul(x, pow(y, MODVAL-2)); } // (x / y) % MODVAL ←ここ
ll C(ll n, ll k) { // nCk
  ll2 p(n,k);
  if (found(cmm,p)) return cmm[p];
  ll v = 1;
  for(ll i=1; i<=k; ++i) 
    v = divi(mul(v, n-i+1), i);
  return cmm[p]=v;
}

ll sub(int n,int last){
  if (n == 1) return 1LL;
  //nがk番目(k=1..n-1)
  ii key=ii(n,last);
  if (found(mm,key)) return mm[key];
  ll skm=last-n-1;
  ll a = 0LL;
  if (last > 10000) {
    for(int k=1; k<=n-1; k++){
      a += sub(k,n);
    }
  } else {
    for(int k=1; k<=n-1; k++){
      ///当然kが入ってる
      int kos=n-k-1;
      a += mul(C(skm,kos),sub(k,n));
    }
  }
  mm[key] = a % MODVAL;
  return mm[key];
}

int main(){
  int T; cin >> T; //100
  mm.clear();
  rep(t,T){
    int n; cin >> n; // 2-500
    int ans = (int)sub(n,987654321);
    printf("Case #%d: %d\n", t+1, ans);
  }
  return 0;
}
