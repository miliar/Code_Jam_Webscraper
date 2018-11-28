#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int N, X;
int L[1009];
int P[1009];
long double Q[1009];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    //input
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
      scanf("%d", &L[i]);
    for (int i = 0; i < N; i++)
      scanf("%d", &P[i]);
    
    //calculate
    for (int i = 0; i < N; i++) {
      long double Qi = 1 - 0.01 * P[i];
      Q[i] = 1 - exp( log(Qi) / L[i] );
    }
    printf("Case #%d:", Ti);
    for (int i = 0; i < N; i++) {
      long double m = -1;
      int mj = -1;
      for (int j = 0; j < N; j++)
        if (m < Q[j]) {
          m = Q[j];
          mj = j;
        }
      printf(" %d", mj);
      Q[mj] = -1;
    }
    printf("\n");
  }
  return 0;
}