#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	char winner;
	int tPos = 0;
	int dotCount;

	for(int t = 0; t < T; t++)
	{
		char d[16];
		dotCount = 0;

		for(int i = 0; i < 16; i++)
		{
			cin >> d[i];
			if(d[i] == 'T')
				tPos = i;
			else if(d[i] == '.')
				dotCount++;
		}

		d[tPos] = 'O';
		winner = '.';
		//For each row
		for(int r = 0; r < 4; r++)
		{
			if(d[r] == 'O' && d[r+4] == 'O'&& d[r+8] == 'O' && d[r+12] == 'O')
				winner = 'O';

			if(d[r] == 'X' && d[r+4] == 'X' && d[r+8] == 'X' && d[r+12] == 'X')
				winner = 'X';
		}

		//For Each col
		for(int c = 0; c <= 12; c+=4)
		{
			if(d[c] == 'O' && d[c+1] == 'O' && d[c+2] == 'O'&& d[c+3] == 'O')
				winner = 'O';

			if(d[c] == 'X' && d[c+1] == 'X' && d[c+2] == 'X'&& d[c+3] == 'X')
				winner = 'X';
		}

		//Diags
		if(d[0] == 'O' &&  d[5] == 'O' && d[10] == 'O' && d[15] == 'O')
			winner = 'O';
		else if(d[0] == 'X' &&  d[5] == 'X' && d[10] == 'X' && d[15] == 'X')
			winner = 'X';
		else if(d[3] == 'O' &&  d[6] == 'O' && d[9] == 'O' && d[12] == 'O')
			winner = 'O';
		else if(d[3] == 'X' &&  d[6] == 'X' && d[9] == 'X' && d[12] == 'X')
			winner = 'X';

		d[tPos] = 'X';
		
		//For each row
		for(int r = 0; r < 4; r++)
		{
			if(d[r] == 'O' && d[r+4] == 'O'&& d[r+8] == 'O' && d[r+12] == 'O')
				winner = 'O';

			if(d[r] == 'X' && d[r+4] == 'X' && d[r+8] == 'X' && d[r+12] == 'X')
				winner = 'X';
		}

		//For Each col
		for(int c = 0; c <= 12; c+=4)
		{
			if(d[c] == 'O' && d[c+1] == 'O' && d[c+2] == 'O'&& d[c+3] == 'O')
				winner = 'O';

			if(d[c] == 'X' && d[c+1] == 'X' && d[c+2] == 'X'&& d[c+3] == 'X')
				winner = 'X';
		}

//Diags
		if(d[0] == 'O' &&  d[5] == 'O' && d[10] == 'O' && d[15] == 'O')
			winner = 'O';
		else if(d[0] == 'X' &&  d[5] == 'X' && d[10] == 'X' && d[15] == 'X')
			winner = 'X';
		else if(d[3] == 'O' &&  d[6] == 'O' && d[9] == 'O' && d[12] == 'O')
			winner = 'O';
		else if(d[3] == 'X' &&  d[6] == 'X' && d[9] == 'X' && d[12] == 'X')
			winner = 'X';

/*
		string msg = "";
		if(winner == 'X')
			msg = "X won";
		else if(winner == 'Y')
			msg = "Y won";
		else if(dotCount > 0)
			msg = "Game has not completed";
		else
			msg = "Draw";*/

		cout << "Case #" << (t+1) << ": " <<  (winner == 'X' ? "X won" : (winner == 'O' ? "O won" : (dotCount > 0 ? "Game has not completed" : "Draw"))) << endl;

		//for(int i = 0; i < 16; i++)
		//	cout << d[i];

	}
}