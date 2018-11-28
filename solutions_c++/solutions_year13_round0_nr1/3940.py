#include <iostream>
#include <fstream>
using namespace std;


class Game {
    private:
	char game[4][4];
    public:
	int  dots;
	Game() : dots (0) { for (int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j) game[i][j] = '.'; }
	void read(fstream&);
	bool checkRow(char, int);
	bool checkCol(char, int);
	bool checkDiag(char);
	bool check(char);
};

void Game::read(fstream& f)
{
    for(int i =0; i < 4; ++i) {
	for(int j = 0; j < 4; ++j) {
    	    char c;
	    f >> c;
	    game[i][j] = c;
	    if (c == '.') ++dots;
	}
    }
    return;
}

bool Game::check(char c) 
{
    for(int i = 0; i < 4; ++i) {
	if(checkRow(c, i)) { 
	    // cout <<"Row " << i << " for " << c << endl; 
	    return true; 
	}
	if(checkCol(c, i)) { 
	    // cout <<"Col " << i << " for " << c << endl; 
	    return true; 
	}
    }
    if (checkDiag(c)) {
	// cout << "diag true for " << c << endl; 
	return true;
    }
    return false;
}

bool Game::checkRow(char c, int row)
{
    for(int i = 0; i < 4; ++i) {
	char tc = game[row][i];
	if (tc != c && tc != 'T') {
	    return false;
	}
    }
    return true;
}

bool Game::checkCol(char c, int col)
{
    for(int i = 0; i < 4; ++i) {
	char tc = game[i][col];
	if (tc != c && tc != 'T') {
	    return false;
	}
    }
    return true;
}

bool Game::checkDiag(char c)
{
    bool b1 = (game[0][0] == c || game[0][0] == 'T');
    bool b2 = (game[1][1] == c || game[1][1] == 'T');
    bool b3 = (game[2][2] == c || game[2][2] == 'T');
    bool b4 = (game[3][3] == c || game[3][3] == 'T');
    if (b1 && b2 && b3 && b4) {
	// cout << "D1 true" << endl;
	return true;
    }
    b1 = (game[3][0] == c || game[3][0] == 'T');
    b2 = (game[2][1] == c || game[2][1] == 'T');
    b3 = (game[1][2] == c || game[1][2] == 'T');
    b4 = (game[0][3] == c || game[0][3] == 'T');
    if (b1 && b2 && b3 && b4) {
	// cout << "D2 true" << endl;
	return true;
    }
    return false;
}
int main() 
{

    fstream f("in", fstream::in);
    int T;
    f >> T;
    for (int i = 1; i <= T; ++i) {
    Game g;
    g.read(f);
    cout << "Case #" << i << ": ";
    if (g.check('X')) {
	cout << "X won" << endl;
    } else if (g.check('O')) {
	cout << "O won" << endl;
    } else if (g.dots > 0) {
	cout << "Game has not completed" << endl;
    } else {
	cout << "Draw" << endl;
    }
    }
    return 0;

}
