/*
 * Problem-A-Tic-Tac-Toe-Tomek.cpp
 *
 *  Created on: 13.04.2013
 *      Author: XStalkerX
 */

#include <fstream>
#include <iostream>

int main (int argc, char* argv[])
{
  if (argc != 2)
  {
    std::cout << "No file" << std::endl;
    return 0;
  }

  std::ifstream input (argv[1], std::fstream::in);
  if (!input.is_open())
  {
    std::cout << "Can't read" << std::endl;
    return -1;
  }

  std::ofstream output ("TicTacToe.out", std::fstream::out);
  if (!output.is_open())
  {
    std::cout << "Can't write" << std::endl;
    return -1;
  }

  /* scroll example:
      6
      XXXT
      ....
      OO..
      ....

      XOXT
      XXOO
      OXOX
      XXOO
  */
    int games_number = 0;

    input >> games_number;
    char board[4][4];
    bool finished = true;

    for (int i = 1; i <= games_number; ++i)
    {
      finished = true;
      input >> board[0][0] >> board[0][1] >> board[0][2] >> board[0][3];
      input >> board[1][0] >> board[1][1] >> board[1][2] >> board[1][3];
      input >> board[2][0] >> board[2][1] >> board[2][2] >> board[2][3];
      input >> board[3][0] >> board[3][1] >> board[3][2] >> board[3][3];

//
//      std::cout << std::endl;
//      std::cout << board[0][0] << board[0][1] << board[0][2] << board[0][3] << std::endl;
//      std::cout << board[1][0] << board[1][1] << board[1][2] << board[1][3] << std::endl;
//      std::cout << board[2][0] << board[2][1] << board[2][2] << board[2][3] << std::endl;
//      std::cout << board[3][0] << board[3][1] << board[3][2] << board[3][3] << std::endl;

      bool row_O[4] = { true, true, true, true };
      bool col_O[4] = { true, true, true, true };

      bool row_X[4] = { true, true, true, true };
      bool col_X[4] = { true, true, true, true };

      bool dgn_X[2] = { true, true };
      bool dgn_O[2] = { true, true };

      for (int x = 0; x < 4; ++x)
      {
        for (int y = 0; y < 4; ++y)
        {
          if (board[x][y] == 'X')
          {
            col_O[x] = false;
            row_O[y] = false;
          }
          else if (board[x][y] == 'O')
          {
            col_X[x] = false;
            row_X[y] = false;
          }
          else if (board[x][y] == '.')
          {
            col_O[x] = false;
            row_O[y] = false;

            col_X[x] = false;
            row_X[y] = false;

            finished = false;
          }
        }
      }

      for (int n = 0; n < 4; ++n)
      {
        if (board[n][n] == 'X' or board[n][n] == '.')
          dgn_O[0] = false;
        if (board[3 - n][n] == 'X' or board[3 - n][n] == '.')
          dgn_O[1] = false;

        if (board[n][n] == 'O' or board[n][n] == '.')
          dgn_X[0] = false;
        if (board[3 - n][n] == 'O' or board[3 - n][n] == '.')
          dgn_X[1] = false;
      }

//      std::cout << "O: ";
//      for (int n = 0; n < 4; ++n)
//      {
//        std::cout << row_O[n] << col_O[n] << ", ";
//      }
//      std::cout << std::endl;
//      std::cout << dgn_O[0] << dgn_O[1];
//      std::cout << std::endl;


      if (i != 1)
        output << std::endl;
      output << "Case #" << i << ": ";
      if (row_O[0] or row_O[1] or row_O[2] or row_O[3] or
          col_O[0] or col_O[1] or col_O[2] or col_O[3] or
          dgn_O[0] or dgn_O[1])
        output << "O won";
      else if (row_X[0] or row_X[1] or row_X[2] or row_X[3] or
               col_X[0] or col_X[1] or col_X[2] or col_X[3] or
               dgn_X[0] or dgn_X[1])
        output << "X won";
      else if (finished)
        output << "Draw";
      else
        output << "Game has not completed";


    }
    input.close();
    output.close();
}



