#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void StoreCredit(int C, int I, int P[], int* res);
string isWon(char Line[4], bool* completed);
string TicTacToeTomek(char Board[4][4]);

int main()
{
	ifstream fi;
	ofstream fo;
	string res,strTmp;
	char out[255];
	int N,i,j,k;
	char Board[4][4];

	fi.open ("A-large.in");
	fo.open("A-large.out");

	// Get number of cases, N
	getline(fi,strTmp);
	N = atoi(strTmp.c_str());

	for (i = 0; i<N ; i++)
	{
		// Get board value
		for (j=0;j<4;j++)
		{
			getline(fi,strTmp);
			for (k=0;k<4;k++)
			{
				Board[j][k]=strTmp[k];
			}
		}

		// Read empty line
		getline(fi,strTmp);

		// Write result to file
		res = TicTacToeTomek(Board);
		sprintf_s(out,"Case #%d: %s\n",i+1,res.c_str());
		fo.write(out,strlen(out));
	}

	fi.close();
	fo.close();
	return 0;
}

string TicTacToeTomek(char Board[4][4])
{
	int j,k;
	bool won, completed;
	string res;
	char Line[4];
	completed = true;
	for (j=0;j<4;j++)
	{
		// Check for horizontal line
		res = isWon(Board[j], &completed);
		if (res != "-") { return (res + " won"); }

		// Check for vertical line
		for (k=0;k<4;k++) { Line[k] = Board[k][j]; }
		res = isWon(Line, &completed);
		if (res != "-") { return (res + " won"); }
	}
	// Check for diagonal line
	for (k=0;k<4;k++) { Line[k] = Board[k][k]; }
	res = isWon(Line, &completed);
	if (res != "-") { return (res + " won"); }

	for (k=0;k<4;k++) { Line[k] = Board[k][3-k]; }
	res = isWon(Line, &completed);
	if (res != "-") { return (res + " won"); }

	// Otherwise return
	if (completed) return "Draw";
	else return "Game has not completed";
}

string isWon(char Line[4], bool* completed)
{
	char op = 0;
	for (int i=0;i<4;i++)
	{
		if (Line[i] == '.') { *completed = false; return "-"; }
		if (Line[i]=='X' || Line[i]=='O')
		{
			if (op==0) op = Line[i];
			if (Line[i] != op) return "-";
		}
	}
	string res;
	res = op;
	return res;
}