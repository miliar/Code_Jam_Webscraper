#include <iostream>
using namespace std;

string ticTacToeResult(char board[][4])
{
    string X = "X won";
    string D = "Draw";
    string N = "Game has not completed";
    string O = "O won";
    int Xcount, Ocount, T;
    bool Empty = false;

    for (int i = 0; i < 4; i++)
    {
	Xcount = 0;
	Ocount = 0;
	T = 0;

	for(int j = 0; j < 4; j++)
	{
	    if (board[i][j] == 'X')
	    {
		Xcount++;
	    }
	    else if (board[i][j] == 'O')
	    {
		Ocount++;
	    }
	    else if (board[i][j] == 'T')
	    {
		T = 1;
	    }		   
	    else if (board[i][j] == '.')
	    {
		Empty = true;
	    }
	}

	//cout << "Row " << i << ": X:" << Xcount << " O:" << Ocount << " T:" << T << endl;

	if ((Xcount == 4) || ((Xcount == 3) && (T == 1)))
	{
	    return X;
	}
	else if ((Ocount == 4) || (Ocount == 3) && (T == 1))
	{
	    return O;
	}
    }

    for (int j = 0; j < 4; j++)
    {
	Xcount = 0;
	Ocount = 0;
	T = 0;

	for(int i = 0; i < 4; i++)
	{
	    if (board[i][j] == 'X')
	    {
		Xcount++;
	    }
	    else if (board[i][j] == 'O')
	    {
		Ocount++;
	    }
	    else if (board[i][j] == 'T')
	    {
		T = 1;
	    }		   
	    else if (board[i][j] == '.')
	    {
		Empty = true;
	    }
	}

	//cout << "Col " << j << ": X:" << Xcount << " O:" << Ocount << " T:" << T << endl;

	if ((Xcount == 4) || ((Xcount == 3) && (T == 1)))
	{
	    return X;
	}
	else if ((Ocount == 4) || (Ocount == 3) && (T == 1))
	{
	    return O;
	}
    }

    Xcount = 0;
    Ocount = 0;
    T = 0;
    
    for (int i = 0; i < 4; i++)
    {
	int j = i;

	if (board[i][j] == 'X')
	{
	    Xcount++;
	}
	else if (board[i][j] == 'O')
	{
	    Ocount++;
	}
	else if (board[i][j] == 'T')
	{
	    T = 1;
	}		   
	else if (board[i][j] == '.')
	{
	    Empty = true;
	}
    
	/*
	if (i == 3)
	{    
	    cout << "Dia(i=j) X:" << Xcount << " O:" << Ocount << " T:" << T << endl;
	}
	*/

	if ((Xcount == 4) || ((Xcount == 3) && (T == 1)))
	{
	    return X;
	}
	else if ((Ocount == 4) || (Ocount == 3) && (T == 1))
	{
	    return O;
	}
    }

    Xcount = 0;
    Ocount = 0;
    T = 0;

    for (int i = 0; i < 4; i++)
    {
	int j = 3 - i;

	if (board[i][j] == 'X')
	{
	    Xcount++;
	}
	else if (board[i][j] == 'O')
	{
	    Ocount++;
	}
	else if (board[i][j] == 'T')
	{
	    T = 1;
	}		   
	else if (board[i][j] == '.')
	{
	    Empty = true;
	}

	/*
	if (i == 3)
	{
	    cout << "Dia(i!=j) X:" << Xcount << " O:" << Ocount << " T:" << T << endl;
	}
	*/	
    	
	if ((Xcount == 4) || ((Xcount == 3) && (T == 1)))
	{
	    return X;
	}
	else if ((Ocount == 4) || (Ocount == 3) && (T == 1))
	{
	    return O;
	}
    }

    if (Empty)
    {
	return N;
    }
    else
    {
	return D;
    }
}

int main()
{
    int T;
    char board[4][4];
    
    cin >> T;

    for (int i = 0; i < T; i++)
    {
	for(int j = 0; j < 4; j++)
	{   
	    cin >> board[j][0] >> board[j][1] >> board[j][2] >> board[j][3];
	}
    
	cout << "Case #" << i+1 << ": " << ticTacToeResult(board) << endl;
    } 

    return 0;
}
