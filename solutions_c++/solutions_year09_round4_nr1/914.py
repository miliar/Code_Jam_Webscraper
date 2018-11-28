#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define For(i, x) for (int i = 0; i < (int)x; i++)

typedef vector<int> vi;

const int N = 40;

int calc(int n, char g[][N]) {
  int cnt = 0;

  vi v;
  For(i, n) {
    int last = 0;
    For(j, n) {
      if (g[i][j] == '1')
        last = j;
    }
    v.push_back(last);
  }

  For(i, n) {
    if (v[i] > i) {
      int x = i;
      int p = -1;
      for (int j = i+1; j < n; j++) {
        if (v[j] <= x) {
          p = j;
          break;
        }
      }
      assert(p != -1);

      for (int j = p; j > i; j--) {
        cnt++;
        swap(v[j], v[j-1]);
      }
    }
  }

  return cnt;
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int cc = 0; cc < ncases; cc++) {
    int n;
    scanf("%d", &n);
    char g[N][N];
    For(i, n)
      scanf("%s", &g[i][0]);

    printf("Case #%d: %d\n", cc+1, calc(n, g));
  }
}

