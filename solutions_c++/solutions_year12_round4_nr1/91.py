#include <cstdio>

#define maxn 10010

int d[maxn], l[maxn], nl[maxn];

int main (void) {
  int test_n;
  scanf ("%d", &test_n);

  int test_id;
  for (test_id = 1; test_id <= test_n; test_id++) {
    printf ("Case #%d: ", test_id);

    int n;
    scanf ("%d", &n);
    for (int i = 1; i <= n; i++) {
      scanf ("%d%d", &d[i], &l[i]);
    }

    d[0] = 0;
    l[0] = d[1];
    nl[0] = d[1];

    for (int i = 1; i <= n + 1; i++) {
      nl[i] = -1;
    }

    int D;
    scanf ("%d", &D);

    int f = 0; 

    for (int i = 0; i <= n; i++) {
      if (nl[i] != -1) {
        if (d[i] + nl[i] >= D) {
          f = 1;
          break;
        }
        
        for (int j = i + 1; j <= n; j++) {
          int cur_d = d[j] - d[i];
          if (nl[i] >= cur_d) {
            if (cur_d > l[j]) {
              cur_d = l[j];
            }
            if (nl[j] < cur_d) {
              nl[j] = cur_d;
            }
          } 
        }
      }
    }
    printf (f ? "YES\n" : "NO\n");

  }

  return 0;
}