#include <cassert>
#include <cstdio>
#include <map>
#include <set>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int L[1005];
int P[1005];
int p[1005];

bool cmp(int i, int j) {
  return L[i] * P[j] < L[j] * P[i] || (L[i] * P[j] == L[j] * P[i] && i < j);
}

int main(void) {
  int tn, nt;
  scanf("%d", &nt);
  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d:", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
      scanf("%d", &L[i]);
    for (int i = 0; i < n; i++)
      scanf("%d", &P[i]);
    for (int i = 0; i < n; i++)
      p[i] = i;

    sort (p, p + n, cmp);

    for (int i = 0; i < n; i++)
      printf(" %d", p[i]);
    printf ("\n");
  }

  return 0;
}
