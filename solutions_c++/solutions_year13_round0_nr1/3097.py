#include <iostream>
#include <fstream>

using namespace std;

enum Result {XWON, OWON, DRAW, INCOMPLETE};

Result solve(char** board);
bool checkSpace(char space, char* owner);

int main()
{
	int T;
	char strBuff[6];

	char** board = new char*[4];
	for (int i = 0; i < 4; i++)
		board[i] = new char[4];
	


	ifstream fin;
	fin.open("A.txt", ifstream::in);

	ofstream fout;
	fout.open("Output.txt", ofstream::out);

	fin.getline(strBuff, 6);

	sscanf(strBuff, "%d", &T);

	for (int i = 0; i < T; i++)
	{
		fout << "Case #" << (i+1) << ": ";

		for (int j = 0; j < 4; j++)
		{

			
			for (int k = 0; k < 4; k++)
			{
				fin.get(board[j][k]);
//				cout << board[j][k];
			}
			fin.get();
//			cout << "\n";
		}
		fin.getline(strBuff,6);//get past empty space
//		cout << "\n";

		switch (solve(board))
		{
		case XWON:
			fout << "X won\n";
			break;
		case OWON:
			fout << "O won\n";
			break;
		case DRAW:
			fout << "Draw\n";
			break;
		case INCOMPLETE:
			fout << "Game has not completed\n";
		}

	}
	fout.close();
	
	fin.close();

//	cin.get();
}

Result solve(char** board)
{
	int nEmpty = 0;
	char ownerh;
	char ownerv;

	for (int i = 0; i < 4; i++)
	{
		//first check for horizontal/vertical victory
		ownerh = 0;
		ownerv = 0;
		
		for (int j = 0; j < 4; j++)
		{
			if (!checkSpace(board[i][j], &ownerh)) nEmpty++;
			checkSpace(board[j][i], &ownerv);
		}
		if (ownerv == 'X' || ownerh == 'X') return XWON;
		if (ownerv == 'O' || ownerh == 'O') return OWON;

	}
	//now check for diagonal victory
	ownerh = 0;
	ownerv = 0;
	for (int i = 0; i < 4; i++)
	{
		checkSpace(board[i][i], &ownerh);
		checkSpace(board[i][3-i], &ownerv);
	}
	if (ownerv == 'X' || ownerh == 'X') return XWON;
	if (ownerv == 'O' || ownerh == 'O') return OWON;

	if (nEmpty) return INCOMPLETE;
	return DRAW;
}

bool checkSpace(char space, char* owner)
{
	switch (space)
	{
	case '.':
		*owner = '.';
		return false;
		break;
	case 'T':
		break;
	case 'X':
		if (*owner == 0 || *owner == 'X')
		{
			*owner = 'X';
		}
		else
		{
			*owner = '.';
		}
		break;
	case 'O':
		if (*owner == 0 || *owner == 'O')
		{
			*owner = 'O';
		}
		else
		{
			*owner = '.';
		}

	}
	return true;
}