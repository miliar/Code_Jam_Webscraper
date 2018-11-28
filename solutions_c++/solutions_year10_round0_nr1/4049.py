#include <cstdio>

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=0; t<T; t++){
    int N, K;
    scanf("%d %d", &N, &K);
    K = K&((1<<N)-1);
    if(K == ((1<<N)-1)){ printf("Case #%d: ON\n", t+1); }
    else printf("Case #%d: OFF\n", t+1);
  }
  return 0;
}
