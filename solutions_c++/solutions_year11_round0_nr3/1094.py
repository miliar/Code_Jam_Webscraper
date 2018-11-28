#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N=1100;
int _,n,a[N];

int main() {
   scanf("%d",&_);
   REP(test,_) {
      printf("Case #%d: ",test+1);
      scanf("%d",&n);
      int xo=0, sum=0;
      REP(i,n) scanf("%d",&a[i]), xo ^= a[i], sum += a[i];
      int mi = *min_element(a,a+n);
      if (xo) printf("NO\n");
      else printf("%d\n", sum - mi);
   }
}
