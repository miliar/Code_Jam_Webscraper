#include <cstdio>
#include <cstdlib>
#include <cstring>

char s[] = "yhesocvxduiglbkrztnwjpfmaq";
char buf[256];

int main () {
  gets (buf);
  int t = atol (buf);
  for (int i = 0; i < t; i++) {
    gets (buf);
    int l = strlen(buf);
    for (int j = 0; j < l; j++) if (buf[j] >= 'a') buf[j] = s[buf[j] - 'a'];
    printf ("Case #%d: %s\n", i + 1, buf);
  }
  return 0;
}
