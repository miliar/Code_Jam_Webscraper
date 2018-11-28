#include <cstdio>
#include <cstring>

using namespace std;

const int SIGMA = 26;
const int MAX_LINE = 110;

char map[SIGMA] = {
  'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e',
  'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'
};
char line[MAX_LINE];

char getMappedChar(char c) {
  if (c >= 'a' && c <= 'z') {
    for (int i = 0; i < SIGMA; ++i) {
      if (c == map[i]) {
        return i + 'a';
      }
    }
  } else {
    return ' ';
  }
}

int main() {
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);

  int tests;
  scanf("%d ", &tests);
  for (int t = 1; t <= tests; ++t) {
    fgets(line, MAX_LINE, stdin);
    int len = strlen(line);

    printf("Case #%d: ", t);
    for (int i = 0; i < len; ++i) {
      printf("%c", getMappedChar(line[i]));
    }
    printf("\n");
  }

  return 0;
}
