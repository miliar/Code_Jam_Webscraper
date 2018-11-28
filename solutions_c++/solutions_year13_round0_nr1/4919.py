#include <string>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

typedef vector<vector<bool> > BitMask;

bool CheckRow(const BitMask& aBitMask, int aRowNr)
{
	bool res = true;
	for(int i = 0; i < 4; ++i)
		res = (res && aBitMask[aRowNr][i]);
	return res;
}

bool CheckCol(const BitMask& aBitMask, int aColNr)
{
	bool res = true;
   for(int i = 0; i < 4; ++i)
      res = (res && aBitMask[i][aColNr]);
   return res;
}

bool CheckDiag(const BitMask& aBitMask, bool aFirstOrSecond)
{
	bool res = true;
	if(aFirstOrSecond)
	{
		for(int i = 0; i < 4; ++i)
			res = (res && aBitMask[i][i]);
	}
	else
	{
		for(int i = 0; i < 4; ++i)
         res = (res && aBitMask[3-i][i]);
	}
	return res;
}

bool CheckNotDone(const BitMask& aBitMask)
{
	bool res = false;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			res = (res || aBitMask[i][j]);
	return res;
}

void ReadNewGameBoard(fstream& aFile, BitMask& aPlayerO, BitMask& aPlayerX, BitMask& aEmptyBoard)
{
	string line;
	for(int i = 0; i < 4; ++i)
	{	
		getline(aFile, line);
		for(int j = 0; j < 4; ++j)
		{
			if(line.c_str()[j] == '.')
			{
				aPlayerO[i][j] 	= false;
				aPlayerX[i][j] 	= false;
				aEmptyBoard[i][j]	= true;
			}
			else if(line[j] == 'O')
			{
				aPlayerO[i][j]    = true;
            aPlayerX[i][j]    = false;
            aEmptyBoard[i][j] = false;
			}
			else if(line[j] == 'X')
			{
				aPlayerO[i][j]    = false;
            aPlayerX[i][j]    = true;
            aEmptyBoard[i][j] = false;
			}
			else // line[j] == "T"
			{
				aPlayerO[i][j]    = true;
            aPlayerX[i][j]    = true;
            aEmptyBoard[i][j] = false;
			}
		}
	}
}

void OutPutResult(bool Owon, bool Xwon, bool NotDone)
{
	if(Owon)
	{
		cout << "O won" << endl;
	}
	else if(Xwon)
	{
		cout << "X won" << endl;
	}
	else if(NotDone)
	{
		cout << "Game has not completed" << endl;
	}
	else
	{
		cout << "Draw" << endl;
	}
}

bool CheckPlayerWon(const BitMask& aPlayer)
{
	bool Playerwon = false;
   for(int j = 0; j < 4; ++j)
   {
      Playerwon = (Playerwon || CheckRow(aPlayer, j));
      Playerwon = (Playerwon || CheckCol(aPlayer, j));
   }
   Playerwon = (Playerwon || CheckDiag(aPlayer, true));
   Playerwon = (Playerwon || CheckDiag(aPlayer, false));
	return Playerwon;
}

void OutPutGameBoard(const BitMask& aBoard)
{
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
			cout << aBoard[i][j];
		cout << endl;
	}		
}

int main(){
	fstream input_file("input");
	int nr_of_boards;
	input_file >> nr_of_boards;
	string empty_line;
	BitMask PlayerO;
	BitMask PlayerX;
	BitMask EmptyBoard;
	vector<bool> PlaceHolder;
	for(int i = 0; i < 4; ++i)
		PlaceHolder.push_back(false);
	for(int i = 0; i < 4; ++i)
	{
		PlayerO.push_back(PlaceHolder);
		PlayerX.push_back(PlaceHolder);
		EmptyBoard.push_back(PlaceHolder);
	}
	for(int i = 1; i <= nr_of_boards; ++i)
	{
		getline(input_file, empty_line);
		ReadNewGameBoard(input_file,PlayerO,PlayerX,EmptyBoard);
		bool PlayerOwon = CheckPlayerWon(PlayerO);
		bool PlayerXwon = CheckPlayerWon(PlayerX);
		bool IsGameDone = CheckNotDone(EmptyBoard);
		/*cout << "Os board : " << endl;
		OutPutGameBoard(PlayerO);
		cout << "Xs board : " << endl;
		OutPutGameBoard(PlayerX);*/
		/*cout << "Empty Titles : " << endl;
		OutPutGameBoard(EmptyBoard);
		cout << "IsGameDone : " << IsGameDone << endl;*/
		cout << "Case #" << i << ": ";
		OutPutResult(PlayerOwon,PlayerXwon,IsGameDone);
		//getline(input_file, empty_line);
	}
	return 0;
}
