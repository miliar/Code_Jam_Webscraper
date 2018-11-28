/* CodeJam solution tic-tac-toe in C++11 by domob.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>


/* Check whether some player has won along a given direction.  Throw that
   player's symbol if yes.  */

void
checkWon (char board[4][4], int x, int y, int dx, int dy)
{
  int xs = 0;
  int os = 0;

  for (int i = 0; i < 4; ++i)
    {
      switch (board[x][y])
        {
          case 'T':
            ++xs;
            ++os;
            break;
          case 'X':
            ++xs;
            break;
          case 'O':
            ++os;
            break;
          default:
            break;
        }

      x += dx;
      y += dy;
    }

  if (xs == 4)
    throw 'X';
  if (os == 4)
    throw 'O';
}


/* Solve a single case.  */

void
solve_case ()
{
  bool empty = false;

  char board[4][4];
  for (int i = 0; i < 4; ++i)
    {
      char line[5];
      scanf ("%s\n", line);
      for (int j = 0; j < 4; ++j)
        {
          board[i][j] = line[j];
          if (line[j] == '.')
            empty = true;
        }
    }

  try
    {
      for (int i = 0; i < 4; ++i)
        {
          checkWon (board, 0, i, 1, 0);
          checkWon (board, i, 0, 0, 1);
        }
      checkWon (board, 0, 0, 1, 1);
      checkWon (board, 0, 3, 1, -1);
    }
  catch (char res)
    {
      printf ("%c won", res);
      return;
    }

  if (empty)
    printf ("Game has not completed");
  else
    printf ("Draw");
}


/* Main routine, handling the different cases.  */

int
main ()
{
  int n;

  scanf ("%d\n", &n);
  for (int i = 1; i <= n; ++i)
    {
      printf ("Case #%d: ", i);
      solve_case ();
      printf ("\n");
    }

  return EXIT_SUCCESS;
}
