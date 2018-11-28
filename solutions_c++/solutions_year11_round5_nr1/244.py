#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;
#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FCC(i,a,b) for(int i=a,_b=b;i<=_b;++i)
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
#define D(A) 

const int INF = 2000000000;
typedef long long ll;
typedef long double ld;
const ld FINF = 1e8;
const ld eps = 1e-9;

int main() {
  int ncases; scanf("%d", &ncases);
  D(cerr<<"There are "<<ncases<<" cases "<<endl;);
  FOR(casenum, ncases) {
    printf("Case #%d:\n", casenum+1);
    D(cerr<<"Case : "<<casenum+1<<endl;);

    int W, L, U, G; scanf("%d %d %d %d", &W, &L, &U, &G);
    int xlo[L+1], ylo[L+1]; FOR(i,L) scanf("%d %d", &xlo[i], &ylo[i]); xlo[L] = INF;
    int xhi[U+1], yhi[U+1]; FOR(i,U) scanf("%d %d", &xhi[i], &yhi[i]); xhi[U] = INF;

    D(cerr<<"Lo"<<endl; FOR(i,L) cerr<<xlo[i]<<" "; cerr<<endl;
      cerr<<"Hi"<<endl; FOR(i,U) cerr<<xhi[i]<<" "; cerr<<endl;);

    set<int> ix; FOR(i,L) ix.insert(xlo[i]); FOR(i,U) ix.insert(xhi[i]);
    vector<int> xx(ALL(ix));
    D(FOZ(i,xx) cerr<<xx[i]<<" "; cerr<<endl;);
    int N = SZ(xx);
    ld yl[N], yh[N];
    {
      int l=0, u=0;
      FOR(i,N) {
        D(cerr<<i<<": "<<xx[i]<<" "<<xlo[l]<<" ("<<l<<") "<<xhi[u]<<" ("<<u<<")"<<endl;);
        assert(xlo[l]>=xx[i]);
        assert(xhi[u]>=xx[i]);
        if(xlo[l]==xx[i]) yl[i]=ylo[l++]; else yl[i]= ylo[l-1] + (ylo[l]-ylo[l-1])*ld(xx[i]-xlo[l-1])/(xlo[l]-xlo[l-1]);
        if(xhi[u]==xx[i]) yh[i]=yhi[u++]; else yh[i]= yhi[u-1] + (yhi[u]-yhi[u-1])*ld(xx[i]-xhi[u-1])/(xhi[u]-xhi[u-1]);
      }
    }
    //FOR(i,N) cerr<<xx[i]<<": "<<yl[i]<<" "<<yh[i]<<endl;

    ld A = 0;
    FOR(i,N-1) 
      A += (xx[i+1]-xx[i])*(yh[i]-yl[i] + 0.5*(yh[i+1]-yh[i]) - 0.5*(yl[i+1]-yl[i]));
    //cerr<<A<<endl;

    ld e = A/G;
    {
      ld cx = 0, cyl=yl[0], cyh=yh[0]; int w=0;
      FOR(k,G-1) {
        //cerr<<"Trying k = "<<k<<endl;
        ld need = e;
        while(need > 1e-9) {
          //Area from x to xx[w+1]
          ld next = (xx[w+1]-cx)*(cyh-cyl + 0.5*(yh[w+1]-cyh) - 0.5*(yl[w+1]-cyl));
          //cerr<<"need = "<<need<<" and next = "<<next<<endl;
          if(next > need - 1e-9) {
            ld lo=0, hi=1; //area(lo)< need < area(hi)
            while(hi - lo > 1e-9) {
              ld t = lo + (hi-lo)/2;
              ld xa = t*(xx[w+1] - cx)*(cyh-cyl + 0.5*t*(yh[w+1]-cyh) - 0.5*t*(yl[w+1]-cyl));
              if(xa>need) hi = t;
              else lo = t;
            }
            cx = cx + lo*(xx[w+1] - cx);
            printf("%.8Lf\n", cx);
            cyl = cyl + lo*(yl[w+1]-cyl);
            cyh = cyh + lo*(yh[w+1]-cyh);
            break;
          }
          //else
          cx = xx[w+1];
          cyl = yl[w+1];
          cyh = yh[w+1];
          need -= next;
          ++w;
        }
      }
    }
  }
  return 0;
}
