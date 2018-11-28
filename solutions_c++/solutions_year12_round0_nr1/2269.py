#include <cstdio>

char alph[27] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
  FILE *inf = fopen("input2.in", "r");
  FILE *outf = fopen("output.out", "w");
  char c;
  int n;
  fscanf(inf, "%d\n", &n);
  for (int t = 1; t <= n; ++t) {
    fprintf(outf, "Case #%d: ", t);
    while (fscanf(inf, "%c", &c) == 1 && c != 10 )
      if (c != ' ') fprintf(outf, "%c", alph[c - 'a']);
      else fprintf(outf, " ");
    fprintf(outf, "\n");
  } 
  fclose(inf);
  fclose(outf);
  return 0;
}