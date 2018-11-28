#include <cstdio>
#include <utility>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
  int t;
  scanf("%d",&t);
  int case_n = 1;
  while (t--) {
    int n, s, p;
    scanf("%d %d %d",&n, &s, &p);
    int tot = 0;
    int triplets = 0;
    while (n--) {
      int a;
      scanf("%d",&a);
      int b = a%3;
      a = a/3;
      if (a >= p) tot++;
      else if (b == 0 && a+1 >= p && a) triplets++;
      else if (b == 1 && a+1 >= p) tot++;
      else if (b == 2 && a+1 >= p) tot++;
      else if (b == 2 && a+2 >= p) triplets++;
      //printf("A = %d, = %d, k = %d, tot %d, trip %d\n",a,b,a*3+b,tot,triplets);
    }
    printf("Case #%d: %d\n", case_n++, tot + min(s, triplets));
  }
  return 0;
}
