#include <cstdio>

long long int a[1000];

int main() {
  long long int case_no, i, t, n, sum, esum, min;
  
  scanf("%lld", &t);
  for (case_no = 1ll; case_no <= t; case_no++) {
    scanf("%lld", &n);
    for (i = 0ll; i < n; i++)
      scanf("%lld", &a[i]);
    
    sum = esum = 0ll;
    min = 20000000000ll;
    for (i = 0ll; i < n; i++) {
      sum += a[i];
      esum ^= a[i];
      if (a[i] < min)
        min = a[i];
    }
    
    if (esum)
      printf("Case #%lld: NO\n", case_no);
    else
      printf("Case #%lld: %lld\n", case_no, sum - min);
  }
  
  return 0;
}
