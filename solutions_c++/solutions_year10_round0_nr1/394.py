#include <cstdio>

using namespace std;

int main(void)
{
  int t;
  scanf("%d", &t);
  for(int case_cnt = 1; case_cnt <= t; case_cnt++) {
    int n, k;
    scanf("%d %d", &n, &k);
    printf("Case #%d: %s\n", case_cnt, (k > 0 && (k + 1) % (1 << n) == 0) ? "ON" : "OFF");
  }
    
  return 0;
}

