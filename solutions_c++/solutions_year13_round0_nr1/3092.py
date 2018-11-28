#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool over ;

bool Judge(vector<string>& board, char ch)
{
    int chCount , tCount;
    for(int i = 0; i < 4; ++i)
    {
	chCount = 0; 
	tCount = 0;
	for(int col = 0; col < 4; ++col)
	{
	    if(board[i][col] == '.')
	    {
		over = false;
		continue;
	    }
	    if(board[i][col] == ch)
		++chCount;
	    else if(board[i][col] == 'T')
		++tCount;
	}
	if(chCount == 4 || (chCount == 3 && tCount == 1))
	    return true;

	chCount = 0; 
	tCount = 0;
	for(int row = 0; row < 4; ++row)
	{
	    if(board[row][i] == ch)
		++chCount;
	    else if(board[row][i] == 'T')
		++tCount;
	}
	if(chCount == 4 || (chCount == 3 && tCount == 1))
	    return true;
    }

    chCount = 0;
    tCount = 0;

    int chCount1 = 0, tCount1 = 0;
    for(int i = 0; i < 4; ++i)
    {
	if(board[i][i] == ch)
	    ++chCount;
	else if(board[i][i] == 'T')
	    ++tCount;

	if(board[i][3-i] == ch)
	    ++chCount1;
	else if(board[i][3-i] == 'T')
	    ++tCount1;
    }
    if(chCount == 4 || (chCount == 3 && tCount == 1))
	return true;
    if(chCount1 == 4 || (chCount1 == 3 && tCount1 == 1))
	return true;

    return false;
}

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
	vector<string> board;
	for(int j = 0; j < 4; ++j)
	{
	    string temp;
	    cin >> temp;
	    board.push_back(temp);
	}

	over = true;
	bool xwin = Judge(board, 'X');
	bool owin = Judge(board, 'O');

	cout << "Case #" << i << ": ";
	if( xwin )
	    cout << "X won";
	else if( owin )
	    cout << "O won";
	else if( over )
	    cout << "Draw";
	else cout << "Game has not completed";
	cout << endl;
    }
}
