#include<cstdio>

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int N;
    scanf("%d\n", &N);
    int res = 0;
    for(int i = 1; i <= N; i++)
    {
      int v;
      scanf("%d", &v);
      if(v != i)
        res++;
    }

    printf("Case #%d: %d\n", t, res);
  }
}
