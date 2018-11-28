#include <stdio.h>
#include <stdlib.h>

int main() {
  FILE *fin = fopen("A-large.in", "r");
  FILE *fout = fopen("A-large.out", "w");
  unsigned int t, n, k, i, j;
  fscanf(fin, "%d", &t);
  for (i = 0; i < t; i++) {
    fscanf(fin, "%d%d", &n, &k);
    j = 1;
    j = (j << n) - 1;
    fprintf(fout, "Case #%d: %s\n", i + 1, ((k & j) == j) ? "ON" : "OFF");
  }
  fclose(fin);
  fclose(fout);
  return 0;
}