#include <cstdio>
#include <cstring>
#include <cstdlib>

char map[55][55];

int main() {
    int t, r, c, i, j, b, a = 1;
    scanf("%d", &t);
    while (t--) {
          scanf("%d %d", &r, &c);
          b = 0;
          for (i = 0; i < r; i++) {
              scanf("%s", map[i]);
              for (j = 0; j < c; j++)
                  b += map[i][j] == '#';
          }
          printf("Case #%d:\n", a++);
          if (b % 4 != 0)
             printf("Impossible\n");
          else {
               for (i = 0; i < r - 1; i++) {
                   for (j = 0; j < c - 1; j++)
                       if (map[i][j] == '#' && map[i][j + 1] == '#' && map[i + 1][j] == '#' && map[i + 1][j + 1] == '#')
                          map[i][j] = map[i + 1][j + 1] = '/', map[i][j + 1] = map[i + 1][j] = '\\', b -= 4;
               }
               
               if (b) printf("Impossible\n");
               else
                   for (i = 0; i < r; i++)
                       printf("%s\n", map[i]);
          }
    }
    return 0;
}
