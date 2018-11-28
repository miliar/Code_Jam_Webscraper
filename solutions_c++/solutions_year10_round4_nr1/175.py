#include <algorithm>
#include <cstdio>

using namespace std;

const int kInf = 200000000;
const int kMaxS = 256;

int k;
char ch[kMaxS][kMaxS];

bool In(int k, int i, int j) {
  if (i <= k) {
    return (j > k - i) && (j < k + i);
  } else if (i < 2 * k) {
    return (j > i - k) && (j < 3 * k - i);
  }
  return false;
}

int Try(int k, int si, int sj) {
  for (int i = 1; i <= si; ++i)
    for (int j = 1; j <= sj; ++j)
      if (In(k, i, j) && ch[i][j] != ' ') {
        int ii = 2 * si - i;
        int jj = j;
        if (In(k, ii, jj) && ch[ii][jj] != ' ') {
          if (ch[ii][jj] != ch[i][j])
            return -1;
        }
        ii = i;
        jj = 2 * sj - j;
        if (In(k, ii, jj) && ch[ii][jj] != ' ') {
          if (ch[ii][jj] != ch[i][j])
            return -1;
        }
      }
  for (int i = si; i < 2 * k; ++i)
    for (int j = sj; j < 2 * k; ++j)
      if (In(k, i, j) && ch[i][j] != ' ') {
        int ii = i;
        int jj = 2 * sj - j;
        if (In(k, ii, jj) && ch[ii][jj] != ' ') {
          if (ch[ii][jj] != ch[i][j])
            return -1;
        }
        ii = 2 * si - i;
        jj = j;
        if (In(k, ii, jj) && ch[ii][jj] != ' ') {
          if (ch[ii][jj] != ch[i][j])
            return -1;
        }
      }

  if (si > k) si = 2 * k - si;
  if (sj > k) sj = 2 * k - sj;
  int len = 3 * k - si - sj;
  return len * len - k * k;
}

int main() {
  char buf[10];
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    int totalmin = kInf;
    scanf("%d", &k);
    for (int i = 1; i <= k; ++i) {
      fill(ch[i], ch[i] + 2 * k, ' ');
      for (int j = k - i + 1; j < k + i; j += 2) {
        scanf("%s", buf);
        ch[i][j] = buf[0];
      }
      //printf("\n%s\n", ch[i]);
    }
    for (int i = k + 1; i <= 2 * k - 1; ++i) {
      fill(ch[i], ch[i] + 2 * k, ' ');
      for (int j = i - k + 1; j < 3 * k - i; j += 2) {
        scanf("%s", buf);
        ch[i][j] = buf[0];
      }
      //printf("\n%s\n", ch[i]);
    }
    for (int i = 1; i <= 2 * k - 1; ++i)
      for (int j = 1; j <= 2 * k - 1; ++j) {
        int t = Try(k, i, j);
        if (t == -1) continue;
        totalmin = min(totalmin, t);
        //printf("%d %d %d\n", i, j, t);
      }
    printf("%d\n", totalmin);
  }
  return 0;
}
