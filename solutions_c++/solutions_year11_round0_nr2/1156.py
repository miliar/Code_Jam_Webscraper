#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

char comb[256][256], opp[256];

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i: ", numcase);

    int numcomb, numopposed, n;
    char str[128];
    memset(comb, 0, sizeof(comb));
    memset(opp, 0, sizeof(opp));

    scanf("%i", &numcomb);
    for (int i = 0; i < numcomb; ++i) {
      scanf(" %s", str);
      comb[str[0]][str[1]] = comb[str[1]][str[0]] = str[2];
    }

    scanf("%i", &numopposed);
    for (int i = 0; i < numopposed; ++i) {
      scanf(" %s", str);
      opp[str[0]] = str[1];
      opp[str[1]] = str[0];
    }

    scanf("%i %s", &n, str);
    int len = 0;
    for (int i = 0; i < n; ++i) {
      str[len++] = str[i];
      if (len > 1) {
        char c = comb[str[len - 2]][str[len - 1]];
        if (c != 0) { str[len - 2] = c; --len; }

        c = opp[str[len - 1]];
        if (c != 0 && find(&str[0], &str[len], c) != &str[len]) len = 0;
      }
    }
    printf("[");
    for (int i = 0; i < len; ++i) {
      if (i > 0) printf(", ");
      printf("%c", str[i]);
    }
    printf("]\n");
  }
  return 0;
}
