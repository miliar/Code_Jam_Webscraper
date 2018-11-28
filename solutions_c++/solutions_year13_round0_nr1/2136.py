#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

char b[5][5];
char *res[] = {"X won", "O won", "Draw", "Game has not completed"};

int check (int sx, int sy, int dx, int dy)
{
  int i, x = sx, y = sy, T = 0, X = 0, O = 0;
  for (i = 0; i < 4; i++)
  {
    if (b[y][x] == '.')
      return -1;
    if (b[y][x] == 'X')
      X++;
    else if (b[y][x] == 'O')
      O++;
    else
      T++;
    x += dx;
    y += dy;  
  }
  if (X + T == 4)
    return 0;
  else if (O + T == 4)  
    return 1;
  else
    return -1;
}
              
int main (void)
{
  int test, tests;

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, nres = 2, t;
    for (i = 0; i < 4; i++)
      for (j = 0; j < 4; j++)
      {
        scanf (" %c", &b[i][j]);
        if (b[i][j] == '.')
          nres = 3;
      }
    for (i = 0; i < 4; i++)
    {
      t = check (0, i, 1, 0);
      if (t == 0 || t == 1)
        nres = t;
    }
    for (i = 0; i < 4; i++)
    {
      t = check (i, 0, 0, 1);
      if (t == 0 || t == 1)
        nres = t;
    }
    
    t = check (0, 0, 1, 1);
    if (t == 0 || t == 1)
      nres = t;

    t = check (0, 3, 1, -1);
    if (t == 0 || t == 1)
      nres = t;

    printf ("Case #%d: %s\n", test + 1, res[nres]);
    
  }
  return 0;
}
