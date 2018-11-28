#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

#define maxn 210
#define st 50

int a[maxn][maxn], h[maxn], w[maxn];

int get(int xa, int ya, int xb, int yb) {
  xa += st;
  ya += st;
  xb += st;
  yb += st;
  while (a[xa][ya] != -1 && a[xb][yb] != -1) {
    if (a[xa][ya] != a[xb][yb]) {
      return false;
    }
    xa--, ya--;
    xb++, yb++;
  }
  return true;
}

int get2(int xa, int ya, int xb, int yb) {
  xa += st;
  ya += st;
  xb += st;
  yb += st;
  while (a[xa][ya] != -1 && a[xb][yb] != -1) {
    if (a[xa][ya] != a[xb][yb]) {
      return false;
    }
    xa--, ya++;
    xb++, yb--;
  }
  return true;

}

int f(int k) {
  return k * k;
}

int main (void) {
  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++) {
    printf("Case #%d: ", tt);

    memset(a, -1, sizeof(a));

    int n;
    cin >> n;
    for (int t = 0; t < n; t++) {
      for (int i = t, j = 0; j <= t; i--, j++) {
        cin >> a[i + st][j + st];
      }
    }
    for (int t = 1; t < n; t++) {
      for (int i = n - 1, j = t; j < n; i--, j++) {
        cin >> a[i + st][j + st];
      }
    }
/*    
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        fprintf(stderr, "%d %c", a[i + st][j + st], " \n"[j + 1 == n]);
      }
    }
    fprintf(stderr, "\n");
*/

    for (int i = 0; i < 2 * n; i++) {
      w[i] = 1;
      h[i] = 1;
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        w[i + j + 1] &= get(i, j, i + 1, j + 1);
        w[i + j] &= get(i - 1, j - 1, i + 1, j + 1);
        h[i - j + n - 1 + 1] &= get2(i, j, i + 1, j - 1);
        h[i - j + n - 1] &= get2(i - 1, j + 1, i + 1, j - 1);
      }
    }
    int res = 100000;

    for (int i = 0; i <= 2 * n - 2; i++) {
      for (int j = 0; j <= 2 * n - 2; j++) {
        if (w[i] && h[j]) {
          res = min(res, f(n + abs(i - n + 1) + abs(j - n + 1)) - f(n));
        }
      }
    }

    printf("%d\n", res);
  }

  return 0;
} 