#include <stdio.h>

/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

Output
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
*/

int main() {
  // read
  int T;
  scanf("%d", &T);
  // loop
  char G[200];
  int i, j;
  gets(G); // scang
  for (i = 1; i <= T; ++i) {
    printf("Case #%d: ", i);

    for (j = 0; j != 200; ++j) {
      G[j] = 0;
    }
    gets(G);

    for (j = 0; j != 200; ++j) {
      if (G[j]==0 ) {
        printf("\n");
        break;
      }
      switch (G[j]) {
        case ' ': printf(" "); break;
        case 'a': printf("y"); break;
        case 'b': printf("h"); break;
        case 'c': printf("e"); break;
        case 'd': printf("s"); break;
        case 'e': printf("o"); break;
        case 'f': printf("c"); break;
        case 'g': printf("v"); break;
        case 'h': printf("x"); break;
        case 'i': printf("d"); break;
        case 'j': printf("u"); break;
        case 'k': printf("i"); break;
        case 'l': printf("g"); break;
        case 'm': printf("l"); break;
        case 'n': printf("b"); break;
        case 'o': printf("k"); break;
        case 'p': printf("r"); break;
        case 'q': printf("z"); break;
        case 'r': printf("t"); break;
        case 's': printf("n"); break;
        case 't': printf("w"); break;
        case 'u': printf("j"); break;
        case 'v': printf("p"); break;
        case 'w': printf("f"); break;
        case 'x': printf("m"); break;
        case 'y': printf("a"); break;
        case 'z': printf("q"); break;
      }
    }
  }
  return 0;
}
