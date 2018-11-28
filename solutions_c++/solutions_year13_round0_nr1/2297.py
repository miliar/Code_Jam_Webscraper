#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

char s[8][8];

int finish(void)
{
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
      if (s[i][j] == '.')
        return 0;
  return 1;
}

int won(char who)
{
  int c, t;

  for(int i = 0; i < 4; i++)
  {
    c = t = 0;
    for(int j = 0; j < 4; j++)
    {
      if (s[i][j] == who) c++;
      else if (s[i][j] == 'T') t++;
    }
    if (c == 4 || (c == 3 && t == 1)) return 1;

    c = t = 0;
    for(int j = 0; j < 4; j++)
    {
      if (s[j][i] == who) c++;
      else if (s[j][i] == 'T') t++;
    }
    if (c == 4 || (c == 3 && t == 1)) return 1;
  }

  c = t = 0;
  for(int i = 0; i < 4; i++)
  {
    if (s[i][i] == who) c++;
    else if (s[i][i] == 'T') t++;
  }
  if (c == 4 || (c == 3 && t == 1)) return 1;

  c = t = 0;
  for(int i = 0; i < 4; i++)
  {
    if (s[3-i][i] == who) c++;
    else if (s[3-i][i] == 'T') t++;
  }
  if (c == 4 || (c == 3 && t == 1)) return 1;

  return 0;
}

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    for(int i = 0; i < 4; i++)
      scanf("%s", s[i]);

    printf("Case #%d: ", caso);

    if (won('X')) printf("X won\n");
    else if (won('O')) printf("O won\n");
    else if (finish()) printf("Draw\n");
    else printf("Game has not completed\n");
  }
}
