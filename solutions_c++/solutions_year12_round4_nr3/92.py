#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

#define maxn 2010

int ne[maxn], h[maxn]; 
vector <int> rev[maxn];

void go (int v, double sdv) {
  for (int i = 0; i < (int)rev[v].size(); i++) {
    int u = rev[v][i];
    double x = h[v] - sdv * (v - u);
    h[u] = x;
    if (fabs (x - h[u]) < 1e-9 || 1) {
      h[u]--;
    }
    assert (h[u] >= 0);
    sdv = (double)(h[v] - h[u]) / (v - u);
    go (u, sdv);
  }
} 

int main (void) {
  int test_n;
  scanf ("%d", &test_n);

  for (int test_id = 1; test_id <= test_n; test_id++) {
    printf ("Case #%d: ", test_id);

    int n;
    scanf ("%d", &n);
    for (int i = 1; i < n; i++) {
      scanf ("%d", &ne[i]);
      rev[ne[i]].push_back (i);
    }
//    fprintf (stderr, "test_id = %d [n = %d]\n", test_id, n);

    int must_fail = 0;

    for (int i = 1; i < n; i++) {
      for (int j = i + 1; j < ne[i]; j++) {
        if (ne[j] > ne[i]) {
          must_fail = 1;
        }
      } 
    }

    h[n] = 10000000;
    go (n, 0);

    for (int i = 1; i <= n; i++) {
      rev[i].clear();
    }

    int failed = 0;

    for (int i = 1; i < n; i++) {
      int t = i + 1;
      for (int j = i + 2; j <= n; j++) {

        long long x = t - i, y = h[t] - h[i],
           nx = j - i,ny = h[j] - h[i];
        if (x * ny - y * nx > 0) {
          t = j;
        }
      }
      if (t != ne[i]) {
        failed = 1;
      }
    }

    assert (failed == must_fail);


    if (failed) {
      printf ("Impossible\n");
    } else {
      for (int i = 1; i <= n; i++) {
        printf ("%d%c", h[i], " \n"[i == n]);
      }
    }
    
  }

  return 0;
}