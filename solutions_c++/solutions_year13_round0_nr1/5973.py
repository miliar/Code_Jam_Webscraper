
#include <iostream>
#include <sstream>
#include <numeric>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;

#include <iostream>
#include <fstream>
using namespace std;

bool checkWinning(char x, vector<string> board)
{
	bool check = false;
	//rows
	for(int i = 0 ;i< 4; i++)
	{
		check = true;
		for(int j = 0; j < 4; j++)
		{
			if(board[i][j]!=x && board[i][j] != 'T')
			{
				check = false;
				break;
			}
		}
		if(check)
			return true;
	}
	//cols
	for(int i = 0 ; i < 4; i++)
	{
		check = true;
		for(int j = 0; j < 4; j++)
		{
			if(board[j][i]!=x && board[j][i] != 'T')
			{
				check = false;
				break;
			}
		}
		if(check)
			return true;
	}
	//diagonals
	check = true;
	for(int i = 0 ; i < 4; i++)
	{
		if(board[i][i]!=x && board[i][i]!='T')
		{
			check = false;
			break;
		}
	}
	if(check)
		return true;
	check = true;
	for(int i = 0,j=3; i < 4; j--,i++)
	{
		if(board[i][j]!=x && board[i][j]!='T')
		{
			check = false;
			break;
		}
	}
	if(check)
		return true;
	return false;
}
int main () 
{
  fstream fin;
  fstream fout;
  fin.open("A-large.in",ios::in);
  fout.open("A-large.out",ios::out);
  int T;
  fin>>T;
  vector<string> board;
  string temp;
  bool notCompleted;
  for(int i = 0; i < T; i++)
  {
	  notCompleted = false;
	  for(int j =0 ; j < 4; j++)
	  {
		  fin>>temp;
		  board.push_back(temp);
		  if(!notCompleted)
		  {
			 size_t pos = temp.find(".");
			if(pos!= string::npos)
			{
				notCompleted = true;
			}
		  }
	  }
	  bool OWins = checkWinning('O',board);
	  bool XWins = checkWinning('X',board);
	  if(XWins)
		  temp = "X won";
	  else if(OWins)
		  temp = "O won";
	  else if(!OWins && !XWins && notCompleted)
		  temp = "Game has not completed";
	  else
		  temp = "Draw";

	  fout<<"Case #"<<i+1<<": "<<temp<<endl;
	  board.clear();
  }
  fout.close();
  fin.close();
  return 0;
}