#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char match[] = "welcome to code jam";

int main() {
  int n;

  scanf("%d\n", &n);

  int len = 501;
  char line[501];

  int mlen = strlen(match);
  int *cnt = new int[mlen];

  for (int cs=1; cs<=n; cs++) {
    fgets(line, len, stdin);

    int len = strlen(line);
    memset(cnt, 0, sizeof(int)*mlen);
    for (int i=0; i<len; i++) {
      for (int j=0; j<mlen; j++) {
        if (line[i] == match[j])
          cnt[j] = (cnt[j] + (j?cnt[j-1]:1))%10000;
      }
    }
    printf("Case #%d: %04d\n", cs, cnt[mlen-1]);
  }
  
  delete cnt;

  return 0;
}
