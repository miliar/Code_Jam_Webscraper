#include <cstdio>
#include <algorithm>
using namespace std;

const int infinity = 1e9 + 9;

int N, X;
int D[10009];
int L[10009];
int E[10009];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    //input
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
      scanf("%d %d", &D[i], &L[i]);
      E[i] = infinity;
    }
    scanf("%d", &X);
    
    //add sentinel
    D[N] = X;
    L[N] = 0;
    E[N] = infinity;
    N++;
    
    //calculate
    E[0] = 0;
    for (int i = 0; i < N; i++)
      if (E[i] < infinity)
      {
        int r = D[i] - E[i];
        for (int j = i + 1; j < N; j++)
          if (D[i] + r >= D[j])
            E[j] = min(E[j], max(D[i], D[j] - L[j]));
      }
    
    //for (int i = 0; i < N; i++) printf("%d %d %d\n", D[i], L[i], E[i]);
    
    //output
    printf("Case #%d: ", Ti);
    if (E[N - 1] < infinity)
      printf("YES");
    else
      printf("NO");
    printf("\n");
  }
  return 0;
}