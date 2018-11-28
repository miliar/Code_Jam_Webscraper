#include <stdio.h>

char map[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
    int kase;
    char s[200];
    int count = 1;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    gets(s);
    while (kase--) {
          gets(s);
          printf("Case #%d: ",count++);
          for (int i = 0; s[i] != 0;++i) {
              if (s[i] == ' ') printf(" ");
              else printf("%c",map[s[i]-'a']);
          }
          printf("\n");
    }
    return 0;
}
