#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#define MAX 110
#define DEBUG 0

int main() {
  int kases;
  scanf("%d", &kases);
  for (int i = 1; i <= kases; i++) {
    int N;
    scanf("%d", &N);
    char matrix[MAX][MAX] = {'\0'};
    for (int a = 0; a < N; a++) 
      scanf("%s", matrix[a]);
#if DEBUG
  for (int q = 0; q < N; q++) {
    printf("%s\n", matrix[q]);
  }
#endif
    // Input over
    double wp[MAX] = {0}, owp[MAX] = {0}, oowp[MAX] = {0};
    double RPI = 0.0;
    int number[MAX] = {0};

    for (int a = 0; a < N; a++) {
      for (int b = 0; b < N; b++) {
        if (matrix[a][b] != '.')
          number[a]++;
        if (matrix[a][b] == '1')
          wp[a]++;
      }
      wp[a] /= number[a];
#if DEBUG
  printf("wp[%d] = %.2lf, matches = %d\n", a+1, wp[a], number[a]);
#endif
    }

    for (int a = 0; a < N; a++) {
      for (int b = 0; b < N; b++) {
        if (matrix[a][b] != '.') {
          double add = wp[b]*number[b];
          if (matrix[b][a] == '1')
            add -= 1;
          add /= (number[b]-1);
          owp[a] += add;
        }
      }
      owp[a] /= number[a];
#if DEBUG
  printf("owp[%d] = %.2lf, matches = %d\n", a+1, owp[a], number[a]);
#endif
    }

    for (int a = 0; a < N; a++) {
      for (int b = 0; b < N; b++) {
        if (matrix[a][b] != '.') {
          oowp[a] += owp[b];
        }
      }
      oowp[a] /= number[a];
#if DEBUG
  printf("oowp[%d] = %.2lf, matches = %d\n", a+1, oowp[a], number[a]);
#endif
    }

    printf("Case #%d:\n", i);
    for (int a = 0; a < N; a++) {
      printf("%lf\n", 0.25*wp[a] + 0.50*owp[a]+ 0.25*oowp[a]);
    }
  }
}
