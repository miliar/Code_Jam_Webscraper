#include <iostream>
using namespace std;

int main()
{
	int t;
	char board[4][4];
	char emptyline;
	int counto;
	int countx;
	int countov;
	int countxv;
	bool xwin;
	bool owin;
	bool emptypresent;

	cin >> t;

	for(int i = 0; i < t; i++)
	{
		counto = 0;
		countx = 0;
		countov = 0;
		countxv = 0;
		xwin = false;
		owin = false;
		emptypresent = false;
		
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				cin >> board[j][k];

				if(board[j][k] == '.')
					emptypresent = true;
			}

			//cin >> emptyline;
		}

		cin.get();
		cin.get();

		for(int j = 0; j < 4; j++)
		{
			countx = 0;
			counto = 0;
			countxv = 0;
			countov = 0;

			for(int k = 0; k < 4; k++)
			{
				if(board[j][k]=='X')
				{
					countx++;
					counto = 0;
				}
				else if(board[j][k]=='O')
				{
					counto++;
					countx = 0;
				}
				else if(board[j][k]=='T')
				{
					counto++;
					countx++;
				}
				else
				{
					counto = 0;
					countx = 0;
				}

				if(board[k][j] == 'X')
				{
					countxv++;
					countov = 0;
				}
				else if(board[k][j]=='O')
				{
					countov++;
					countxv =0 ;
				}
				else if(board[k][j]=='T')
				{
					countov++;
					countxv++;
				}
				else
				{
					countov = 0;
					countxv = 0;
				}
			}

			if(counto == 4 || countov == 4)
				owin = true;

			if(countx == 4 || countxv == 4)
				xwin = true;
		}

		if(!(owin && xwin))
		{
			counto = 0;
			countx = 0;

			for(int j = 0; j < 4; j++)
			{
				if(board[j][j] == 'X')
				{
					countx++;
					counto = 0;
				}
				else if(board[j][j] == 'O')
				{
					counto++;
					countx = 0;
				}
				else if(board[j][j] == 'T')
				{
					counto++;
					countx++;
				}
				else
				{
					counto = 0;
					countx = 0;
				}
			}

			if(counto == 4 )
				owin = true;

			if(countx == 4 )
				xwin = true;
		}

		if(!(owin && xwin))
		{
			counto = 0;
			countx = 0;

			for(int j = 3, k = 0; j >= 0 && k < 4; j--, k++)
			{
				if(board[j][k] == 'X')
				{
					countx++;
					counto = 0;
				}
				else if(board[j][k]=='O')
				{
					counto++;
					countx = 0;
				}
				else if(board[j][k]=='T')
				{
					counto++;
					countx++;
				}
				else
				{
					counto = 0;
					countx = 0;
				}
			}

			if(counto == 4 )
				owin = true;

			if(countx == 4 )
				xwin = true;
		}

		cout << "Case #" << i + 1 << ": ";

		if((owin && xwin) || (owin == false && xwin == false && emptypresent == false ))
		{
			cout << "Draw" << endl;
		}
		else if(owin)
		{
			cout << "O won" << endl;
		}
		else if(xwin)
		{
			cout << "X won" << endl;
		}
		else if(emptypresent == true)
		{
			cout << "Game has not completed" << endl;
		}
	}

	return 0;
}