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

char s[10005];
int a[40][40];
int degi[40];
int dego[40];
int mark[40];

char *t = "oieastbg";

void add(int n1, int n2) {
  if (!a[n1][n2]) {
    degi[n2]++;
    dego[n1]++;
    a[n1][n2] = 1;
  }
}

int main(void) {
  int tn, nt;
  scanf("%d", &nt);
  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    int k;
    scanf("%d\n", &k);
    assert (k == 2);
    gets(s);

    memset (a, 0, sizeof(a));
    memset (degi, 0, sizeof(degi));
    memset (dego, 0, sizeof(dego));
    for (int i = 0; s[i + 1]; i++) {
      int n11 = s[i] - 'a';
      int n21 = s[i + 1] - 'a';
      int n12 = strchr (t, s[i]) != NULL ? strchr (t, s[i]) - t + 'z' - 'a' + 1 : n11;
      int n22 = strchr (t, s[i + 1]) != NULL ? strchr (t, s[i + 1]) - t + 'z' - 'a' + 1 : n21;

      add(n11, n21);
      add(n12, n21);
      add(n11, n22);
      add(n12, n22);
    }
    int sx = 0, sy = 0, sz = 0;
    for (int i = 0; i < 34; i++) {
      if (degi[i] > dego[i]) {
        sx += degi[i] - dego[i];
      } else {
        sy -= degi[i] - dego[i];
      }
      sz += max (degi[i], dego[i]);
    }
    assert (sx == sy);
    if (sx > 0) {
      sz--;
    }
    printf ("%d\n", sz + 1);
  }

  return 0;
}
