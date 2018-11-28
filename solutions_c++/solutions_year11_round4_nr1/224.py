#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;
#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ROF(i,n) for(int i=n-1;i>=0;--i)
#define SZ(v) (signed(v.size()))
#define FOZ(i,v) FOR(i,SZ(v))
#define ALL(s) s.begin(),s.end()
#define LET(a,b) typeof(b) a=b
#define FOREACH(it,s) for(LET(it,s.begin());it!=s.end();++it)

typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define D(A) A

const int INF = 2000000000;
typedef long long ll;
typedef long double ld;
const ld FINF = 1e8;
const ld eps = 1e-9;

typedef struct {
  int b, e, w;
} walkway;
walkway iway[1000], way[3000];

bool cmpbegin(const walkway a, const walkway b) {
  return a.b<b.b;
}

bool cmpw(const walkway a, const walkway b) {
  if(a.w != b.w) return a.w<b.w;
  return a.b < b.b;
}

int main() {
  int ncases; scanf("%d", &ncases);
  FOR(casenum, ncases) {
    int X, S, R, tt, N;
    scanf("%d %d %d %d %d", &X, &S, &R, &tt, &N);
    ld t = tt;
    //cerr<<X<<" "<<S<<" "<<R<<" "<<t<<" "<<N<<endl;
    FOR(i,N) {
      scanf("%d %d %d", &(iway[i].b), &(iway[i].e), &(iway[i].w));
    }
    sort(iway, iway + N, cmpbegin);

    int last=0, nway=0;
    FOR(i,N) {
      if(iway[i].b > last) {
        walkway t; t.b=last; t.e=iway[i].b; t.w=0;
        way[nway++] = t;
      }
      way[nway++] = iway[i];
      last = iway[i].e;
    }
    if(X > last) {
      walkway t; t.b=last; t.e=X; t.w=0;
      way[nway++] = t;
    }
    sort(way, way + nway, cmpw);
    //FOR(i,nway) cerr<<way[i].b<<" "<<way[i].e<<" "<<way[i].w<<endl;

    ld ans = 0;
    FOR(i,nway) {
      walkway w = way[i];
      int L = w.e - w.b;
      ld runspeed = w.w + R;
      ld run = min(L/runspeed, t);
      t -= run;
      ld walk = 0;
      if(runspeed*run < L) walk = (L-run*runspeed)/(w.w + S);
      //cerr<<"Way "<<i<<": run for "<<run<<" and walk for "<<walk<<endl;
      ans += run + walk;
    }
    printf("Case #%d: %.9Lf\n", casenum+1, ans);
  }
  return 0;
}
