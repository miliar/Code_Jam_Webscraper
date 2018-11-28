#include <cstdio>
#include <cmath>

#define min(a, b) ((a) < (b) ? (a) : (b))
#define T 0.0000001

char m[10][11];

bool check(int k, int i, int j) {
     double cx = (2 * i + k - 1) / 2.0, cy = (2 * j + k - 1) / 2.0;
     double sx = 0, sy = 0;
     int a, b;
     for (a = i; a < i + k; a++)
     for (b = j; b < j + k; b++) {
         sx += m[a][b] * (a - cx);
         sy += m[a][b] * (b - cy);
     }
     
     sx -= m[i][j] * (i - cx) + m[i][j + k - 1] * (i - cx) + m[i + k - 1][j] * (i + k - 1 - cx) + m[i + k - 1][j + k - 1] * (i + k - 1 - cx);
     sy -= m[i][j] * (j - cy) + m[i][j + k - 1] * (j + k - 1 - cy) + m[i + k - 1][j] * (j - cy) + m[i + k - 1][j + k - 1] * (j + k - 1 - cy);
     
     // printf("[%d %d %d %lf %lf]", k, i, j, sx, sy);
     
     return fabs(sx) < T && fabs(sy) < T;
}

int main() {
    int t, r, c, d, a = 1;
    int i, j, k;
    scanf("%d", &t);
    loop: while (t--) {
          scanf("%d %d %d ", &r, &c, &d);
          for (i = 0; i < r; i++)
              gets(m[i]);
          for (k = min(r, c); k >= 3; k--)
          for (i = 0; i <= r - k; i++)
          for (j = 0; j <= c - k; j++)
              if (check(k, i, j)) {
                 printf("Case #%d: %d\n", a++, k);
                 goto loop;
              }
          printf("Case #%d: IMPOSSIBLE\n", a++);
          
    }
    return 0;
}
