#include <stdio.h>
#include <string.h>

#define DEBUG 0

char merge['Z' + 1]['Z' + 1];
char opp['Z' + 1]['Z' + 1];

int main(int argc, char **argv) {
  int t, c, d, n, i, j, k, test, sc;
  char buf[1024];
  char s[1024];
  int count['Z' + 1];
  char m;
  scanf("%d", &t);
  for (test = 1; test <= t; test++) {

    sc = 0;
    memset(merge, 0, sizeof(merge));
    memset(opp, 0, sizeof(opp));
    memset(s, 0, sizeof(s));
    memset(count, 0, sizeof(count));
    scanf("%d", &c);
    for (i = 0; i < c; i++) {
      scanf("%s", buf);
      merge[buf[0]][buf[1]] = merge[buf[1]][buf[0]] = buf[2];
    }
    scanf("%d", &d);
    for (i = 0; i < d; i++) {
      scanf("%s", buf);
      opp[buf[0]][buf[1]] = opp[buf[1]][buf[0]] = 1;
    }
    scanf("%d", &n);
    scanf("%s", buf);
    for (i = 0; i < n; i++) {
      // Push invoke
      s[sc++] = buf[i];
      count[buf[i]]++;
      if (DEBUG) printf("Added %c to get %s %d\n", buf[i], s, sc);

      // Repeat
      while (1) {
        // Check combine
        m = merge[s[sc-1]][s[sc-2]];
        if (sc >= 2 && m) {
          if (DEBUG)  printf("Combined %c %c to get", s[sc-1], s[sc-2]);
          count[s[sc-1]]--;
          count[s[sc-2]]--;
          count[m]++;
          s[sc-2] = m;
          s[sc-1] = 0;
          sc--;
          if (DEBUG) printf(" %s %d\n", s, sc);
          continue;
        }
        else {
          // Check oppose
          for (j = 'A'; j <= 'Z'; j++) {
            if (count[j] && opp[s[sc-1]][j]) {
              for (k = 'A'; k <= 'Z'; k++) {
                count[k] = 0;
              }
              if (DEBUG) printf("Cleared on %c %c\n", s[sc-1], j);
              sc = 0;
              memset(s, 0, sizeof(s));


              break;
            }
          }
          break;
        }
      }      
    }
    printf("Case #%d: [", test);
    for (i = 0; i < sc; i++) {
      if (i != 0) {
        printf(", ");
      }
      printf("%c", s[i]);
    }
    printf("]\n");
  }
}
