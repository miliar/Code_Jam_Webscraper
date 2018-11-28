#include <stdio.h>
#include <stdlib.h>

int main() {
  int n, k, t, i, j, m, p, d, ii;
  int dr[8] = {0, 1, 0, -1, 1, 1, -1, -1};
  int dc[8] = {1, 0, -1, 0, 1, -1, 1, -1};
  int status;
  
  char orig[100][100];
  char rot[100][100];
  scanf("%d", &t);
  for (i = 0; i < t; i++) {
    
    status = 0;
    scanf("%d%d", &n, &k);
    for (j = 0; j < n; j++) {
      scanf("%s", orig[j]);
      //printf("%s", orig[j]);
    }
    // rotate
    for (j = 0; j < n; j++) {
      m = 0;
      for (p = n - 1; p >= 0; p--) {
        if (orig[j][p] != '.') {
          rot[m++][j] = orig[j][p];
        }
      }
      while (m < n) {
        rot[m++][j] = '.';
      }
    }
    
    
    // check for k in a row
    for (j = 0; j < n; j++) {
      for (p = 0; p < n; p++) {
        if (rot[j][p] == '.')
          continue;
        for (d = 0; d < 8; d++) {
          ii = 1;
          while (j+dr[d]*ii >= 0 && j+dr[d]*ii < n && p+dc[d]*ii >= 0 && p+dc[d]*ii < n && rot[j+dr[d]*ii][p+dc[d]*ii] == rot[j][p]) {
            ii++;
          }
          if (ii >= k) {
            if (rot[j][p] == 'R') status |= 1;
            if (rot[j][p] == 'B') status |= 2;
          }
        }
      }
    }
    char *str;
    switch (status) {
      case 0: str = "Neither"; break;
      case 1: str = "Red"; break;
      case 2: str = "Blue"; break;
      case 3: str = "Both"; break;
    }
    
    printf("Case #%d: %s\n", i + 1, str);
  }
  return 0;
}