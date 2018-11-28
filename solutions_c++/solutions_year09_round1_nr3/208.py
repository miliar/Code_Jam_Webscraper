#include <cstdio>
#include <cstring>

const int MAXC = 50;
const int MAX_DEEP = 1000;

int c, n;
double memo1[MAXC][MAX_DEEP];

double memo2[MAXC][MAXC][MAXC][MAXC];
double gogo(int A, int B, int N, int X) {
  if (A<0||B<0||X<0) return 0;
  double &ref = memo2[A][B][N][X];  
  if (ref < 0) {
    if (N == 0) {
      if (X==0) return 1;
      return 0;
    }
    ref = 0;
    if (X>0) ref = double(A)/(A+B) * gogo(A-1, B, N - 1, X - 1);
    ref += double(B)/(A+B) * gogo(A, B-1, N - 1, X);
  }
  return ref;
}

double prob(int have, int newcards) {
  return gogo(c - have, have, n, newcards);
}

double go(int have, int deep = 0) {
  //printf("%d %d\n", have, deep);
  if (deep == MAX_DEEP) return 0;
  if (have == c) return deep;

  double &ref = memo1[have][deep];

  if (ref < 0) {
    ref = 0;
    int A = c - have, B = have;
    for (int i = n > A ? A : n; i >= 0; --i) {
      //printf("%d %d %lf\n", have, i, prob(have,i));
      ref += prob(have, i) * go(have + i, deep + 1);
    }
  }

  return ref;
}

int main() {
  int n_tests;

  scanf("%d", &n_tests);
  for (int test = 1; test <= n_tests; ++test) {
    fprintf(stderr,"%d\n", test);
    scanf("%d %d", &c, &n);
    for (int i = 0; i < MAXC; ++i) {
      for (int d = 0; d < MAX_DEEP; ++d) { 
      memo1[i][d] = -1;
      }
    }
  for (int a = 0; a <= c; ++a) {
    for (int b = 0; b <= c; ++b) {
      for (int i = 0; i <= c; ++i) {
        for (int j = 0; j <= c; ++j) {
          memo2[a][b][i][j] = -1;
        }
      }
    }
  }

    printf("Case #%d: %.10lf\n", test, go(0));
  }

  return 0;
}
