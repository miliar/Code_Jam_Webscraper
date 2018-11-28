#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>

using namespace std;

char board[8][8], mark;
int T, M;

int main (int argc, char const* argv[])
{
	ifstream cin ("A-large.in");
	ofstream cout ("A-large.out");
	cin >> T;
	for (int t = 0; t < T; t += 1)
	{
		M = 3; // draw
		int flag = 0;
		for (int i = 0; i < 4; i += 1)
		{
			for (int j = 0; j < 4; j += 1)
			{
				cin >> board[i][j];
				if ( board[i][j] == '.' ) M = 2;
			}
		}
		// Now checking
		mark = 'X'; // check X first
		for (int i = 0; i < 4; i += 1)
		{
			int flag = 0;
			for (int j = 0; j < 4; j += 1) //checking rows
			{
				if( board [i][j] == mark || board [i][j] == 'T')
					flag++;
			}
			if (flag == 4)
			{
				M = 1;
				goto hell;
			}
			flag = 0;
			for (int j = 0; j < 4; j += 1) //checking columns
			{
				if( board [j][i] == mark || board [j][i] == 'T')
					flag++;
			}
			if (flag == 4)
			{
				M = 1;
				goto hell;
			}
		}
		//check diagonals
		if ( board [0][0] == 'T' || board [0][0] == mark )
		{
			if ( board [1][1] == 'T' || board [1][1] == mark )
			{
				if ( board [2][2] == 'T' || board [2][2] == mark)
				{
					if ( board [3][3] == 'T' || board [3][3] == mark)
					{
						M = 1;
						goto hell;
					}
				}
			}
		}
		if ( board [3][0] == 'T' || board [3][0] == mark )
		{
			if ( board [2][1] == 'T' || board [2][1] == mark )
			{
				if ( board [1][2] == 'T' || board [1][2] == mark)
				{
					if ( board [0][3] == 'T' || board [0][3] == mark)
					{
						M = 1;
						goto hell;
					}
				}
			}
		}
		//finished checking X, now check Y
		mark = 'O';
		for (int i = 0; i < 4; i += 1)
		{
			int flag = 0;
			for (int j = 0; j < 4; j += 1) //checking rows
			{
				if( board [i][j] == mark || board [i][j] == 'T')
					flag++;
			}
			if (flag == 4)
			{
				M = 0;
				goto hell;
			}
			flag = 0;
			for (int j = 0; j < 4; j += 1) //checking columns
			{
				if( board [j][i] == mark || board [j][i] == 'T')
					flag++;
			}
			if (flag == 4)
			{
				M = 0;
				goto hell;
			}
		}
		//check diagonals
		if ( board [0][0] == 'T' || board [0][0] == mark )
		{
			if ( board [1][1] == 'T' || board [1][1] == mark )
			{
				if ( board [2][2] == 'T' || board [2][2] == mark)
				{
					if ( board [3][3] == 'T' || board [3][3] == mark)
					{
						M = 0;
						goto hell;
					}
				}
			}
		}
		if ( board [3][0] == 'T' || board [3][0] == mark )
		{
			if ( board [2][1] == 'T' || board [2][1] == mark )
			{
				if ( board [1][2] == 'T' || board [1][2] == mark)
				{
					if ( board [0][3] == 'T' || board [0][3] == mark)
					{
						M = 0;
						goto hell;
					}
				}
			}
		}

		hell:
		cout << "Case #" << t+1 <<": ";
		if (M == 3) cout << "Draw\n";
		else if (M == 2) cout << "Game has not completed\n";
		else if (M == 1) cout << "X won\n";
		else if (M == 0) cout << "O won\n";
	}
	return 0;
}
