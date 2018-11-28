#include <iostream>
#include <string>

using namespace std;

enum Status
{
    XWon,
    OWon,
    Draw,
    Incomplete
};

Status CheckforStatus(char board[][4]);

int main()
{
    int numCases;
    cin >> numCases;
    for (int caseNum = 1; caseNum <= numCases; caseNum++)
    {
	char board[4][4];
	string line;
	for (int i = 0; i < 4; i++)
	{
	    cin >> line;
	    for (int j = 0; j < 4; j++)
	    {
		board[i][j] = line[j];
	    }
	}
	Status status = CheckforStatus(board);
	switch(status)
	{
	case XWon:
	    cout << "Case #" << caseNum << ": X won" << endl;
	    break;
	case OWon:
	    cout << "Case #" << caseNum << ": O won" << endl;
	    break;
	case Draw:
	    cout << "Case #" << caseNum << ": Draw" << endl;
	    break;
	case Incomplete:
	    cout << "Case #" << caseNum << ": Game has not completed" << endl;
	    break;
	}
    }
}

Status CheckforStatus(char board[][4])
{
    for (int y = 0; y < 4; y++)
    {
	int X = 0;
	int O = 0;
	for (int x = 0; x < 4; x++)
	{
	    if (board[y][x] == 'X' || board[y][x] == 'T')
	    {
		X++;
	    }
	    if (board[y][x] == 'O' || board[y][x] == 'T')
	    {
		O++;
	    }
	}
	if (X == 4)
	{
	    return XWon;
	}
	if (O == 4)
	{
	    return OWon;
	}
    }
    for (int x = 0; x < 4; x++)
    {
	int X = 0;
	int O = 0;
	for (int y = 0; y < 4; y++)
	{
	    if (board[y][x] == 'X' || board[y][x] == 'T')
	    {
		X++;
	    }
	    if (board[y][x] == 'O' || board[y][x] == 'T')
	    {
		O++;
	    }
	}
	if (X == 4)
	{
	    return XWon;
	}
	if (O == 4)
	{
	    return OWon;
	}
    }
    int X = 0;
    int O = 0;
    for (int x = 0; x < 4; x++)
    {
	if (board[x][x] == 'X' || board[x][x] == 'T')
	{
	    X++;
	}
	if (board[x][x] == 'O' || board[x][x] == 'T')
	{
	    O++;
	}
    }
    if (X == 4)
    {
	return XWon;
    }
    if (O == 4)
    {
	return OWon;
    }
    X = 0;
    O = 0;
    for (int x = 0; x < 4; x++)
    {
	if (board[x][3-x] == 'X' || board[x][3-x] == 'T')
	{
	    X++;
	}
	if (board[x][3-x] == 'O' || board[x][3-x] == 'T')
	{
	    O++;
	}
    }
    if (X == 4)
    {
	return XWon;
    }
    if (O == 4)
    {
	return OWon;
    }
    // either draw or incomplete
    for (int y = 0; y < 4; y++)
    {
	for (int x = 0; x < 4; x++)
	{
	    if (board[y][x] == '.')
	    {
		return Incomplete;
	    }
	}
    }
    return Draw;
}
	    
