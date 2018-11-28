/*
 * Problem A. Speaking in Tongues
 */

#include <cstdio>
#include <cstring>

#define INPUT_FILE    "A-small-attempt0.in"
#define OUTPUT_FILE   "A-small-attempt0.out"

int T;
char Map[256];


int main()
{
  freopen(INPUT_FILE, "rt", stdin);
  freopen(OUTPUT_FILE, "wt", stdout);

  Map['a'] = 'y';
  Map['b'] = 'h';
  Map['c'] = 'e';
  Map['d'] = 's';
  Map['e'] = 'o';
  Map['f'] = 'c';
  Map['g'] = 'v';
  Map['h'] = 'x';
  Map['i'] = 'd';
  Map['j'] = 'u';
  Map['k'] = 'i';
  Map['l'] = 'g';
  Map['m'] = 'l';
  Map['n'] = 'b';
  Map['o'] = 'k';
  Map['p'] = 'r';
  Map['q'] = 'z';
  Map['r'] = 't';
  Map['s'] = 'n';
  Map['t'] = 'w';
  Map['u'] = 'j';
  Map['v'] = 'p';
  Map['w'] = 'f';
  Map['x'] = 'm';
  Map['y'] = 'a';
  Map['z'] = 'q';


  scanf("%d\n", &T);

  for (int i = 1; i <= T; ++i)
  {
    printf("Case #%d: ", i);

    char sz[1000];
    gets(sz);

    int size = strlen(sz);

    for (int j = 0; j < size; ++j)
      if (sz[j] != ' ')
      {
        sz[j] = Map[sz[j]];
      };

    printf("%s\n", sz);
  }

  return 0;
}