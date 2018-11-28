#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>

using namespace std;




int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
 
	char board[4][4]={'.'};

	int t;

	cin >> t;

	int xcount = 0, ocount = 0;

	bool xvin = false;

	bool ovin = false;

	for (int i = 0; i < t; i++)
	{

		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> board[j][k];
			}
		}
		xcount = 0;
		ocount = 0;

		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if ( board[j][k] == 'X' || board[j][k] == 'T' ) xcount++;
				if ( board[j][k] == 'O' || board[j][k] == 'T' ) ocount++;
			}

			if ( xcount == 4 ) { xvin = true; break; }
			if ( ocount == 4 ) ovin = true;

			xcount = 0;
			ocount = 0;
		}

		for (int j = 0; j < 4 && !xvin; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if ( board[k][j] == 'X' || board[k][j] == 'T' ) xcount++;
				if ( board[k][j] == 'O' || board[k][j] == 'T' ) ocount++;
			}

			if ( xcount == 4 ) { xvin = true; break; }
			if ( ocount == 4 ) ovin = true;

			xcount = 0;
			ocount = 0;
		}


		for (int j = 0; j < 4 && !xvin; j++)
		{
			if ( board[j][j] == 'X' || board[j][j] == 'T' ) xcount++;
			if ( board[j][j] == 'O' || board[j][j] == 'T' ) ocount++;
		}

			if ( xcount == 4 ) xvin = true;
			if ( ocount == 4 ) ovin = true;

			xcount = 0;
			ocount = 0;

			for (int j = 0; j < 4 && !xvin; j++)
			{
				if ( board[j][4-j-1] == 'X' || board[j][4-j-1] == 'T' ) xcount++;
				if ( board[j][4-j-1] == 'O' || board[j][4-j-1] == 'T' ) ocount++;
			}


			if ( xcount == 4 ) xvin = true;
			if ( ocount == 4 ) ovin = true;

			xcount = 0;
			ocount = 0;

			cout << "Case #" << i+1 << ':' << ' ';

			if ( xvin ) { cout << "X won" << endl; xvin = false; ovin = false; continue;}
			else if ( ovin ) { cout << "O won" << endl; xvin = false; ovin = false; continue;}

			bool ispoint = false;

			for (int j = 0; j < 4; j++)
			{
				for (int k = 0; k < 4; k++)
				{
					if ( board[j][k] == '.' ) {ispoint = true; break;}
				}
				if (ispoint) break;
			}

			if (ispoint) cout << "Game has not completed" << endl;
			else cout << "Draw" << endl;

			xvin = false;
			ovin = false;

	}


	//system("pause");
	return 0;
}
