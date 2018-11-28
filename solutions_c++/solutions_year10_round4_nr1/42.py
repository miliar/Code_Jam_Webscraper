#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
using namespace std;

int a[200][200];
int b[200][200];
int pb[200];

int find_axis(int k, int a[200][200]) {
  for (int i = 0; i < k; i++) {
    for (int s = 0; s < 2; s++) {
      int x = s ? -i : i;
      int l = x - 1;
      int u = x + 1;
      bool symmetric = true;
      for (; l >= -(k - 1) && u <= k - 1; l--, u++) {
        int nl = k - abs(l);
        int nu = k - abs(u);
        int n = min(nl, nu);
        int sl = nl < nu ? 0 : (nl - nu) / 2;
        int su = nu < nl ? 0 : (nu - nl) / 2;
        for (int j = 0; j < n; j++) {
          if (a[l + k][sl + j] != a[u + k][su + j]) {
            symmetric = false;
            break;
          }
        }
        if (!symmetric) {
          break;
        }
      }
      if (symmetric) {
        return x;
      }
    }
  }
  assert(0);
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int k;
    cin >> k;
    for (int i = -(k - 1); i < k; i++) {
      pb[i + k] = 0;
    }
    for (int i = -(k - 1); i <= 0; i++) {
      int r = -(k - (-i) - 1);
      for (int j = 0; j < k - (-i); j++) {
        cin >> a[i + k][j];
        b[r + k][pb[r + k]++] = a[i + k][j];
        r += 2;
      }
    }
    for (int i = 1; i < k; i++) {
      int r = -(k - i - 1);
      for (int j = 0; j < k - i; j++) {
        cin >> a[i + k][j];
        b[r + k][pb[r + k]++] = a[i + k][j];
        r += 2;
      }
    }
    int x = find_axis(k, a);
    int y = find_axis(k, b);
    int k2 = k + abs(x) + abs(y);
    int z = k2 * k2 - k * k;
    cout << "Case #" << t << ": " << z << endl;
  }
}
