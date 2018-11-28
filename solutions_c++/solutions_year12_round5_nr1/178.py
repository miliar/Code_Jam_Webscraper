#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

pair <double, int> s[2000];
int L[2000], P[2000];

int main () {
  int tn;
  scanf ("%d", &tn);
  for (int tc = 1; tc <= tn; tc++) {
    int n;
    scanf ("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf ("%d", &L[i]);
    }
    for (int i = 0; i < n; i++) {
      scanf ("%d", &P[i]);
    }
    for (int i = 0; i < n; i++) {
      s[i].second = i;
      s[i].first = L[i] * 100.0 / P[i];
    }
    printf ("Case #%d: ", tc);
    sort (s, s + n);
    for (int i = 0; i < n; i++) {
      printf ("%d%c", s[i].second, (i < n - 1) ? ' ' : '\n');
    }
  }
  return 0;
}
