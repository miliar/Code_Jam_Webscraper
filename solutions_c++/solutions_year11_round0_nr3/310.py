#include <cstdio>
using namespace std;

int T, n;
int xorsum, tmin, totsum;

int main() {

  freopen("C-large.in", "rt", stdin);
  freopen("C-large.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int cT = 0; cT < T; cT++) {
  
    scanf("%d", &n);
    xorsum = 0;
    totsum = 0;
    tmin = 1000000000;
    for(int i = 0; i < n; i++) {
      int t; scanf("%d", &t);
      xorsum ^= t;
      totsum += t;
      if (t < tmin) tmin = t;   
    }
    
    printf("Case #%d: ", cT+1);
    if (xorsum) puts("NO");
    else printf("%d\n", totsum - tmin);
  
  }
  
  return 0;
 
}
