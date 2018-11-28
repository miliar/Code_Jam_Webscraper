#include <iostream>
#include <cstdio>

char table[5][5];

#define debug(...) //printf(__VA_ARGS__)

bool lineWon(int line, char p)
{
  for(int i = 0; i < 4; i++)
  {
    if(table[line][i] != p && table[line][i] != 'T') return false;
  }
  debug("Line %d for %c\n", line, p);
  return true;
}

bool colWon(int col, char p)
{
  for(int i = 0; i < 4; i++)
  {
    if(table[i][col] != p && table[i][col] != 'T') return false;
  }

  debug("Col %d for %c\n", col, p);
  return true;
}

bool diag1Won(char p)
{
  for(int i = 0; i < 4; i++)
  {
    if(table[i][i] != p && table[i][i] != 'T') return false;
  }

  debug("Diag1 for %c\n", p);
  return true;
}

bool diag2Won(char p)
{
  for(int i = 0; i < 4; i++)
  {
    if(table[i][3-i] != p && table[i][3-i] != 'T') return false;
  }

  debug("Diag2 for %c\n", p);
  return true;
}

int main(void)
{
  int N;

  scanf("%d\n",&N);

  for(int cas = 1; cas <= N; cas++)
  {
    for(int i = 0; i < 4; i++)
    {
      scanf("%s\n",table[i]);
    }

    for(int i = 0; i < 4; i++)
    {
      for(int j = 0; j < 4; j++) debug("%c", table[i][j]);
      debug("\n");
    }
    
    bool x=false, o=false, finished = true;

    for(int i = 0; i < 4; i++)
    {
      x |= lineWon(i,'X') | colWon(i, 'X');
      o |= lineWon(i, 'O') | colWon(i, 'O');

      for(int j = 0; j < 4; j++) if(table[i][j] == '.') { debug("ponto em %d, %d\n", i, j); finished = false; }
    }

    x |= diag1Won('X') | diag2Won('X');
    o |= diag1Won('O') | diag2Won('O');

    printf("Case #%d: %s\n", cas, (!x && !o) ? (finished ? "Draw" : "Game has not completed") : x ? "X won" : "O won");
  }

  return 0;
}
