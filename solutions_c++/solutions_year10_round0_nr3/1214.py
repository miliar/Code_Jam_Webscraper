#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>

#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cstring>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
#define FOR(i,b,e) for(int i=(int)(b);i<(int)(e);i++)
#define ALL(c) (c).begin(), (c).end()
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEFOP(T,O,E)    bool operator O(const T& a,const T& b){ return a.E O b.E; }
#define DEFOP2(T,O,E,F) bool operator O(const T& a,const T& b){ return make_pair(a.E,a.F) O make_pair(b.E,b.F); }

using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<long long> vll;
typedef vector<string> vstring;
typedef vector<double> vdouble;

template<class T>void pp(T v,int n){ REP(i,n)cout<<v[i]<< ' ' ; cout << endl;}
template<class T>void pp(T v){ EACH(it,v) cout << *it << ' ' ; cout << endl; }
template<class T>T& ls(T& a,T b){ if(b<a) a=b; return a;}
template<class T>T& gs(T& a,T b){ if(b>a) a=b; return a;}
int to_i(const string& s){int n;sscanf(s.c_str(),"%d",&n);return n;}
string to_s(int n){char buf[32];sprintf(buf,"%d",n);return string(buf);}

const int N=1024;

ll solve(ll r,ll k, ll v[],ll n){
  static ll next[N];
  static ll earn[N];

  REP(i,n){
    ll cnt=v[i], pos=(i+1)%n;
    REP(j,n){
      if(cnt+v[pos]>k || pos==i) break;
      cnt+=v[pos];
      pos++; pos=pos%n;
    }
    next[i]=pos; earn[i]=cnt;
  }

  ll ans=0, pos=0;
  REP(i,r) ans+=earn[pos], pos=next[pos];
  return ans;
}

int main(){
  int C;
  cin >> C;
  REP(CC,C){
    ll r,k,n;
    static ll v[N];
    cin >> r >> k >> n;
    REP(i,n) cin >> v[i];

    printf("Case #%d: %lld\n",CC+1, solve(r,k,v,n));
  }
}
