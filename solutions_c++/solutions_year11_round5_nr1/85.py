#include <cstdio>
#include <algorithm>
#include <cassert>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

struct pt {
   double x,y;
};
double operator^(const pt& a, const pt& b) { return a.x*b.y - a.y*b.x; }
pt ptx(const pt& a, const pt& b, double x) {
   pt p; p.x = x; p.y = a.y + (b.y-a.y)*(x-a.x)/(b.x-a.x); return p;
}

const int N=2000;
int _,w,l,u,g;
pt lp[N],up[N];

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d%d%d%d",&w,&l,&u,&g);
      REP(i,l) scanf("%lf%lf",&lp[i].x,&lp[i].y);
      REP(i,u) scanf("%lf%lf",&up[i].x,&up[i].y);
      reverse(up,up+u);

      double area = 0;
      REP(i,l-1) area += lp[i] ^ lp[i+1];
      area += lp[l-1] ^ up[0];
      REP(i,u-1) area += up[i] ^ up[i+1];
      area += up[u-1] ^ lp[0];
//      printf("%lf\n",area);

      printf("Case #%d:\n",test+1);
      REP(ii,g-1) {
	 double lb=0,ub=w;
	 REP(z,100) {
	    double s = (lb+ub)/2, ar = 0; int li=l-1,lj;
	    REP(i,l-1) if (lp[i+1].x < s) ar += lp[i] ^ lp[i+1]; else { li=i; break; }
	    REP(i,u-1) if (up[i].x < s) ar += up[i] ^ up[i+1]; else lj=i+1;
//	    printf("li=%d lj=%d  (%d %d)\n",li,lj,l,u);
	    assert(0 <= li && li+1 < l);
	    assert(0 <= lj-1 && lj < u);
	    pt tpl = ptx(lp[li],lp[li+1],s),
	       tpu = ptx(up[lj],up[lj-1],s);
	    ar += (lp[li] ^ tpl) + (tpl ^ tpu) + (tpu ^ up[lj]) + (up[u-1] ^ lp[0]);
//	    printf("%lf -> %lf\n",s,ar);

	    if (ar > area/g*(ii+1)) ub = s; else lb = s;
	 }
	 printf("%.10lf\n",lb);
      }
   }
}
