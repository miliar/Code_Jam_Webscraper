#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <iomanip>

using namespace std;

bool isWin(const vector<vector<char>>& m, char color)
{
   for (int i = 0; i < m.size(); ++i)
   {
      int row = 0;
      int column = 0;

      for (int j = 0; j < m.size(); ++j)
      {
         if (m[i][j] == color || m[i][j] == 'T')
         {
            ++row;
         }
         if (m[j][i] == color || m[j][i] == 'T')
         {
            ++column;
         }
      }

      if (row == m.size() || column == m.size())
      {
         return true;
      }
   }

   int diagonal1 = 0;
   int diagonal2 = 0;
   for (int i = 0; i < m.size(); ++i)
   {
      if (m[i][i] == color || m[i][i] == 'T')
      {
         ++diagonal1;
      }
      if (m[i][m.size() - i - 1] == color || m[i][m.size() - i - 1] == 'T')
      {
         ++diagonal2;
      }
   }

   if (diagonal1 == m.size() || diagonal2 == m.size())
   {
      return true;
   }

   return false;
}

bool isDraw(const vector<vector<char>>& m)
{
   for (int i = 0; i < m.size(); ++i)
   {
      for (int j = 0; j < m.size(); ++j)
      {
         if (m[i][j] == '.')
         {
            return false;
         }
      }
   }

   return true;
}

void SolveA()
{
   ifstream fin("input.txt");
   ofstream fout("output.txt");

   int tests = 0;
   fin >> tests;

   for (int tc = 0; tc < tests; ++tc)
   {
      vector<vector<char>> board;
      for (int i = 0; i < 4; ++i)
      {
         board.push_back(vector<char>(4, 0));
         for (int j = 0; j < 4; ++j)
         {
            char ch;
            fin >> ch;
            board[i][j] = ch;
         }
      }

      fout << "Case #" << tc + 1 << ": ";
      if (isWin(board, 'X'))
      {
         fout << "X won";
      } 
      else if (isWin(board, 'O'))
      {
         fout << "O won";
      } 
      else if (isDraw(board))
      {
         fout << "Draw";
      } 
      else
      {
         fout << "Game has not completed";
      }
      fout << endl;
   }
}
