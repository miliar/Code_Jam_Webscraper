#include <stdio.h>
#include <string.h>

#define MAX 500

int main() {
  int n;
  char in[MAX];
  char out[MAX];
  char map[27] = "yhesocvxduiglbkrztnwjpfmaq";
  scanf("%d", &n);
  gets(in);
  for (int i = 1; i <=n; ++i) {
    gets(in);
    for (int j = 0;j < strlen(in); ++j) {
      if (in[j] >= 'a' && in[j] <= 'z') {
        out[j] = map[in[j]-'a'];
      } else {
        out[j] = in[j];
      }
    }
    out[strlen(in)] = '\0';
    printf("Case #%d: %s\n", i, out);
  }
}
