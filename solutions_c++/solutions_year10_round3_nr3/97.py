#include <algorithm>
#include <cstdio>

using namespace std;

const int kMaxN = 512 + 5;

int M, N;
int b[kMaxN][kMaxN];
int cnt[kMaxN];

void Cut(int m, int n, int si, int sj, int len) {
  for (int i = si; i < si + len; ++i)
    fill(b[i] + sj, b[i] + sj + len, -1);
}

int Solve(int m, int n, int top) {
  int max_l = 0;
  int mi, mj;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (b[i][j] == -1) continue;
      int l = 1, flag = 1;
      for (; flag && l < top; ++l) {
        if (i + l >= m || j + l >= n) break;
        if (b[i + l][j + l] == -1) break;
        if (b[i + l][j + l] != b[i + l - 1][j + l - 1]) break;
        for (int ii = i + l - 1, jj = j + l; ii >= i; --ii)
          if (b[ii][jj] == -1 || b[ii][jj] == b[ii + 1][jj]) {
            flag = 0;
            break;
          }
        if (flag == 0) break;
        for (int ii = i + l, jj = j + l - 1; jj >= j; --jj)
          if (b[ii][jj] == -1 || b[ii][jj] == b[ii][jj + 1]) {
            flag = 0;
            break;
          }
        if (flag == 0) break;
      }
      if (max_l < l) {
        max_l = l;
        mi = i;
        mj = j;
      }
    }
  }
  Cut(m, n, mi, mj, max_l);
  return max_l;
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    scanf("%d %d", &M, &N);
    fill(cnt, cnt + min(N, M) + 1, 0);
    for (int i = 0; i < M; ++i) {
      for (int j = 0; j < N / 4; ++j) {
        int digit;
        scanf("%1x", &digit);
        for (int k = 0; k < 4; ++k, digit /= 2)
          b[i][j * 4 + 3 - k] = digit % 2;
      }
    }
    int maximal = min(M, N);
    for (int area = 0; area < M * N;) {
      maximal = Solve(M, N, maximal);
      ++cnt[maximal];
      area += maximal * maximal;
    }
    int num = 0;
    for (int i = min(M, N); i > 0; --i)
      if (cnt[i] > 0)
        ++num;
    printf("%d\n", num);
    for (int i = min(M, N); i > 0; --i)
      if (cnt[i] > 0)
        printf("%d %d\n", i, cnt[i]);
  }
  return 0;
}
