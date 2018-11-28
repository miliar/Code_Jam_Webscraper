#include <stdio.h>

int main() {
    int t, n, cur_pos;
    long int r, k, g[1000], rest_places, i, j, steps;
    __int64 answer;
    FILE *fin, *fout;
    fin = fopen("small.in", "r");
    fout = fopen("small.out", "w");
    fscanf(fin, "%d", &t);
    for(i=1;i<=t;i++) {
      fscanf(fin, "%ld%ld%d", &r, &k, &n);
      for (j=0;j<n;j++) fscanf(fin, "%ld", &g[j]);
      answer = 0;
      cur_pos = 0;
      for(j=0;j<r;j++) {
        steps = 0;
        rest_places = k;
        while(rest_places - g[cur_pos] >= 0 && steps < n) {
          rest_places -= g[cur_pos];
          answer += g[cur_pos];
          cur_pos ++;
          steps++;
          if (cur_pos == n) cur_pos = 0;
        }
      }
      fprintf(fout, "Case #%d: %I64d\n", i, answer);
    }
    fclose(fout);
    fclose(fin);
    return 0;
}
      
