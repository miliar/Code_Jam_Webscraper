#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;
#define FCO(i,a,b) for(ll i=a,_b=b;i<_b;++i)
#define FCC(i,a,b) for(ll i=a,_b=b;i<=_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ROF(i,n) for(ll i=n-1;i>=0;--i)
#define SZ(v) (signed(v.size()))
#define FOZ(i,v) FOR(i,SZ(v))
#define ALL(s) s.begin(),s.end()
#define LET(a,b) typeof(b) a=b
#define FOREACH(it,s) for(LET(it,s.begin());it!=s.end();++it)

#define D(A) 

typedef long long ll;

bool issq(ll n) {
  if(n==0) return true;
  ll big = 1000000000;
  ll lo = 0, hi = big + n/big; //lo*lo <= n < hi*hi
  assert(hi * hi > n);
  while(hi>lo+1) {
    ll mid = (lo + hi)/2;
    D(assert(lo <= mid););
    D(assert(mid < hi););
    ll sq = mid*mid;
    if(sq==n) return true;
    if(sq<n) lo = mid;
    if(sq>n) hi = mid;
  }
  assert(lo <= hi);
  assert(hi <= lo+1);
  return lo*lo==n or hi*hi==n;
}

int main() {
  int ncases; scanf("%d", &ncases);
  FOR(casenum, ncases) {
    cout<<"Case #"<<casenum+1<<": ";
    //printf("Case #%d: ", casenum+1);
    string s; cin>>s;
    D(cerr<<"#"<<s<<"#"<<endl;);
    int nq = 0; FOZ(i,s) if(s[i]=='?') ++nq;
    cerr<<nq<<" quetions"<<endl;
    int N = SZ(s);
    ll v[nq], lq=0;
    FOR(i,N) {
      if(s[N-1-i]=='?') v[lq++] = i;
    }
    ll bare = 0;
    FOR(i,N) if(s[N-1-i]!='?') bare += (s[N-1-i]=='1')*(1LL<<i);

    ll tn = 1LL<<nq;
    cerr<<tn<<endl;
    FOR(sub,tn) {
      ll sq = 0;
      ll ch[nq]; FOR(i,nq) ch[i]= (sub>>i)&1;
      FOR(i,nq) sq += (1LL<<v[i])*ch[i];
      D(cerr<<sq<<", so "<<sq+bare<<endl;);
      sq += bare;
      if(issq(sq)) {
        FOR(i,nq) s[N-1-v[i]] = (ch[i] ? '1' : '0');
        //printf("%s\n", s.c_str());
        cout<<s<<endl;
        break;
      }
    }
  }
  return 0;
}
