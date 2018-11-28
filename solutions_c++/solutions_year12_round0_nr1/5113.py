#include <stdio.h>

char words[27][2] = {
  {' ', ' '},
  {'a', 'y'},
  {'b', 'h'},
  {'c', 'e'},
  {'d', 's'},
  {'e', 'o'},
  {'f', 'c'},
  {'g', 'v'},
  {'h', 'x'},
  {'i', 'd'},
  {'j', 'u'},
  {'k', 'i'},
  {'l', 'g'},
  {'m', 'l'},
  {'n', 'b'},
  {'o', 'k'},
  {'p', 'r'},
  {'q', 'z'},
  {'r', 't'},
  {'s', 'n'},
  {'t', 'w'},
  {'u', 'j'},
  {'v', 'p'},
  {'w', 'f'},
  {'x', 'm'},
  {'y', 'a'},
  {'z', 'q'}
};

char translate(char ch) {
  for (int i = 0; i < 27; i++) {
    if (words[i][0] == ch) {
      return words[i][1];
    }
  }
  return '\n';
}

int main(int argc, char *argv[]) {
  int T;
  char buf[200];
  scanf("%d\n", &T);

  for (int i = 1; i <= T; i++) {
    gets(buf);
    
    for (int j = 0; buf[j] != '\0'; j++) {
      buf[j] = translate(buf[j]);
    }

    printf("Case #%d: %s\n", i, buf);
  }

  return 0;
}
