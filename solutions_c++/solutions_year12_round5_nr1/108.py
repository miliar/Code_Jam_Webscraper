#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define maxn 1100

int p[maxn], l[maxn], a[maxn];

int cmp (int i, int j) {
  int ci = l[i] * 100 + l[j] * p[i], cj = l[j] * 100 + l[i] * p[j];
  return make_pair (ci, i) < make_pair (cj, j);
}


int main (void) {
  int test_n;
  cin >> test_n;

  for (int test_id = 1; test_id <= test_n; test_id++) {
    printf ("Case #%d:", test_id);

    int n;
    scanf ("%d", &n);

    for (int i = 0; i < n; i++) {
      scanf ("%d", &l[i]);
    }
    for (int i = 0; i < n; i++) {
      scanf ("%d", &p[i]);
      p[i] = 100 - p[i];
    }
    for (int i = 0; i < n; i++) {
      a[i] = i;
    }

    bool flag = true;
    while (flag) {
      flag = false;
      for (int i = 0; i + 1 < n; i++) {
        if (!cmp (a[i], a[i + 1])) {
          swap (a[i], a[i + 1]);
          flag = true;
        }
      }
    }

    for (int i = 0; i < n; i++) {
      printf (" %d", a[i]);
    }
    printf ("\n");
  }

  return 0;
}