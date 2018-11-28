#include <cstdio>

int main() {
  int tc;
  scanf("%d", &tc);
  for(int z = 1; z <= tc; z++) {
    int N, K;
    scanf("%d%d", &N, &K);
    if((K&((1<<N)-1)) == ((1<<N)-1))
      printf("Case #%d: ON\n", z);
    else
      printf("Case #%d: OFF\n", z);
  }
  return 0;
}
