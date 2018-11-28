#include <cstdio>
#include <string>

using namespace std;

const int MAX_N = 110;
char combine[0x100][0x100];
bool opposed[0x100][0x100];

int main() {
  int nCases, n;
  char c1, c2, c3, s[MAX_N + 1], t[MAX_N + 1];
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    for (int i = 'A'; i <= 'Z'; i++) {
      for (int j = 'A'; j <= 'Z'; j++) {
        combine[i][j] = 0;
        opposed[i][j] = 0;
      }
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf(" %c%c%c", &c1, &c2, &c3);
      combine[(int) c1][(int) c2] = c3;
      combine[(int) c2][(int) c1] = c3;
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf(" %c%c", &c1, &c2);
      opposed[(int) c1][(int) c2] = true;
      opposed[(int) c2][(int) c1] = true;
    }
    scanf("%d %s", &n, s);
    int j = 0;
    for (int i = 0; i < n; i++) {
      t[j] = s[i];
      j++;
      char c = (j >= 2) ? combine[(int) t[j - 1]][(int) t[j - 2]] : 0;
      if (c) {
        t[j - 2] = c;
        j--;
      }
      else {
        for (int k = 0; k < j - 1; k++) {
          if (opposed[(int) t[k]][(int) t[j - 1]]) {
            j = 0;
            break;
          }
        }
      }
      /*t[j] = 0; printf("t='%s'\n", t);*/
    }
    printf("Case #%i: [", iCase);
    for (int i = 0; i < j; i++) {
      if (i > 0) printf(", ");
      printf("%c", t[i]);
    }
    printf("]\n");
  }
  return 0;
}
