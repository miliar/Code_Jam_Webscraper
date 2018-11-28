
#include <iostream>

using namespace std;

#include <iomanip>

#include "TicTacToe.h" //include my personal Class


bool TicTacToe::set_pos(int row ,int col,int user) //set position for specific user
{
	if (pos[row][col]==0){
	  pos[row][col]=user;
	  return true;}
  else
	  return false;
}

TicTacToe::TicTacToe() //initialize the value for all position equal to 0
{
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			pos[i][j]=0;
}

inline bool compare_user(int a, int b)
{
  return (a == b) || (a == 3);
}

bool TicTacToe::ifWin(int user) //check if anyone has won...
{
	for (int j=0;j<4;j++){
		if (compare_user(pos[0][j],user)&&compare_user(pos[1][j],user)&&compare_user(pos[2][j],user)&&compare_user(pos[3][j],user))
			return true;}
	for (int i=0;i<4;i++){
		if (compare_user(pos[i][0],user)&&compare_user(pos[i][1],user)&&compare_user(pos[i][2],user)&&compare_user(pos[i][3],user))
			return true;}
	if (compare_user(pos[0][0],user)&&compare_user(pos[1][1],user)&&compare_user(pos[2][2],user)&&compare_user(pos[3][3],user))
		return true;
	if (compare_user(pos[0][3],user)&&compare_user(pos[1][2],user)&&compare_user(pos[2][1],user)&&compare_user(pos[3][0],user))
		return true;
	return false;
}

void TicTacToe::show() //output the game result...
{
	for (int i=0;i<3;i++){
		for (int j=0;j<3;j++)
			cout<<setw(j+3)<<pos[i][j];
	    cout<<"\n";}
}
