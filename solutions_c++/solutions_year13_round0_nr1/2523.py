#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <set>

using namespace std;

enum Tile
{
    EMPTY,
    X,
    O,
    T
};

struct Board
{
    vector<vector<Tile> > state;
};


int main(int argc, char const *argv[])
{
    ifstream ifs(argv[1]);
    ofstream ofs("result");
    int ncases;
    ifs >> ncases;

    vector<int> result;

    for (int casenum = 1; casenum < ncases+1; ++casenum)
    {
        Board current_board;
        string temp;
        for (int i = 0; i < 4; i++)
        {
            ifs >> temp;
            vector<Tile> current_row;
            for (int j = 0; j  < temp.length(); j++)
            {
                if (temp[j] == '.')
                {
                    current_row.push_back(EMPTY);
                } else if (temp[j] == 'X')
                {
                    current_row.push_back(X);
                } else if (temp[j] == 'T')
                {
                    current_row.push_back(T);
                } else if (temp[j] = 'O')
                {
                    current_row.push_back(O);
                }
            }
            current_board.state.push_back(current_row);
        }


        Board boardX(current_board);
        Board boardO(current_board);

        for (int y = 0; y < current_board.state.size(); y++)
        {
            for (int x = 0; x < current_board.state[y].size(); x++)
            {
                if (current_board.state[y][x] == T)
                {
                    boardX.state[y][x] = X;
                    boardO.state[y][x] = O;
                }
            }
        }

        Tile winner = T;

        for (int i = 0; i < 4; i++)
        {
            if (boardX.state[i][0] == boardX.state[i][1] &&
                boardX.state[i][1] == boardX.state[i][2] &&
                boardX.state[i][2] == boardX.state[i][3])
            {
                winner = boardX.state[i][0];
                break;
            }
        }

        for (int i = 0; i  < 4 && winner != T; i++)
        {
            if (boardX.state[0][i] == boardX.state[1][i] &&
                boardX.state[1][i] == boardX.state[2][i] &&
                boardX.state[2][i] == boardX.state[3][i])
            {
                winner = boardX.state[0][i];
                break;
            }
        }

        if (winner == T &&
            boardX.state[0][0] != EMPTY &&
            boardX.state[0][0] == boardX.state[1][1] &&
            boardX.state[1][1] == boardX.state[2][2] &&
            boardX.state[2][2] == boardX.state[3][3])
        {
            winner = boardX.state[0][0];
        }

        if (winner == T &&
            boardX.state[0][3] != EMPTY &&
            boardX.state[0][3] == boardX.state[1][2] &&
            boardX.state[1][2] == boardX.state[2][1] &&
            boardX.state[2][1] == boardX.state[3][0])
        {
            winner = boardX.state[0][3];
        }

        if (winner == T)
        {
            // check for O
            for (int i = 0; i < 4; i++)
            {
                if (boardO.state[i][0] == boardO.state[i][1] &&
                    boardO.state[i][1] == boardO.state[i][2] &&
                    boardO.state[i][2] == boardO.state[i][3])
                {
                    winner = boardO.state[i][0];
                    break;
                }
            }

            for (int i = 0; i  < 4 && winner == T; i++)
            {
                if (boardO.state[0][i] == boardO.state[1][i] &&
                    boardO.state[1][i] == boardO.state[2][i] &&
                    boardO.state[2][i] == boardO.state[3][i])
                {
                    winner = boardO.state[0][i];
                    break;
                }
            }

            if (winner == T &&
                boardO.state[0][0] != EMPTY &&
                boardO.state[0][0] == boardO.state[1][1] &&
                boardO.state[1][1] == boardO.state[2][2] &&
                boardO.state[2][2] == boardO.state[3][3])
            {

                cout << "BLA" << endl;
                winner = boardO.state[0][0];
            }

            if (winner == T &&
                boardO.state[0][3] != EMPTY &&
                boardO.state[0][3] == boardO.state[1][2] &&
                boardO.state[1][2] == boardO.state[2][1] &&
                boardO.state[2][1] == boardO.state[3][0])
            {
                cout << "BLA" << endl;
                winner = boardO.state[0][3];
            }
        }

        ofs << "Case #" << casenum << ": ";
        // determine winner
        if (winner == X)
        {
            cout << "X won" << endl;
            ofs << "X won" << endl;
        } else if (winner == O)
        {
            cout << "O won" << endl;
            ofs << "O won" << endl;
        } else {
            // check for full board
            int empty_count = 0;
            for (int y = 0; y < current_board.state.size(); y++)
            {
                for (int x = 0; x < current_board.state[y].size(); x++)
                {
                    if (current_board.state[y][x] == EMPTY) empty_count++;
                }
            }
            if (empty_count > 0)
            {
                cout << "Game has not completed" << endl;
                ofs << "Game has not completed" << endl;
            } else {
                cout << "Draw" << endl;
                ofs << "Draw" << endl;
            }
        }
    }

    return 0;
}
