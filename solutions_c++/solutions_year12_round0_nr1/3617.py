#include <cstdio>

char input[] = 
  "ejp mysljylc kd kxveddknmc re jsicpdrysi"
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
  "de kr kd eoya kw aej tysr re ujdr lkgc jv";

char output[] = 
  "our language is impossible to understand"
  "there are twenty six factorial possibilities"
  "so it is okay if you want to just give up";

char to[256];

int main(void) {
  char str[104];
  int T;
  
  to[(int)'q'] = 'z';
  to[(int)'z'] = 'q';
  
  for ( int i = 0; input[i]; ++i )
    to[(int)input[i]] = output[i];
    
  scanf("%d", &T);
  for ( int t = 1; t <= T; ++t ) {
    scanf(" %[^\n]", str);
    for ( int i = 0; str[i]; ++i )
      str[i] = to[(int)str[i]];
    printf("Case #%d: %s\n", t, str);
  }
  return 0;
}
