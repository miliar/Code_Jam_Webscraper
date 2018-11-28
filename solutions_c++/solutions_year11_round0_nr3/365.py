#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int sum, minnum;
int xor_sum;

int main()
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    scanf("%d", &n);

    sum = 0, minnum = 100000000, xor_sum = 0;
    for (int x, i = 0; i < n; ++i) {
      scanf("%d", &x);
      sum += x;
      xor_sum ^= x;
      minnum = min(minnum, x);
    }

    printf("Case #%d: ", l);
    if (xor_sum) 
      puts("NO");
    else
      printf("%d\n", sum-minnum);
  }
  return 0;
}
