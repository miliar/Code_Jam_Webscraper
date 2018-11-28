#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int check (char game[4][4]);

int main()
{
  ofstream fout("tictac.out");
  ifstream fin("A-small-attempt1.in");
  char board[4][4];
  int cases, result;

  fin >> cases;
  
  for (int i = 1; i <= cases; i++)
    {
      for (int j = 0; j < 4; j++)
	for (int k = 0; k < 4; k++)
	  fin >> board[j][k];
      if (
	  (
	   (board[0][0] == 'X' || board[0][0] == 'T') 
	   && (board[0][1] == 'X' || board[0][1] == 'T') 
	   &&(board[0][2] == 'X' || board[0][2] == 'T') 
	   &&(board[0][3] == 'X' || board[0][3] == 'T')
	   )||
	  (
	   (board[1][0] == 'X' || board[1][0] == 'T') 
	   &&(board[1][1] == 'X' || board[1][1] == 'T') 
	   &&(board[1][2] == 'X' || board[1][2] == 'T') 
	   &&(board[1][3] == 'X' || board[1][3] == 'T')
	   )||
	  (
	   (board[2][0] == 'X' || board[2][0] == 'T') 
	   &&(board[2][1] == 'X' || board[2][1] == 'T') 
	   &&(board[2][2] == 'X' || board[2][2] == 'T') 
	   &&(board[2][3] == 'X' || board[2][3] == 'T')
	   )||
	  (
	   (board[3][0] == 'X' || board[3][0] == 'T') 
	   &&(board[3][1] == 'X' || board[3][1] == 'T') 
	   &&(board[3][2] == 'X' || board[3][2] == 'T') 
	   &&(board[3][3] == 'X' || board[3][3] == 'T')
	   )||
	  (
	   (board[0][0] == 'X' || board[0][0] == 'T') 
	   &&(board[1][0] == 'X' || board[1][0] == 'T') 
	   &&(board[2][0] == 'X' || board[2][0] == 'T') 
	   &&(board[3][0] == 'X' || board[3][0] == 'T')
	   )||
	  ( 
	   (board[0][1] == 'X' || board[0][1] == 'T') 
	   &&(board[1][1] == 'X' || board[1][1] == 'T') 
	   &&(board[2][1] == 'X' || board[2][1] == 'T') 
	   &&(board[3][1] == 'X' || board[3][1] == 'T') 
	    )||
	  (
	   (board[0][2] == 'X' || board[0][2] == 'T')
	   &&(board[1][2] == 'X' || board[1][2] == 'T')
	   &&(board[2][2] == 'X' || board[2][2] == 'T')
	   &&(board[3][2] == 'X' || board[3][2] == 'T')
	   )||
	  (
	   (board[0][3] == 'X' || board[0][3] == 'T')
	   &&(board[1][3] == 'X' || board[1][3] == 'T')
	   &&(board[2][3] == 'X' || board[2][3] == 'T')
	   &&(board[3][3] == 'X' || board[3][3] == 'T')
	   )||
	  (
	   (board[0][0] == 'X' || board[0][0] == 'T')
	   &&(board[1][1] == 'X' || board[1][1] == 'T')
	   &&(board[2][2] == 'X' || board[2][2] == 'T')
	   &&(board[3][3] == 'X' || board[3][3] == 'T')
	   )||
	  (
	   (board[0][3] == 'X' || board[0][3] == 'T')
	   &&(board[1][2] == 'X' || board[1][2] == 'T')
	   &&(board[2][1] == 'X' || board[2][1] == 'T')
	   &&(board[3][0] == 'X' || board[3][0] == 'T')
	   ))
	fout << "Case #" << i << ": X won" << endl;
      else if 
	(
	 (
	  (board[0][0] == 'O' || board[0][0] == 'T')
	  && (board[0][1] == 'O' || board[0][1] == 'T')
	  &&(board[0][2] == 'O' || board[0][2] == 'T')
	  &&(board[0][3] == 'O' || board[0][3] == 'T')
	  )||
	 (
	  (board[1][0] == 'O' || board[1][0] == 'T')
	  &&(board[1][1] == 'O' || board[1][1] == 'T')
	  &&(board[1][2] == 'O' || board[1][2] == 'T')
	  &&(board[1][3] == 'O' || board[1][3] == 'T')
	  )||
	 (
	  (board[2][0] == 'O' || board[2][0] == 'T')
	  &&(board[2][1] == 'O' || board[2][1] == 'T')
	  &&(board[2][2] == 'O' || board[2][2] == 'T')
	  &&(board[2][3] == 'O' || board[2][3] == 'T')
	  )||
	 (
	  (board[3][0] == 'O' || board[3][0] == 'T')
	  &&(board[3][1] == 'O' || board[3][1] == 'T')
	  &&(board[3][2] == 'O' || board[3][2] == 'T')
	  &&(board[3][3] == 'O' || board[3][3] == 'T')
	  )||
	 (
	  (board[0][0] == 'O' || board[0][0] == 'T')
	  &&(board[1][0] == 'O' || board[1][0] == 'T')
	  &&(board[2][0] == 'O' || board[2][0] == 'T')
	  &&(board[3][0] == 'O' || board[3][0] == 'T')
	  )||
	 (
	  (board[0][1] == 'O' || board[0][1] == 'T')
	  &&(board[1][1] == 'O' || board[1][1] == 'T')
	  &&(board[2][1] == 'O' || board[2][1] == 'T')
	  &&(board[3][1] == 'O' || board[3][1] == 'T')
	  )||
	 (
	  (board[0][2] == 'O' || board[0][2] == 'T')
	  &&(board[1][2] == 'O' || board[1][2] == 'T')
	  &&(board[2][2] == 'O' || board[2][2] == 'T')
	  &&(board[3][2] == 'O' || board[3][2] == 'T')
	  )||
	 (
	  (board[0][3] == 'O' || board[0][3] == 'T')
	  &&(board[1][3] == 'O' || board[1][3] == 'T')
	  &&(board[2][3] == 'O' || board[2][3] == 'T')
	  &&(board[3][3] == 'O' || board[3][3] == 'T')
	  )||
	 (
	  (board[0][0] == 'O' || board[0][0] == 'T')
	  &&(board[1][1] == 'O' || board[1][1] == 'T')
	  &&(board[2][2] == 'O' || board[2][2] == 'T')
	  &&(board[3][3] == 'O' || board[3][3] == 'T')
	  )||
	 (
	  (board[0][3] == 'O' || board[0][3] == 'T')
	  &&(board[1][2] == 'O' || board[1][2] == 'T')
	  &&(board[2][1] == 'O' || board[2][1] == 'T')
	  &&(board[3][0] == 'O' || board[3][0] == 'T')
	  ))
	fout << "Case #" << i << ": O won" << endl;
      else
	{
	  bool draw = true;
	  for (int j = 0; j < 4; j++)
	    for (int k = 0; k < 4; k++)
	      if (board[j][k] == '.')
		draw  = false;
	  if (draw)
	    fout << "Case #" << i << ": Draw" << endl;
	  else 
	    fout << "Case #" << i << ": Game has not completed" << endl;
	}
    }
}
