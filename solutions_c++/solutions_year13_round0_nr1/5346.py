// CodeJam2013PracticeA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#define cout outfile
int isNotDone(char board[][5])
{
	for (int i = 0;i<sizeof (board);i++)
		if( board[0][i] == '.') return 1;
	return 0;
}
int isWinner(char board[4][5],char search)
{
	for (int i = 0;i<4;i++)
	{
		if( (board[0][i] == search ||board[0][i] == 'T' )&&
			(board[1][i] == search ||board[1][i] == 'T' )&&
			(board[2][i] == search ||board[2][i] == 'T' )&&
			(board[3][i] == search ||board[3][i] == 'T' )
			) return 1;
		if( (board[i][0] == search ||board[i][0] == 'T' )&&
			(board[i][1] == search ||board[i][1] == 'T' )&&
			(board[i][2] == search ||board[i][2] == 'T' )&&
			(board[i][3] == search ||board[i][3] == 'T' )
			) return 1;

	}
			if( (board[0][0] == search ||board[0][0] == 'T' )&&
			(board[1][1] == search ||board[1][1] == 'T' )&&
			(board[2][2] == search ||board[2][2] == 'T' )&&
			(board[3][3] == search ||board[3][3] == 'T' )
			) return 1;
		if( (board[3][0] == search ||board[3][0] == 'T' )&&
			(board[2][1] == search ||board[2][1] == 'T' )&&
			(board[1][2] == search ||board[1][2] == 'T' )&&
			(board[0][3] == search ||board[0][3] == 'T' )
			) return 1;
		return 0;
}
int _tmain(int argc, _TCHAR* argv[])
{

	ifstream infile("A-small-practice.in");
	ofstream outfile("A-small-practice.out");
    string line;
	long numberOfCases = 0;
	
    if(infile)
    {
		infile>>numberOfCases;
     //   while(getline(inFile,line))
		for (int i = 1;i<=numberOfCases;i++)
		{
			char board[4][5] ={0};
			for (int j = 0;j<4;j++)
            infile>>board[j];
			if (isWinner(board,'X'))
			{cout<<"Case #"<<i<<": X won"<<endl;}
			else if (isWinner(board,'O'))
			{cout<<"Case #"<<i<<": O won"<<endl;}		
			else if (isNotDone(board))
			{cout<<"Case #"<<i<<": Game has not completed"<<endl;}		
			else
			{cout<<"Case #"<<i<<": Draw"<<endl;}		


        }

    infile.close();
    }
	else
	{
		cout<<"ERROR: Couldn't open File"<<endl;
	}
	//cout<<"endoffile"<<endl;


	return 0;
}

