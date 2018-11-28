#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int P, N;
int M[1025], TC[1025];
long long DP[2049][11];

#define INF 2000000000LL
#define PARENT(x) ((x)/2)
#define LEFT(x) ((x)*2)
#define RIGHT(x) ((x)*2+1)

int main() {
  int i, j;
  scanf("%d", &T);
  for(int tc=1; tc<=T; tc++) {
    scanf("%d", &P); N = 1<<P;
    for(i = 0; i < N; i++) scanf("%d", &M[i]);
    for(i = P-1; i >= 0; i--) for(j = (1<<i); j < (2<<i); j++) scanf("%d", &TC[j]);
    for(i = 0; i < 2*N; i++) for(j = 0; j <= P; j++) DP[i][j] = 0;
    for(i = 2*N-1; i > 0; i--) for(j = 0; j <= P; j++) {
      if(i >= N) DP[i][j] = (j > M[i-N] ? INF : 0);
      else
        DP[i][j] = min(DP[LEFT(i)][j]+DP[RIGHT(i)][j]+TC[i],
          j < P ? DP[LEFT(i)][j+1]+DP[RIGHT(i)][j+1] : INF);
    }
    printf("Case #%d: %lld\n", tc, DP[1][0]);
  }
  return 0;
}

