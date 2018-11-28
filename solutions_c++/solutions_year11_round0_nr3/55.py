#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {
  int tests; scanf("%d",&tests);
  for(int t=1;t<=tests;++t) {
    int n; scanf("%d",&n);
    int a, b, c, d;
    a=b=0, c=1000000;
    while(n--) {
      scanf("%d",&d);
      a^=d;
      b+=d;
      c=min(c,d);
    }
    if (a)
      printf("Case #%d: NO\n",t);
    else
      printf("Case #%d: %d\n", t,b-c);
  }
}
