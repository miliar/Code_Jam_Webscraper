#include <iostream>
#include <fstream>
#include <vector>

#define BUF_SIZE 10

using namespace std;

enum Result {X_Won, O_Won, Draw, Not_Over, Unknown};

typedef struct
{
    char board[4][4];
    Result result;
} Game;

char checkWin(char b1, char b2, char b3, char b4)
{
    if ((b1 == 'O') && (b2 == 'O') && (b3 == 'O') && (b4 == 'O'))
	return 'O';
    else if ((b1 == 'T') && (b2 == 'O') && (b3 == 'O') && (b4 == 'O'))
	return 'O';
    else if ((b1 == 'O') && (b2 == 'T') && (b3 == 'O') && (b4 == 'O'))
	return 'O';
    else if ((b1 == 'O') && (b2 == 'O') && (b3 == 'T') && (b4 == 'O'))
	return 'O';
    else if ((b1 == 'O') && (b2 == 'O') && (b3 == 'O') && (b4 == 'T'))
	return 'O';
    else if ((b1 == 'X') && (b2 == 'X') && (b3 == 'X') && (b4 == 'X'))
	return 'X';
    else if ((b1 == 'T') && (b2 == 'X') && (b3 == 'X') && (b4 == 'X'))
	return 'X';
    else if ((b1 == 'X') && (b2 == 'T') && (b3 == 'X') && (b4 == 'X'))
	return 'X';
    else if ((b1 == 'X') && (b2 == 'X') && (b3 == 'T') && (b4 == 'X'))
	return 'X';
    else if ((b1 == 'X') && (b2 == 'X') && (b3 == 'X') && (b4 == 'T'))
	return 'X';
    else
	return '.';
}

int main()
{
    //ifstream fin("input.txt", ios::in);
    //ifstream fin("A-small-attempt0.in", ios::in);
    ifstream fin("A-large.in", ios::in);
    
    int N;
    fin >> N;

    char buffer[BUF_SIZE];
    fin.getline(buffer, BUF_SIZE, '\n');
    vector<Game> games;
    bool hasEmpty = false;
    for (int g = 0; g < N; ++g) // game
    {
//	cout << g+1 << endl; 
	Game game;
	game.result = Unknown;
	hasEmpty = false;
	for (int r = 0; r < 4; ++r)
	{
	    fin.getline(buffer, BUF_SIZE, '\n');
//	    cout << "buffer " << r << ": " << buffer << endl;
	    for (int c = 0; c < 4; ++c)
	    {
		if (buffer[c] == '.')
		{
		    hasEmpty = true;
		}
		game.board[r][c] = buffer[c];
	    }
	}
//	cout << endl;
	fin.getline(buffer, BUF_SIZE, '\n');
	
/*	for (int r = 0; r < 4; ++r)
	{
	    cout << game.board[r][0] << game.board[r][1] << game.board[r][2] << game.board[r][3] << endl;
	}
	cout << endl;
*/	
	char check = '.';

	// Check rows
	for (int r = 0; r < 4; ++r)
	{
	    check = checkWin(game.board[r][0], game.board[r][1], game.board[r][2], game.board[r][3]);
	    if (check == 'X')
	    {
		game.result = X_Won;
		break;
	    }
	    else if (check == 'O')
	    {
		game.result = O_Won;
		break;
	    }
	}
	
	if (game.result != Unknown)
	{
	    games.push_back(game);
	    continue;
	}

	// Check cols
	for (int c = 0; c < 4; ++c)
	{
	    check = checkWin(game.board[0][c], game.board[1][c], game.board[2][c], game.board[3][c]);
	    if (check == 'X')
	    {
		game.result = X_Won;
		break;
	    }
	    else if (check == 'O')
	    {
		game.result = O_Won;
		break;
	    }
	}
	
	if (game.result != Unknown)
	{
	    games.push_back(game);
	    continue;
	}
	
        // Check diag 1
	check = checkWin(game.board[0][0], game.board[1][1], game.board[2][2], game.board[3][3]);
	if (check == 'X')
	{
	    game.result = X_Won;
	    games.push_back(game);
	    continue;
	}
	else if (check == 'O')
	{
	    game.result = O_Won;
	    games.push_back(game);
	    continue;
	}
	
	// Check diag 2
	check = checkWin(game.board[3][0], game.board[2][1], game.board[1][2], game.board[0][3]);
	if (check == 'X')
	{
	    game.result = X_Won;
	    games.push_back(game);
	    continue;
	}
	else if (check == 'O')
	{
	    game.result = O_Won;
	    games.push_back(game);
	    continue;
	}

	if (hasEmpty == true)
	    game.result = Not_Over;
	else
	    game.result = Draw;
	games.push_back(game);
    }

    ofstream fout("output.txt", ios::out);
    for (int g = 0; g < N; ++g)
    {
	fout << "Case #" << g+1 << ": ";
	if (games[g].result == X_Won)
	    fout << "X won" << endl;
	else if (games[g].result == O_Won)
	    fout << "O won" << endl;
	else if (games[g].result == Draw)
	    fout << "Draw" << endl;
	else
	    fout << "Game has not completed" << endl;
    }

    return 0;
}
