#include <stdio.h>
#include <math.h>

int main() {
  int ncs;

  scanf("%d", &ncs);

  for (int cs = 0; cs<ncs; cs++) {
    int n, k;
    scanf("%d %d", &n, &k);

    int pn = pow(2,n);
    printf("Case #%d: %s\n", cs+1, (k % pn == pn-1) ? "ON" : "OFF");
  }

  return 0;
}

