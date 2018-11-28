#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

int main() {
  map<char, char> c;
  c['a'] = 'y';
  c['b'] = 'h';
  c['c'] = 'e';
  c['d'] = 's';
  c['e'] = 'o';
  c['f'] = 'c';
  c['g'] = 'v';
  c['h'] = 'x';
  c['i'] = 'd';
  c['j'] = 'u';
  c['k'] = 'i';
  c['l'] = 'g';
  c['m'] = 'l';
  c['n'] = 'b';
  c['o'] = 'k';
  c['p'] = 'r';
  c['r'] = 't';
  c['s'] = 'n';
  c['t'] = 'w';
  c['u'] = 'j';
  c['w'] = 'f';
  c['q'] = 'z';
  c['x'] = 'm';
  c['y'] = 'a';
  c['z'] = 'q';
  c['v'] = 'p';
  c[' '] = ' ';
  int n;
  scanf("%d\n", &n);
  char str[1000];
  for (int i = 0; i < n; ++i) {
    gets(str);
    if (str[strlen(str) - 1] == '\n') {
      str[strlen(str) - 1] = '\0';
    }
    char *p = str;
    while (*p != '\0') {
      *p = c[*p];
      ++p;
    }
    printf("Case #%d: %s\n", i + 1, str);
  }
  return 0;
}
