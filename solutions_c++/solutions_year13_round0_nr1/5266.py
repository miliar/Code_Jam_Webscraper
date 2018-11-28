#include <iostream>

using namespace std;

int main()
{
    int t;
    char board[4][4];
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
	cout << "Case #" << i+1 << ": ";

	bool full=true, xwin=true, ywin=true;
	bool sawx=false, sawy=false, done=false;

	// Read board
	for (int j = 0; j < 4; ++j)
	{
	    cin >> board[j][0] >> board[j][1] >> board[j][2] >> board[j][3];
	}
	
	// Rows
	//cout << "Rows" << endl;
	for (int j = 0; j < 4; ++j)
	{
	    sawx = false; sawy = false; done = false;
	    for (int k = 0; k < 4; ++k)
	    {
		if (board[j][k] == 'X')
		    sawx = true;
		else if (board[j][k] == 'O')
		    sawy = true;
		else if (board[j][k] != 'T')
		{
		    full = false;
		    done = true;
		    break;
		}
	    }
	    if (done)
		continue;

	    if (sawx && !sawy)
		ywin = false;
	    else if (sawy && !sawx)
		xwin = false;
	}
	//cout << "DEBUG " << ywin << "," << xwin << "," << full << endl;


	// Columns
	//cout << "Columns" << endl;
	for (int j = 0; j < 4; ++j)
	{
	    sawx = false; sawy = false; done = false;
	    for (int k = 0; k < 4; ++k)
	    {
		if (board[k][j] == 'X')
		    sawx = true;
		else if (board[k][j] == 'O')
		    sawy = true;
		else if (board[k][j] != 'T')
		{
		    full = false;
		    done = true;
		    break;
		}
	    }
	    if (done)
		continue;


	    if (sawx && !sawy)
		ywin = false;
	    else if (sawy && !sawx)
		xwin = false;
	}
	//cout << "DEBUG " << ywin << "," << xwin << "," << full << endl;


	// Diagonals
	//cout << "Diagonals" << endl;
	sawx = false; sawy = false; done = false;
	for (int j = 0; j < 4; ++j)
	{
	    if (board[j][j] == 'X')
		sawx = true;
	    else if (board[j][j] == 'O')
		sawy = true;
	    else if (board[j][j] != 'T')
	    {
		full = false;
		done = true;
		break;
	    }
	}

	if(!done)
	{
	    if (sawx && !sawy)
		ywin = false;
	    else if (sawy && !sawx)
		xwin = false;
	}

	sawx = false; sawy = false; done = false;
	for (int j = 0; j < 4; ++j)
	{
	    if (board[j][3-j] == 'X')
		sawx = true;
	    else if (board[j][3-j] == 'O')
		sawy = true;
	    else if (board[j][3-j] != 'T')
	    {
		full = false;
		done = true;
		break;
	    }
	}
	if(!done)
	{
	    if (sawx && !sawy)
		ywin = false;
	    else if (sawy && !sawx)
		xwin = false;
	}
	//cout << "DEBUG " << ywin << "," << xwin << "," << full << endl;


	// Check for X win or Y win
	//cout << "DEBUG " << ywin << "," << xwin << "," << full << endl;
	/*
	for (int j=0; j<4; ++j)
	{
	    for (int k=0; k<4; ++k)
	    {
		cout << board[j][k];
	    }
	    cout << endl;
	}
	*/
	if (ywin && !xwin)
	    cout << "O won" << endl;
	else if (xwin && !ywin)
	    cout << "X won" << endl;
	else if (full)
	    cout << "Draw" << endl;
	else
	    cout << "Game has not completed" << endl;
    }
}
