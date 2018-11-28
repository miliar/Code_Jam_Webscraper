#include <stdio.h>

char board[8][8];

enum whoWins
{
  NOONE,
  DRAW,
  OWINS,
  XWINS
};

bool doesWin(char t, int x, int y, int vx, int vy, int c)
{
  if(c == 4)
    return true;

  if(x+vx >= 4 || x+vx < 0)
    return false;
  if(y+vy >= 4 || y+vy < 0)
    return false;

  if(board[x+vx][y+vy] == t || board[x+vx][y+vy] == 'T')
    return doesWin(t, x+vx, y+vy, vx, vy, c+1);

  return false;
}

int main(void)
{
  int t;
  char line[128];
  fgets(line, sizeof(line), stdin);
  sscanf(line,"%d",&t);

  for(int i(0); i < t; ++i)
  {
    // get the board
    for(int j(0); j < 4; ++j)
    {
      fgets(board[j], sizeof(board[j]), stdin);
    }
    fgets(line, sizeof(line), stdin);

    whoWins w = DRAW;

    for(int j(0); j < 4; ++j)
    {
      for(int k(0); k < 4; ++k)
      {
        if(board[j][k] != '.' && board[j][k] != 'T')
        {
          bool win = false;
          win = doesWin(board[j][k], j, k, 1, 0, 1);
          if(win)
          {
            if(board[j][k] == 'O')
              w = OWINS;
            else
              w = XWINS;
          }
          else
          {
            win = doesWin(board[j][k], j, k, 0, 1, 1);
            if(win)
            {
              if(board[j][k] == 'O')
                w = OWINS;
              else
                w = XWINS;
            }
            else
            {
              win = doesWin(board[j][k], j, k, -1, 0, 1);
              if(win)
              {
                if(board[j][k] == 'O')
                  w = OWINS;
                else
                  w = XWINS;
              }
              else
              {
                win = doesWin(board[j][k], j, k, 0,-1, 1);
                if(win)
                {
                  if(board[j][k] == 'O')
                    w = OWINS;
                  else
                    w = XWINS;
                }
                else
                {
                  win = doesWin(board[j][k], j, k, 1, 1, 1);
                  if(win)
                  {
                    if(board[j][k] == 'O')
                      w = OWINS;
                    else
                      w = XWINS;
                  }
                  else
                  {
                    win = doesWin(board[j][k], j, k, -1, 1, 1);
                    if(win)
                    {
                      if(board[j][k] == 'O')
                        w = OWINS;
                      else
                        w = XWINS;
                    }
                    else
                    {
                      win = doesWin(board[j][k], j, k, 1, -1, 1);
                      if(win)
                      {
                        if(board[j][k] == 'O')
                          w = OWINS;
                        else
                          w = XWINS;
                      }
                      else
                      {
                        win = doesWin(board[j][k], j, k, -1,-1, 1);
                        if(win)
                        {
                          if(board[j][k] == 'O')
                            w = OWINS;
                          else
                            w = XWINS;
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        if(board[j][k] == '.')
          w = NOONE;

        if(w == OWINS || w == XWINS)
          break;
      }
      if(w == OWINS || w == XWINS)
        break;
    }

    char result[64];
    if(w == DRAW)
      sprintf(result, "Draw");
    else if(w == NOONE)
      sprintf(result, "Game has not completed");
    else if(w == XWINS)
      sprintf(result, "X won");
    else if(w == OWINS)
      sprintf(result, "O won");
    printf("Case #%d: %s\n",i+1,result);
  }
}
