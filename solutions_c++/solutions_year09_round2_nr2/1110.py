#include <stdio.h>
#include <string.h>

#include <algorithm>

using namespace std;

int main() {
  int t;
  scanf("%d", &t);

  for (int x = 1; x <= t; x++) {
    char line[64];
    int llen;
    
    scanf("%s", line);
    llen = strlen(line);

    if (!next_permutation(line, line+llen)) {
      sort(line, line+llen);

      char copy[64];
      // find first non-zero digit
      int i, j;
      for (i = 0; line[i] && line[i]=='0'; i++);
      copy[0] = line[i];
      // copy zeros
      for (i = 0, j = 1; line[i] && line[i]=='0'; i++,j++) {
        copy[j] = line[i];
      }
      copy[j++] = '0'; // add another zero.
      // copy the rest
      for (++i; line[i]; i++, j++) {
        copy[j] = line[i];
      }
      copy[j] = 0;
      strcpy(line, copy);
    }

    printf("Case #%d: %s\n", x, line);
  }
  return 0; 
}
