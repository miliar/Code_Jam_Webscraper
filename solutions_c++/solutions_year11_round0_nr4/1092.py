#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N=1100;
int _,n,a[N],ans;

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d",&n);
      REP(i,n) scanf("%d",&a[i]), --a[i];
      /*ans = 0;
      REP(i,n) if (a[i] != i) {
	 ++ans;
	 REP(j,n) if (a[j] == i) { swap(a[i],a[j]); break; }
      }*/

      ans = n;
      /*REP(i,n) if (!vis[i]) {
	 vis[i] = 1;
	 int j = i;
	 do {
	    j = a[j]; vis[j] = 1;
	 } while (j != i);
	 --ans;
      }*/
      REP(i,n) if (a[i] == i) --ans;

      printf("Case #%d: %d.000000\n", test+1,ans);
   }
}
