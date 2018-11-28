#include <stdio.h>

              // "abcdefghijklmnopqrstuvwxyz"
const char *tr = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
  int T;
  scanf("%d", &T); getchar();
  for (int Tn = 1; Tn <= T; Tn++) {
    printf("Case #%d: ", Tn);
    while(1) {
      int c = getchar();
      if (c < ' ') break;
      if (c >= 'a' && c <= 'z') c = tr[c-'a'];
      putchar(c);
    }
    printf("\n");
  }
  return 0;
}
