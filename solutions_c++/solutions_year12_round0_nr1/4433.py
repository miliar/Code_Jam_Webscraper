#include <cstdio>

using namespace std;

const char *c = "yhesocvxduiglbkrztnwjpfmaq";
char s[100];

int main() {
  int n; scanf("%d\n", &n);
  for (int tt = 1; tt <= n; ++tt) {
    gets(s);
    printf("Case #%d: ", tt);
    for (int i = 0; s[i] != 0; ++i) {
      if (s[i] != ' ') {
        putchar(c[s[i] - 'a']);
      } else putchar(' ');
    }
    putchar('\n');
  }
  return 0;
}

