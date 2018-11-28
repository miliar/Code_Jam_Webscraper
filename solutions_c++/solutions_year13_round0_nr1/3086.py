#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>
#include <queue>
#include <stdio.h>
#include <math.h>

//////////////////////////////////////////////////
// std::map<std::string, std::vector<int>> map; //
// std::vector<int> v;                          //
// v.push_back(1);                              //
// v.push_back(2);                              //
// v.push_back(3);                              //
// map["one"] = v;                              //
//                                              //
// for(const auto& kvp : map)                   //
//   {                                          //
//     std::cout << kvp.first << std::endl;     //
//                                              //
//     for(auto v : kvp.second)                 //
//       {                                      //
//         std::cout << v << std::endl;         //
//       }                                      //
//   }                                          //
//////////////////////////////////////////////////

using namespace std;

int checkRow(const char * const board, int row)
{
  int idx = row * 4;
  int x_count = 0;
  int o_count = 0;
  int empty_count = 0;
  
  for (int i = 0; i < 4; ++i)
    {
      if (board[idx] == 'X')
        {
          x_count++;
        }        
      if (board[idx] == 'O')
        {
          o_count++;
        }
      if (board[idx] == 'T')
        {
          x_count++;
          o_count++;
        }
      if (board[idx] == '.')
        {
          empty_count++;
        }
      idx++;
    }

  if(x_count > 3)
    return 1;
  
  if(o_count > 3)
    return 2;

  if(empty_count > 0)
    return -1;
}


int checkCol(const char * const board, int col)
{
  int idx = col;
  int x_count = 0;
  int o_count = 0;
  int empty_count = 0;
  
  for (int i = 0; i < 4; ++i)
    {
      if (board[idx] == 'X')
        {
          x_count++;
        }        
      if (board[idx] == 'O')
        {
          o_count++;
        }
      if (board[idx] == 'T')
        {
          x_count++;
          o_count++;
        }
      if (board[idx] == '.')
        {
          empty_count++;
        }
      idx+=4;
    }

  if(x_count > 3)
    return 1;
  
  if(o_count > 3)
    return 2;

  if(empty_count > 0)
    return -1;
}

int checkDiag(const char * const board, int diag_type)
{
  int idx;
  int x_count = 0;
  int o_count = 0;
  int empty_count = 0;

  if (diag_type == 0)
    {
      idx = 0;
    }
  else
    {
      idx = 12;
    }
  
  for (int i = 0; i < 4; ++i)
    {
      if (board[idx] == 'X')
        {
          x_count++;
        }        
      if (board[idx] == 'O')
        {
          o_count++;
        }
      if (board[idx] == 'T')
        {
          x_count++;
          o_count++;
        }
      if (board[idx] == '.')
        {
          empty_count++;
        }
      
      if (diag_type == 0)
        {
          idx += 5;
        }
      else
        {
          idx -= 3;
        }
    }

  if(x_count > 3)
    return 1;
  
  if(o_count > 3)
    return 2;

  if(empty_count > 0)
    return -1;
}

int main(int argc, char *argv[])
{

  int numCases;
  cin >> numCases;

  if(numCases)
    {
      cin.get(); // New line

      char board[16];
      int status;

      // Case Loop
      for (int _case = 0; _case < numCases; ++_case)
        {
          status = -1; // -1 Incomplete, 0 Draw, 1 X, 2 O
          // Read board
          for (int i = 0; i < 4; ++i)
            {
              for (int j = 0; j < 4; ++j)
                {
                  cin >> board[i*4 + j];
                  //cout << board[i*4 + j];
                }
              //cout << endl;
            }

          // Get board status
          int incomplete = 0;
          int winner = 0;
          int partial_status;
          
          // Check Rows
          for (int i = 0; i < 4; ++i)
            {
              partial_status = checkRow(board, i);
              if(partial_status == -1)
                incomplete++;
              if(partial_status > 0)
                winner |= partial_status;              
            }

          // Check Columns
          for (int i = 0; i < 4; ++i)
            {
              partial_status = checkCol(board, i);
              if(partial_status == -1)
                incomplete++;
              if(partial_status > 0)
                winner |= partial_status;              
            }

          // Check ULDR Diag
          partial_status = checkDiag(board, 0);
          if(partial_status == -1)
            incomplete++;
          if(partial_status > 0)
            winner |= partial_status;

          // Check DLUR Diag
          partial_status = checkDiag(board, 1);
          if(partial_status == -1)
            incomplete++;
          if(partial_status > 0)
            winner |= partial_status;
          
          //cout << "Winner " << winner << endl;
          if (winner)
            {
              if(winner % 2 == 1)
                {
                  cout << "Case #" << _case+1 << ": X won";
                }
              else
                {
                  cout << "Case #" << _case+1 << ": O won";
                }
            }
          else
            {
              if (incomplete)
                {
                  cout << "Case #" << _case+1 << ": Game has not completed";
                }
              else
                cout << "Case #" << _case+1 << ": Draw";
            }
          cout << endl;
        }
    }
  return 0;
}
