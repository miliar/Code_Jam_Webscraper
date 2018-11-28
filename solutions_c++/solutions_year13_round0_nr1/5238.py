#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;


string check_game(vector<string> x)
{
    //ROWS
    for (size_t i = 0; i < 4; ++i)
    {
        size_t nX = 0, nO = 0, nT = 0;
        for (int j = 0; j < 4; ++j)
        {
            switch(x[i][j])
            {
            case 'X':
            {
                ++nX;
            }
                break;
            case 'O':
            {
                ++nO;
            }
                break;
            case 'T':
            {
                ++nT;
            }
                break;
            case '.':
            {
            }
                break;
            default:
                throw exception();
            }
        }
        if (nX + nT == 4)
        {
            return "X won";
        }
        else if (nO + nT == 4)
        {
            return "O won";
        }
    }
    //COLUMNS
    for (size_t i = 0; i < 4; ++i)
    {
        size_t nX = 0, nO = 0, nT = 0;
        for (int j = 0; j < 4; ++j)
        {
            switch(x[j][i])
            {
            case 'X':
            {
                ++nX;
            }
                break;
            case 'O':
            {
                ++nO;
            }
                break;
            case 'T':
            {
                ++nT;
            }
                break;
            case '.':
            {
            }
                break;
            default:
                throw exception();
            }
        }
        if (nX + nT == 4)
        {
            return "X won";
        }
        else if (nO + nT == 4)
        {
            return "O won";
        }
    }
    //DIAGONAL 1
    {
        size_t nX = 0, nO = 0, nT = 0;
        for (int j = 0; j < 4; ++j)
        {
            switch(x[j][j])
            {
            case 'X':
            {
                ++nX;
            }
                break;
            case 'O':
            {
                ++nO;
            }
                break;
            case 'T':
            {
                ++nT;
            }
                break;
            case '.':
            {
            }
                break;
            default:
                throw exception();
            }
        }
        if (nX + nT == 4)
        {
            return "X won";
        }
        else if (nO + nT == 4)
        {
            return "O won";
        }
    }
    //DIAGONAL 2
    {
        size_t nX = 0, nO = 0, nT = 0;
        for (int j = 0; j < 4; ++j)
        {
            switch(x[j][4 - 1 - j])
            {
            case 'X':
            {
                ++nX;
            }
                break;
            case 'O':
            {
                ++nO;
            }
                break;
            case 'T':
            {
                ++nT;
            }
                break;
            case '.':
            {
            }
                break;
            default:
                throw exception();
            }
        }
        if (nX + nT == 4)
        {
            return "X won";
        }
        else if (nO + nT == 4)
        {
            return "O won";
        }
    }
    bool IsDraw = true;
    for(int i = 0; i < 4; ++i)
    {
        IsDraw &= (x[i].end() == find(x[i].begin(), x[i].end(), '.'));
    }
    return IsDraw ? "Draw" : "Game has not completed";
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt", ios_base::out | ios_base::trunc);
    size_t T;
    in >> T;

    for (size_t i = 0; i < T; ++i)
    {
        vector<string> game(4);
        for(vector<string>::iterator j = game.begin(); j != game.end(); ++j)
        {
            in >> *j;
        }
        out << "Case #" << i + 1 << ": " << check_game(game) << "\n";
    }
    return 0;
}

