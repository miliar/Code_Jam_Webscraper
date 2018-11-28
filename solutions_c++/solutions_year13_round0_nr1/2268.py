/*
 * Gary Ferrao
 * https://plus.google.com/u/0/110619450313015458698
 * 07:52:01 13 April 2013 IST
 * Tic-Tac-Toe-Tomek

Problem
Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts
empty, except that a single 'T' symbol may appear in one of the 16 squares.
There are two players: X and O. They take turns to make moves, with X starting.
In each move a player puts her symbol in one of the empty squares. Player X's
symbol is 'X', and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal containing 4 of
that player's symbols, or containing 3 of her symbols and the 'T' symbol, she
wins and the game ends. Otherwise the game continues with the other player's
move. If all of the fields are filled with symbols and nobody won, the game ends
in a draw. See the sample input for examples of various winning positions.

Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters
(where '.' represents an empty square), describing the current state of a game,
determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to
choose from are:

"X won" (the game is over, and X won)
"O won" (the game is over, and O won)
"Draw" (the game is over, and it ended in a draw)
"Game has not completed" (the game is not over yet)
If there are empty cells, and the game is not over, you should output "Game has
not completed", even if the outcome of the game is inevitable.

Input
The first line of the input gives the number of test cases, T. T test cases
follow. Each test case consists of 4 lines with 4 characters each, with each
character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case
is followed by an empty line.

Output
For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1) and y is one of the statuses given above. Make
sure to get the statuses exactly right. When you run your code on the sample
input, it should create the sample output exactly, including the "Case #1: ",
the capital letter "O" rather than the number "0", and so on.

Limits
The game board provided will represent a valid state that was reached through
play of the game Tic-Tac-Toe-Tomek as described above.

Small dataset
1 ≤ T ≤ 10.

Large dataset
1 ≤ T ≤ 1000.

 */
#include <iostream>
#include <fstream>
#include <string>
#define MAX 4
using namespace std;

char checkLine(char [MAX]);
char checkQuarts(char, char, char, char);
char check_vertically(char [MAX], char [MAX], char [MAX], char [MAX]);
char check_diagonals(char [MAX], char [MAX], char [MAX], char [MAX]);
char check_empty_space(char [MAX], char [MAX], char [MAX], char [MAX]);
int main ()
{
  ifstream ipfile;
  ofstream opfile;
  ipfile.open("A-large.in");
  opfile.open("A-large.op");
  if(! ipfile.is_open())
  {
  	cout << "Input file not found. Exiting..." << endl;
  	ipfile.close();
  	opfile.close();
  	return -1;
  }
  int n;
  char line1[MAX], line2[MAX], line3[MAX], line4[MAX];
  ipfile >> n;
  cout << "Beginning checking..." << endl;
  for(int i=1; i<=n; i++)
  {
  	ipfile >> line1;
  	ipfile >> line2;
  	ipfile >> line3;
  	ipfile >> line4;
  	char player;
  	int status_index=0;
  	string status[3]={"Draw","Game has not completed"," won"};
  	//check horizontally
  	if( ('T'!=(player=checkLine(line1))) || ('T'!=(player=checkLine(line2)))
  	  ||('T'!=(player=checkLine(line3)))||('T'!=(player=checkLine(line4))) )
	{
		status_index=2;
		goto printstatus;
	}
	//check vertically
	else if('T'!=(player=check_vertically(line1, line2, line3, line4)))
	{
		status_index = 2;
		goto printstatus;
	}
	//check diagonals
	else if('T'!=(player=check_diagonals(line1, line2, line3, line4)))
	{
		status_index = 2;
		goto printstatus;
	}
	//check for incomplete game
	else if('.'==(player=check_empty_space(line1,line2,line3,line4)))
	{
		status_index = 1;
	}
	opfile << "Case #" << i <<": " << status[status_index] << endl;
	printstatus:
	if(2==status_index)
		opfile << "Case #" << i <<": " << player << status[status_index]
		     << endl;
  }
  cout << "Completed checking." << endl;
  ipfile.close();
  opfile.close();
  return 0;
}

char checkLine(char line[MAX])
{
	char player=checkQuarts(line[0],line[1],line[2],line[3]);
	return player;
}
char checkQuarts(char a, char b, char c, char d)
{
	if('.'==a || '.'==b || '.'==c || '.'==d)
		return 'T';
	if(a==b && b==c && c==d)
		return a;
	else if('T'==a && b==c && c==d)
		return b;
	else if('T'==b && a==c && c==d)
		return a;
	else if('T'==c && a==b && b==d)
		return d;
	else if('T'==d && a==b && b==c)
		return c;
	else
		return 'T';
}
char check_vertically(char l1[MAX], char l2[MAX], char l3[MAX],char l4[MAX])
{
	char player;
	if(
	   ('T'!=(player=checkQuarts(l1[0],l2[0],l3[0],l4[0]))) ||
	   ('T'!=(player=checkQuarts(l1[1],l2[1],l3[1],l4[1]))) ||
	   ('T'!=(player=checkQuarts(l1[2],l2[2],l3[2],l4[2]))) ||
	   ('T'!=(player=checkQuarts(l1[3],l2[3],l3[3],l4[3])))	)
		return player;
	else
		return 'T';
}
char check_diagonals(char l1[MAX], char l2[MAX], char l3[MAX],char l4[MAX])
{
	char player;
	if('T'!=(player=checkQuarts(l1[0],l2[1],l3[2],l4[3])) ||
	   'T'!=(player=checkQuarts(l1[3],l2[2],l3[1],l4[0])))
		return player;
	else
		return 'T';
}
char check_empty_space(char l1[MAX], char l2[MAX], char l3[MAX], char l4[MAX])
{
	for(int i=0; i<MAX; i++)
		if('.'==l1[i])
			return '.';
	for(int i=0; i<MAX; i++)
		if('.'==l2[i])
			return '.';
	for(int i=0; i<MAX; i++)
		if('.'==l3[i])
			return '.';
	for(int i=0; i<MAX; i++)
		if('.'==l4[i])
			return '.';
}
