#include <cstdio>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <queue>
using namespace std;


#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(int)(n); ++i)
        
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int mod=10009;


string s[128];
int cnt[128][32];
map<int,int> f[105][11][505];
vector<vi> poly;
vector<vi> power;
int ans[32];
int n, k;
int c[32][32];
vi x; int y;
vi xp;


inline int code(int a[]) {
 int res=0;
 forn (i, sz(x))
  res=(res<<9)+a[i];
 return res;
}

inline void decode(int h, int a[]) {
 for (int i=sz(x)-1; i>=0; --i) {
  a[i]=h&511; h>>=9;
 }
}

inline int prod(int s, int h) {
  int a[5]={0};
  a[0]=s;
  decode(h, a+1);
  int res=1;
  forn (i, sz(x)+1)
    forn (j, xp[i])
     res=res*a[i]%mod;
  return res;
}




int rec(int pos, int rem, int s, int h) {
 if (rem==0) return prod(s, h);
 if (pos>=n) return 0;
 if (f[pos][rem][s].count(h)) return f[pos][rem][s][h];
 int& res=f[pos][rem][s][h];
 res=0;
 int a[5]={0};
 decode(h, a);
 res+=rec(pos+1, rem, s, h);
 if (res>=mod) res-=mod;
 
 forn (i, rem) {
  s+=cnt[pos][y];
  forn (j, sz(x))
   a[j]+=cnt[pos][x[j]];
  res=(res+rec(pos+1, rem-1-i, s, code(a))*c[rem][i+1])%mod;
 }
 
 return res;
}


int main() {
 freopen("b.in", "r", stdin);
 freopen("b.out", "w", stdout);

 forn (i, 32) {
   c[i][0]=1;
   for (int j=1; j<=i; ++j)
     c[i][j]=(c[i-1][j-1]+c[i-1][j])%mod;
 }

 int nt; scanf("%d\n", &nt);
 for (int tc=1; tc<=nt; ++tc) {

  string p; cin>>p;
  poly.clear();
  power.clear();
  forn (i, sz(p)) if (p[i]=='+') p[i]=' ';
  istringstream sin(p);
  for (string xx; sin>>xx; ) {
   vi t;
   forn (i, sz(xx)) t.pb(xx[i]-'a');

   vi pp;
   vi tt=t;
   tt.resize(unique(tt.begin(), tt.end())-tt.begin());
   vi aa;
   forn (i, sz(tt)) {
     int cnt=0;
     forn (j, sz(t)) if (t[j]==tt[i]) ++cnt;
     aa.pb(tt[i]);
     pp.pb(cnt);
   }   
   poly.pb(aa);
   power.pb(pp);
  }           


  cin>>k;
  cin>>n;
  forn (i, n) cin>>s[i];

  memset(cnt, 0, sizeof(cnt));

  forn (i, n) {
   forn (j, 26) forn (k, sz(s[i]))
    if (s[i][k]-'a'==j) ++cnt[i][j];
  }

  int mx=0;
  forn (i, n) forn (j, 26) mx=max(mx, cnt[i][j]);
  mx*=k;


  printf("Case #%d:", tc);

  memset(ans, 0, sizeof(ans));

  forn (tt, sz(poly)) {
   forn (i, n+1) forn (j, k+1) forn (q, mx+1) f[i][j][q].clear();
   y=poly[tt][0];
   x=poly[tt];
   x.erase(x.begin());
   xp=power[tt];
   for (int kk=1; kk<=k; ++kk) {
    ans[kk]+=rec(0, kk, 0, 0);
    ans[kk]%=mod;
   }
  }

  for (int kk=1; kk<=k; ++kk)
   printf(" %d", ans[kk]);
  puts("");

  fprintf(stderr, "test %d is done!\n", tc);
  
 }

 return 0;
}

