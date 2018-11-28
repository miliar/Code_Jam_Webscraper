#include <cstdio>
#include <cstring>
#include <string.h>
using namespace std;

const int MAXLEN = 500;
const char pat[] = "welcome to code jam";
char str[MAXLEN + 1];
const int PATLEN = 19; //strlen("welcome to code jam");
int ways[MAXLEN + 1][PATLEN + 1];

int n;
int l;

int main () {
  scanf("%d\n", &n);
  ways[0][0] = 1;
  for (int j = 1; j <= PATLEN; ++j)
    ways[0][j] = 0;
  for (int i = 0; i < n; ++i) {
    gets(str);
    l = strlen(str);
    for (int k = 1; k <= l; ++k) {
      ways[k][0] = 1;
      for (int j = 1; j <= PATLEN; ++j) {
	ways[k][j] = ways[k - 1][j];
	ways[k][j] += (str[k - 1] == pat[j - 1])?ways[k - 1][j - 1]:0;
	ways[k][j] -= (ways[k][j] > 1000)?1000:0;
      }
    }

    printf("Case #%d: %04d\n", i + 1, ways[l][PATLEN]);
  }
}
