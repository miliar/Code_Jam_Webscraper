#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <vector>

int a[1010],b[1010];

int main(){
  int cases, n;
  scanf("%d", &cases);
  for (int j = 1; j <= cases; j++) {
    scanf("%d",&n);
    for(int i=0; i<n; i++){ scanf("%d",&a[i]); b[i] = a[i]; }
    std::sort(b, b+n); int m = n;
    for(int i=0; i<n; i++) if (a[i] == b[i]) m--;
    printf("Case #%d: %lf\n",j ,(double)m);
  }
  return 0;
}
