#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
  int T;
  scanf("%d\n", &T);
  for (int i=0; i<T; i++) {
    int N;
    scanf("%d\n", &N);
    int W[N];
    int G[N];
    int P[N][N];
    memset(W, 0, sizeof(int)*N);
    memset(G, 0, sizeof(int)*N);
    memset(P, 0, sizeof(bool)*N*N);
    for (int a=0; a<N; a++) {
      for (int b=0; b<N; b++) {
        char c;
        scanf("%c", &c);
        if (c == '.') { P[a][b] = -1; continue; }
        G[a] ++;
        if (c == '1') {
          W[a]++;
          P[a][b] = 1;
        } else {
          P[a][b] = 0;
        }
      }
      scanf("\n");
    }
    //for (int a=0; a<N; a++) {
      //for (int b=0; b<N; b++) {
        //printf("%d ", P[a][b]);
      //}
      //printf("\n");
    //}
    long double WP[N];
    long double OWP[N];
    long double OOWP[N];
    for (int a=0; a<N; a++) {
      WP[a] = 1.0 * W[a] / G[a];
    }
    for (int a=0; a<N; a++) {
      //printf("* OWP[%d]\n", a);
      int n = 0;
      OWP[a] = 0.0;
      for (int b=0; b<N; b++) {
        if (P[a][b] == -1) continue;
        OWP[a] += 1.0 * (W[b] - P[b][a]) / (G[b]-1);
        //printf("==> %d %d %d %d\n", b, W[b], P[a][b], G[b]);
        n++;
      }
      //printf("[%d], %d %g\n", a, n, OWP[a]);
      OWP[a] /= n;
    }
    for (int a=0; a<N; a++) {
      int n = 0;
      OOWP[a] = 0.0;
      for (int b=0; b<N; b++) {
        if (P[a][b] == -1) continue;
        OOWP[a] += OWP[b];
        n++;
      }
      OOWP[a] /= n;
    }
    printf("Case #%d:\n", i+1);
    for (int a=0; a<N; a++) {
      //printf("%g\t%g\t%g\t%g\n", WP[a], OWP[a], OOWP[a], WP[a]/4 + OWP[a] / 2 + OOWP[a]/4);
      printf("%.6Lg\n", WP[a]/4 + OWP[a] / 2 + OOWP[a]/4);
    }
  }
  return 0;
}
