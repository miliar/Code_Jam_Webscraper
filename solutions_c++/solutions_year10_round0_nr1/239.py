#include <stdio.h>

void Solve(FILE *fin, FILE *fout) {
  unsigned int n, k;
  fscanf(fin, "%u %u", &n, &k);
  unsigned int p = ((1 << n) - 1);
  if ((k & p) == p) fprintf(fout, "ON\n");
  else fprintf(fout, "OFF\n");
}

int main() {
  FILE *fin = fopen("input.txt", "r");
  FILE *fout = fopen("output.txt", "w");
  
  int test_cases_num;
  fscanf(fin, "%d", &test_cases_num);
  for (int i = 0; i < test_cases_num; ++i) {
    fprintf(fout, "Case #%d: ", i+1);
    Solve(fin, fout);
  }

  fclose(fout);
  return 0;
}
