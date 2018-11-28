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

char w[10005][11];
char s[30];

int cmask[10005];
int c[10005];
int p[10005];
int ans[10005];

int cmp (int i, int j) {
  return cmask[i] < cmask[j] || (cmask[i] == cmask[j] && i < j);
}

int main(void) {
  int tn, nt;
  scanf("%d", &nt);
  s[0] = '_';
  for (tn=1; tn<=nt; tn++) {
    fprintf (stderr, "Case #%d:\n", tn);
    printf ("Case #%d:", tn);

    int n, m;
    scanf("%d%d", &n, &m);
    for (int i=0; i<n; i++) {
      scanf("%s", w[i]);
      int l = strlen(w[i]);
      for (int j=l-1; j >= 0; j--)
        w[i][j-l+10] = w[i][j];
      for (int j=9-l; j >= 0; j--)
        w[i][j] = '_';
    }
    for (int t=0; t<m; t++) {
      for (int i=0; i<n; i++) {
        p[i] = i;
        c[i] = 0;
        ans[i] = 0;
      }

      scanf("%s", s+1);
      assert (strlen(s) == 27);

      int newc = 0;
      for (int C=0; C<27; C++) {
        for (int j=0; j<n; j++) {
          int mask = 0;
          for (int i=0; i<10; i++)
            mask |= (w[j][i] == s[C]) << i;
          cmask[j] = mask;
        }

        for (int j=0; j<n; ) {
          int k=j;
          int was = 0;
          while (k < n && c[p[j]] == c[p[k]]) {
            was |= cmask[p[k]];
            k++;
          }

          if (was != 0) {
            sort(p+j, p+k, cmp);
            for (int i=j; i<k; i++)
              if (i != j && cmask[p[i]] == cmask[p[i-1]])
                c[p[i]] = c[p[i-1]];
              else
                c[p[i]] = newc++;
            if (C) {
              for (int i=j; i<k; i++)
                if (cmask[p[i]] == 0) {
                  ans[p[i]]++;
                }
            }
          }

          j=k;
        }

      }
      int best = 0;
      for (int i=0; i<n; i++) {
        if (ans[i] > ans[best])
          best = i;
      }

      int l = 0;
      while (w[best][l] == '_') l++;
      printf(" %s", w[best]+l);
    }
    puts("");
  }

  return 0;
}
