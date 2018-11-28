#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 64
char s[MAX][MAX];
int R,C;

int doit(void)
{
  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      if (s[i][j] == '#')
      {
        if (j+1 >= C || s[i][j+1] != '#') return(0);
        if (i+1 >= R || s[i+1][j] != '#') return(0);
        if (s[i+1][j+1] != '#') return(0);
        s[i][j] = '/';
        s[i][j+1] = '\\';
        s[i+1][j] = '\\';
        s[i+1][j+1] = '/';
        return(1);
      }

  return(0);
}

int main(void)
{
  int caso, T;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    scanf("%d %d", &R, &C);
    for(int i = 0; i < R; i++)
      scanf("%s", s[i]);

    while(doit());

    bool ok = true;
    for(int i = 0; i < R && ok; i++)
      for(int j = 0; j < C && ok; j++)
        if (s[i][j] == '#')
          ok = false;

    printf("Case #%d:\n", caso);
    if (!ok) printf("Impossible\n");
    else
      for(int i = 0; i < R; i++)
        printf("%s\n", s[i]);
  }

  return(0);
}

