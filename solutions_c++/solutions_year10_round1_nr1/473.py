#include <cstdio>
#include <vector>
#include <string>
using namespace std;

bool check(char D[100][100], int N, int K, char c)
{
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j + K <= N; ++j) {
      int k = 0;
      for (; k < K; ++k)
	if (D[i][j + k] != c) break;
      if (k == K) return true;
    }
  }

  for (int i = 0; i + K <= N; ++i) {
    for (int j = 0; j < N; ++j) {
      int k = 0;
      for (; k < K; ++k)
	if (D[i + k][j] != c) break;
      if (k == K) return true;
    }
  }

  for (int i = 0; i + K <= N; ++i) {
    for (int j = 0; j + K <= N; ++j) {
      int k = 0;
      for (; k < K; ++k)
	if (D[i + k][j + k] != c) break;
      if (k == K) return true;
    }
  }

  for (int i = 0; i + K <= N; ++i) {
    for (int j = K - 1; j < N; ++j) {
      int k = 0;
      for (; k < K; ++k)
	if (D[i + k][j - k] != c) break;
      if (k == K) return true;
    }
  }

  return false;
}

const char *f(int N, int K, char C[100][100])
{
  char D[100][100];
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      double cx = (N - 1) * 0.5, cy = (N - 1) * 0.5;
      double x = j - cx, y = i - cy;
      double xx = y, yy = -x;
      int ii = (int)(cy + yy), jj = (int)(cx + xx);
      // printf("%d %d -> %d %d\n", i, j, ii, jj);
      D[i][j] = C[ii][jj];
    }
  }

  char E[100][100];
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      E[i][j] = '.';
  for (int j = 0; j < N; ++j) {
    int i  = N;
    for (int ii = N - 1; ii >= 0; --ii)
      if (D[ii][j] != '.')
	E[--i][j] = D[ii][j];
  }

//   for (int i = 0; i < N; ++i)
//     printf("%s\n", E[i]);
//   printf("\n");

  if (check(E, N, K, 'R')) {
    if (check(E, N, K, 'B')) {
      return "Both";
    }
    return "Red";
  }
  if (check(E, N, K, 'B'))
    return "Blue";

  return "Neither";
}

int main()
{
  int T;
  scanf(" %d", &T);
  for (int i = 1; i <= T; ++i) {
    int N, K;
    char C[100][100];
    scanf(" %d %d", &N, &K);
    for (int j = 0; j < N; ++j) {
      scanf(" %s", C[j]);
    }

    printf("Case #%d: %s\n", i, f(N, K, C));
  }

  return 0;
}
