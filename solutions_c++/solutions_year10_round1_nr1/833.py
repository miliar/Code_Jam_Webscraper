#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;


int main (int argc, char *argv[])
{
	int T, t, N, K, k;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cin >> N >> K;
		//cout << "N is " << N << " and K is " << K << endl;
		char board[N][N];
		for (int n = 0; n < N; n++)
		{
			int npieces = 0;
			string line;
			cin >> line;
			//cout << "Read in: " << line << endl;
			for (int n2 = 0; n2 < N; n2++)
			{
				char piece;
				piece = line[n2];
				//board[n][(N-1)-n2] = piece;
				board[n][n2] = piece;
				if (piece != '.')
					npieces++;
			}
			//cout << "npieces is " << npieces << endl;
			int i = N-1; int p = 0;
			while (p < npieces)
			{
				//cout << "Letter at i " << i << " p " << p << " is " << board[n][i] << endl;
				if (board[n][i] != '.')
				{
					p++; i--;
				}
				else
				{
					//cout << "Doing a shuffle at i = " << i << endl;
					while (board[n][i] == '.' && i != 0)
					{
						//cout << "One shuffle loop." << endl;
						for (int z = i; z > 0; z--)
						{
							board[n][z] = board[n][z-1];
						}
						board[n][0] = '.';
					}
				}
			}
		}
		for (int n= 0; n < N; n++)
		{
			char tmp[N];
			for (int n2= 0; n2 < N; n2++)
			{
				tmp[(N-1)-n2] = board[n2][n];
			}
			for (int n2= 0; n2 < N; n2++)
			{
				board[n2][n] = tmp[n2];
			}
		}
		/*cout << "Rotatoed board:" << endl;
		for (int n= 0; n < N; n++)
		{
			for (int n2 = 0; n2 < N; n2++)
			{
				cout << board[n2][n];
			}
			cout << endl;
		}*/
		// RIGHT board[col][row] is gravitised by here
		bool rwins = false;
		bool bwins = false;
		for (int col = 0; col < N; col++)
		{
			for (int row = 0; row < N; row++)
			{
				bool rowstraight = true, colstraight = true, diagstraight = true, ldiagstraight = true;
				char target = board[col][row];
				if (target == '.') continue;
				for (int x = 1; x < K; x++)
				{
					if (row+x >= N)
						rowstraight = false;
					if ((row+x < N) && (board[col][row+x] != target))
						rowstraight = false;
				}
				for (int x = 1; x < K; x++)
				{
					if (col+x >= N)
						colstraight = false;
					if ((col+x < N) && (board[col+x][row] != target))
						colstraight = false;
				}
				for (int x = 1; x < K; x++)
				{
					if ((col+x >= N) || (row+x >= N))
						diagstraight = false;
					if ((col+x < N) && (row+x < N) && (board[col+x][row+x] != target))
						diagstraight = false;
				}
				for (int x = 1; x < K; x++)
				{
					if ((col-x < 0) || (row+x >= N))
						ldiagstraight = false;
					if ((col-x >= 0) && (row+x < N) && (board[col-x][row+x] != target))
						ldiagstraight = false;
				}
				if ((rowstraight || colstraight || diagstraight || ldiagstraight) && (target == 'R'))
					rwins = true;
				if ((rowstraight || colstraight || diagstraight || ldiagstraight) && (target == 'B'))
					bwins = true;
			}
		}
		cout << "Case #" << t << ": ";
		if (rwins && bwins)
			cout << "Both";
		if (rwins && !bwins)
			cout << "Red";
		if (bwins && !rwins)
			cout << "Blue";
		if (!bwins && !rwins)
			cout << "Neither";
		
		cout << endl;
	}
	
	return 0;
}


