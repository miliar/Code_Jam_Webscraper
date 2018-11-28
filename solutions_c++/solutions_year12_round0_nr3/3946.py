#include <cstdio>

char buf[256];

int pt [] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
int z[10000000];

int main () {
  int t;
  scanf ("%d", &t);
  for (int tn = 1; tn <= t; tn++) {
    int a, b;
    scanf ("%d%d", &a, &b);
    int k, ans = 0;
    for (k = 0; pt[k] < a; k++);
    for (int j = a; j <= b; j++) {
      if (j == pt[k]) ++k;
      z[j] = j;
      int s = j;
      for (int l = 0; l < k; l++) {
	s = (s % 10) * pt[k - 1] + s / 10;
	if (b >= s && s > j && z[s] != j) {
	  z[s] = j;
	  //printf ("%d %d\n", j, s);
	  ++ans;
	}
      }
    }
    printf ("Case #%d: %d\n", tn, ans);
  }
  return 0;
}
