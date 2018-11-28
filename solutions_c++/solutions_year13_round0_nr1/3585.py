#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char* argv[])
{
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);

	int T;
	cin >> T;
	char B[4][4];
	for (int t=0; t<T; t++)
	{
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> B[i][j];
		bool x[4][4], o[4][4], finished = true;
		for (int i=0; i<4; i++)
		{
			for (int j=0; j<4; j++)
			{
				if (B[i][j] == 'X') { x[i][j] = true; o[i][j] = false; }
				else if (B[i][j] == 'O') { x[i][j] = false; o[i][j] = true; }
				else if (B[i][j] == 'T') { x[i][j] = true; o[i][j] = true; }
				else { x[i][j] = false; o[i][j] = false; finished = false; }
			}
		}

		bool xWin = false, oWin = false;
		for (int i=0; i<4; i++)
		{
			if (x[i][0] && x[i][1] && x[i][2] && x[i][3])
				xWin = true;
			if (o[i][0] && o[i][1] && o[i][2] && o[i][3])
				oWin = true;
		}
		for (int j=0; j<4; j++)
		{
			if (x[0][j] && x[1][j] && x[2][j] && x[3][j])
				xWin = true;
			if (o[0][j] && o[1][j] && o[2][j] && o[3][j])
				oWin = true;
		}
		if (x[0][0] && x[1][1] && x[2][2] && x[3][3])
			xWin = true;
		if (o[0][0] && o[1][1] && o[2][2] && o[3][3])
			oWin = true;
		if (x[0][3] && x[1][2] && x[2][1] && x[3][0])
			xWin = true;
		if (o[0][3] && o[1][2] && o[2][1] && o[3][0])
			oWin = true;

		cout << "Case #" << t+1 << ": ";
		if (xWin)
			cout << "X won";
		else if (oWin)
			cout << "O won";
		else if (finished)
			cout << "Draw";
		else
			cout << "Game has not completed";
		cout << endl;

	}

	return 0;
}


