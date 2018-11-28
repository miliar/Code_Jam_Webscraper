/*
Rotate
*/

#include <iostream>
#include <fstream>

   using namespace std;

   char board[100][100];
   char temp[100][100];
   int dpvert[100][100];
   int dphoriz[100][100];
   int dpdiag1[100][100]; // lower left to upper right
   int dpdiag2[100][100]; // lower right to upper left

    int main()
   {
      ifstream in ("rotate.in");
      ofstream out ("rotate.out");
   
      int T;
      in >> T;
      for(int i = 0; i < T; i++)
      {
         int N, K;
         in >> N >> K;
         for(int j = 0; j < N; j++)
            in >> temp[j];
         for(int r = 0; r < N; r++)
            for(int c = 0; c < N; c++)
               board[c][N - r - 1] = temp[r][c];
         // shift down
         for(int r = N - 2; r >= 0; r--)
         {
            for(int c = 0; c < N; c++)
               if(board[r][c] != '.')
               {
                  int tempr = r;
                  while(tempr < N - 1 && board[tempr + 1][c] == '.')
                     tempr++;
                  if(tempr != r)
                  {
                     board[tempr][c] = board[r][c];
                     board[r][c] = '.';
                  }
               }
         }
         // dp is actually easier to code than brute force, so hopefully it works
         for(int r = 0; r < N; r++)
            for(int c = 0; c < N; c++)
            {
               dpvert[r][c] = 0;
               dphoriz[r][c] = 0;
               dpdiag1[r][c] = 0;
               dpdiag2[r][c] = 0;
            }
         bool bwin = false;
         bool rwin = false;
         for(int r = N - 1; r >= 0; r--)
            for(int c = 0; c < N; c++)
               if(board[r][c] != '.')
               {
                  if(c > 0 && board[r][c] == board[r][c - 1])
                     dphoriz[r][c] = 1 + dphoriz[r][c - 1];
                  else
                     dphoriz[r][c] = 1;
                  if(r < N - 1 && board[r][c] == board[r + 1][c])
                     dpvert[r][c] = 1 + dpvert[r + 1][c];
                  else
                     dpvert[r][c] = 1;
                  if(c > 0 && r < N - 1 && board[r][c] == board[r + 1][c - 1])
                     dpdiag1[r][c] = 1 + dpdiag1[r + 1][c - 1];
                  else
                     dpdiag1[r][c] = 1;
                  if(c < N - 1 && r < N - 1 && board[r][c] == board[r + 1][c + 1])
                     dpdiag2[r][c] = 1 + dpdiag2[r + 1][c + 1];
                  else
                     dpdiag2[r][c] = 1;
               	
                  if(dpvert[r][c] >= K || dphoriz[r][c] >= K || dpdiag1[r][c] >= K || dpdiag2[r][c] >= K)
                  {
                     if(board[r][c] == 'R')
                        rwin = true;
                     else if(board[r][c] == 'B')
                        bwin = true;
                  }
               }
         // 
         // for(int r = 0; r < N; r++)
         // {
            // for(int c = 0; c < N; c++)
               // cout << board[r][c] << "(" << dpvert[r][c] << ") ";
            // cout << endl;
         // }
               
         out << "Case #" << (i + 1) << ": ";
         if(bwin && rwin)
            out << "Both" << endl;
         else if(!bwin && !rwin)
            out << "Neither" << endl;
         else if(bwin)
            out << "Blue" << endl;
         else
            out << "Red" << endl;
      }
   
      return 0;
   }
   
