#include <stdio.h>
#include <string.h>

int solve(char line[]) {
  const char needle[] = "welcome to code jam";
  int k = strlen(needle);
  int n_ways[1024][64];
  for (int i = 0; i <= k; i++) {
    n_ways[0][i] = i == 0;
  }
 
  int n = strlen(line);
  for (int j = 1; j <= n; j++) {
    //    printf("%d: %c: ", j, line[j - 1]);
    for (int i = 0; i <= k; i++) {
      n_ways[j][i] = n_ways[j - 1][i];    
      if (i > 0 && line[j - 1] == needle[i - 1])
	n_ways[j][i] += n_ways[j - 1][i - 1];
      n_ways[j][i] %= 10000;
      //      printf("%5d", n_ways[j][i]);
    }
    //    printf("\n");
  }
  return n_ways[n][k];
}

int main(void) {
  int N;
  scanf("%d\n", &N);
  for (int i = 0; i < N; i++) {
    char line[1024];
    gets(line);
    int r = solve(line);
    printf("Case #%d: %04d\n", i + 1, r);
  }
}
