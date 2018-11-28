#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

char from[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
de kr kd eoya kw aej tysr re ujdr lkgc jv";

char to[] = "our language is impossible to understand\
there are twenty six factorial possibilities\
so it is okay if you want to just give up";

char map[256];

char s[128];

int main() {
  for (int i = 0; i < strlen(from); i++) {
    map[from[i]] = to[i];
  }
  map['z'] = 'q';
  map['q'] = 'z';

  int t;
  scanf("%d\n", &t);
  for (int tt = 1; tt <= t; tt++) {
    printf("Case #%d: ", tt);
    gets(s);
    for (int i = 0; i < strlen(s); i++) {
      printf("%c", map[s[i]]);
    }
    printf("\n");
  }
  
  return 0;
}
