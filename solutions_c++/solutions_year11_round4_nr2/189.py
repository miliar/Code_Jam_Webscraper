#include <cstdio>
#include <algorithm>
#include <cmath>
#include <complex>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N=600;
int _,h,w,d,lb,ub;
char a[N][N];

bool ok(int s) {
   REP(y,h-s+1) REP(x,w-s+1) {
      complex<double> z = 0;
      double cx = x+.5*s, cy = y+.5*s;
      REP(yy,s) REP(xx,s) {
	 if (yy==0 && xx==0 || yy==s-1 && xx==0
	       || yy==0 && xx==s-1 || yy==s-1 && xx==s-1) continue;
	 z += complex<double>(yy+y+.5 - cy, xx+x+.5 - cx) * double(a[yy+y][xx+x]-'0');
      }
//      printf("s=%d y=%d x=%d  z=%lf %lf\n",s,y,x,z.real(),z.imag());
      if (abs(z) < 1e-9) return 1;
   }
   return 0;
}

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d%d%d",&h,&w,&d);
      REP(i,h) REP(j,w) scanf(" %c",&a[i][j]);

      for (lb=min(w,h); lb >= 3; --lb) {
	 fprintf(stderr,"%d\n",lb);
	 if (ok(lb)) break;
      }

      printf("Case #%d: ",test+1);
      if (lb>=3 && ok(lb)) printf("%d\n",lb);
      else printf("IMPOSSIBLE\n");
   }
}
