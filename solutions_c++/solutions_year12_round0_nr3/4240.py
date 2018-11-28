#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  int T;
  char buf1[100], buf2[100];
  scanf("%d\n", &T);

  for (int cas = 1; cas <= T; cas++) {
    int a,b;
    scanf("%d %d\n", &a, &b);
    int count = 0;

    for (int i = a; i <=b; i++) {
      for (int j = i + 1; j <= b; j++) {
        sprintf(buf1, "%d", i);
        sprintf(buf2, "%d", j);

        int len1 = strlen(buf1);
        int len2 = strlen(buf2);

        if (len1 == len2) {
          for (int k = 0; k < len1; k++) {
            int l = 0;
            for (; l < len1; l++) {
              if (buf1[l] != buf2[(l + k) % len1]) {
                break;
              }
            }

            if (l == len1) {
              count++;
              break;
            }
          }
        }
      }
    }

    printf("Case #%d: %d\n", cas, count);
  }

  return 0;
}
