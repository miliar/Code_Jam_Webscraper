#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int D[15000], L[15000], X[15000];
int n;


int main () {
  int tn;
  scanf ("%d", &tn);
  for (int tc = 1; tc <= tn; tc++) {
    scanf ("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf ("%d%d", &D[i], &L[i]);
    }
    scanf ("%d", &D[n]);
    L[n] = 0;
    for (int i = 0; i <= n; i++) X[i] = -1;
    X[0] = D[0];
    for (int i = 0; i < n; i++) 
      if (X[i] >= 0) {
	//	printf ("%d: %d\n", i, X[i]);
	for (int j = i + 1; j <= n; j++)
	  if (D[i] + X[i] >= D[j]) {
	    if (min (D[j] - D[i], L[j]) > X[j])
	      X[j] = min (D[j] - D[i], L[j]);
	  } else break;
      }
    printf ("Case #%d: %s\n", tc, X[n] >= 0  ? "YES" : "NO");
  }
  return 0;
}
