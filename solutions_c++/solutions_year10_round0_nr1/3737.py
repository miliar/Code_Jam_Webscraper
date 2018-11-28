#include <cstdio>

int main() {


  int T, N, K;

  scanf("%d", &T);
  for(int t=0; t<T; t++) {
    printf("Case #%d: ", t+1);

    scanf("%d %d", &N, &K);
    if( K%(1<<N)==((1<<N)-1))
      printf("ON");
    else
      printf("OUT");
    printf("\n");

  }

  return 0;
}