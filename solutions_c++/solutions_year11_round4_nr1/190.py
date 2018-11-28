#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
typedef long long ll;

int _,x,s,r,n,b,e,w;
map<int,int> ma;
double t,ans;

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
      REP(i,n) {
	 scanf("%d%d%d",&b,&e,&w);
	 ma[w + s] += e-b;
	 x -= e-b;
      }
      ma[s] += x;
      ans = 0;
      FORE(i,ma) {
	 double iles = min( ll(i->first+r-s) * t, double(i->second) );
	 t -= iles * 1. / ll(i->first+r-s);
	 ans += iles * 1. / (i->first + r-s);
	 ans += (i->second - iles) * 1. / i->first;
      }
      printf("Case #%d: %.10lf\n",test+1,ans);
      ma.clear();
   }
}
