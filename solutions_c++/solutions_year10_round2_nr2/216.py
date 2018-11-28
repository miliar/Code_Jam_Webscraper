#include <cstdio>
#include <vector>

int main()
{
  int C;
  scanf("%d", &C);
  for(int c=1; c<=C; ++c) {
    int N, K, B, T;
    scanf("%d%d%d%d", &N, &K, &B, &T);
    std::vector<int> X(N), V(N);
    for(int i=0; i<N; ++i)
      scanf("%d", &X[i]);
    for(int i=0; i<N; ++i)
      scanf("%d", &V[i]);
    int reached=0, skipped=0, swaps=0;
    for(int i=N-1; i>=0 && reached<K; --i) {
      if(X[i] + T*V[i] >= B) {
	++reached;
	swaps += skipped;
      } else
	++skipped;
    }
    if(reached==K)
      printf("Case #%d: %d\n", c, swaps);
    else
      printf("Case #%d: IMPOSSIBLE\n", c);
  }
  return 0;
}
