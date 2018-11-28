#include <cstdio>
#include <cstring>

using namespace std;

#define NMAX  128

int solve() {
  int n, s, p;
  int sum[NMAX];
  int a[NMAX][NMAX];

  scanf("%d %d %d", &n, &s, &p);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &sum[i]);
  }

  memset(a[0], 0x00, (s + 1) * sizeof(a[0][0]));
  for (int i = 1; i <= n; i++) {
    int score = sum[i] / 3;
    int remain = sum[i] % 3;
    if (remain != 0) {
      score++;
    }

    int special = score;
    if (remain != 1 && sum[i] != 0) {
      special++;
    }

    a[i][0] = a[i - 1][0];
    if (score >= p) {
      a[i][0]++;
    }
    for (int j = 1; j <= s; j++) {
      a[i][j] = a[i - 1][j];
      if (score >= p) {
        a[i][j]++;
      }

      int other = a[i - 1][j - 1];
      if (special >= p) {
        other++;
      }

      if (other > a[i][j]) {
        a[i][j] = other;
      }
    }
  }

  int max = a[n][0];
  for (int j = 1; j <= s; j++) {
    if (a[n][j] > max) {
      max = a[n][j];
    }
  }

  return max;
}

int main() {
  int t;

  scanf("%d", &t);
  for (int k = 1; k <= t; k++) {
    printf("Case #%d: %d\n", k, solve());
  }

  return 0;
}

