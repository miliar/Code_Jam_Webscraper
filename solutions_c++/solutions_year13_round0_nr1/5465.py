// Problem A. Tic-Tac-Toe-Tomek
// By gvaf

#include <iostream>
#include <stdio.h>
using namespace std;

void readBoard(char board[4][4]);
void printStatus(int testID, char board[4][4]);

int main()
{
 int T;
 char board[4][4];

 cin >> T;

 for(int i = 0; i < T; ++i)
 {
   readBoard(board);
   printStatus(i + 1, board);
 }

 return 0;
}

void readBoard(char board[4][4])
{
 getchar();

  for(int r = 0; r < 4; ++r)
  {
     for(int c = 0; c < 4; ++c)
         board[r][c] = getchar();

     getchar();
  }
}

struct Counter
{
  Counter()
  {
    countX = countO = countT = 0;
  }

  void count(char cell)
  {
   if( cell == 'X' ) ++countX;  
   if( cell == 'O' ) ++countO;  
   if( cell == 'T' ) ++countT;         
  }
  
  bool foundWinner(int testID)
  {
    if( (countX + countT) == 4 )
    {
      cout << "Case #" << testID << ": X won" << endl; 
      return true;
    }

    if( (countO + countT) == 4 )
    {
      cout << "Case #" << testID << ": O won" << endl; 
      return true;
    }

    return false;
  }

  int countX;
  int countO;
  int countT;
};

void printStatus(int testID, char board[4][4])
{
  Counter d0;
  Counter d1;
  int     empty = 0;

  for(int r = 0; r < 4; ++r)
  {
    Counter h;
    Counter v;

    for(int c = 0; c < 4; ++c)
    {
      if( board[r][c] == '.' ) 
        {
          ++empty;
          continue;
        }

       h.count( board[r][c] );
       v.count( board[c][r] );

       if( r == c )       d0.count( board[r][c] );
       if( c == (3 - r) ) d1.count( board[r][c] );    
    }
 
   if( h.foundWinner(testID) )
      return;

   if( v.foundWinner(testID) )
      return;
  }

  if( d0.foundWinner(testID) )
      return;

  if( d1.foundWinner(testID) )
      return;

  if( empty == 0 )
    cout << "Case #" << testID << ": Draw" << endl; 
  else
    cout << "Case #" << testID << ": Game has not completed" << endl; 
}


