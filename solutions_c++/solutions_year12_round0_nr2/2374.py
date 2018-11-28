#include <cstdio>

int main() {
  FILE *inf = fopen("input2.in", "r");
  FILE *outf = fopen("output.out", "w");
  int num_tests;

  fscanf(inf, "%d\n", &num_tests);
  for (int t = 1; t <= num_tests; ++t) {
    int N, S, p, r, res = 0;
    fscanf(inf, "%d %d %d", &N, &S, &p);
    for (int i = 1; i <= N; ++i) {
      fscanf(inf, "%d", &r);
      if ((r + 2) / 3 >= p) {
        ++res;
      } else {
        if ((r + 4) / 3 >= p && S > 0 && r > 1) {
          ++res; 
          --S;
        }
      }
     }
    fprintf(outf, "Case #%d: %d\n", t, res);
  } 
  fclose(inf);
  fclose(outf);
  return 0;
}