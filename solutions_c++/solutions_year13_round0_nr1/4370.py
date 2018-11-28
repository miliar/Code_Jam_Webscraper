#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>

#define REACHED cout << "REACHED" << endl;

using namespace std;

void processBoard(int caseNum);
int isWin(char c[]);
bool processWinResult(int val, int caseNum);


ifstream in;
ofstream out;

int main (void)
{		
	in.open("A-large.in");
	out.open("output.txt");

	int T;
	in >> T;

	for (int i = 0; i < T; i++)
	{
		processBoard(i+1);
		string s;
		getline(in, s);
	}

	in.close();
	out.close();
	return 0;
}

void processBoard(int caseNum)
{
	char b[4][4];
	bool existsDot = false;

	for (int i = 0; i < 4; i++)
	{
		in >> b[i][0] >> b[i][1] >> b[i][2] >> b[i][3];
		//cout << b[i][0] << b[i][1] << b[i][2] << b[i][3] << endl;;
		if (!existsDot && (b[i][0] == '.' || b[i][1] == '.' || b[i][2] == '.' || b[i][3] == '.'))
		{
			existsDot = true;
		}
	}

	//looping through rows and columns
	for (int i = 0; i < 4; i++)
	{
		char row[4] = {b[i][0], b[i][1], b[i][2], b[i][3]};
		char col[4] = {b[0][i], b[1][i], b[2][i], b[3][i]};
		bool rowProcess = processWinResult(isWin(row), caseNum);
		if (rowProcess) return;
		bool colProcess = processWinResult(isWin(col), caseNum);
		if (colProcess) return;
	}

	char diag1[4] = {b[0][0], b[1][1], b[2][2], b[3][3]};
	char diag2[4] = {b[0][3], b[1][2], b[2][1], b[3][0]};
	bool diag1process = processWinResult(isWin(diag1), caseNum);
	//cout << "Case: " << caseNum << " " << isWin(diag1) << endl;
	//cout << "Case: " << caseNum << " " << isWin(diag2) << endl;

	if (diag1process) return;
	bool diag2process = processWinResult(isWin(diag2), caseNum);
	if (diag2process) return;

	if (existsDot)
	{
		out << "Case #" << caseNum << ": Game has not completed\n";
	}
	else
	{
		out << "Case #" << caseNum << ": Draw\n";
	}
	return;

}

//returns -1 if no win, 1 if player 1 win, 2 if player 2 win
int isWin(char c[])
{
	int p1count = 0, p2count = 0;
	for (int i = 0; i < 4; i++)
	{
		if (c[i] == 'T')
		{
			p1count++;
			p2count++;
		}
		if (c[i] == 'O') p1count++;
		if (c[i] == 'X') p2count++;
	}

	if (p1count >= 4) 
	{
		return 1;
	}
	if (p2count >= 4) 
	{
		return 2;
	}
	else return -1;
}

bool processWinResult(int val, int caseNum)
{
	if (val == -1) return false;
	if (val == 1)
	{
		out << "Case #" << caseNum << ": O won\n";
	}
	if (val == 2)
	{
		out << "Case #" << caseNum << ": X won\n";
	}
	return true;
}