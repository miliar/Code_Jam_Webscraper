#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;

string process(vector<string> &game)
{
    for (int i = 0; i < 4; i++)
    {
        // horizontal
        int oCount = 0;
        int xCount = 0;
        for (int j = 0; j < 4; j++)
        {
            if (game[i][j] == 'O' || game[i][j] == 'T')
                oCount++;
            if (game[i][j] == 'X' || game[i][j] == 'T')
                xCount++;
        }
        if (oCount == 4)
            return "O won";
        if (xCount == 4)
            return "X won";

        // vertical
        oCount = 0;
        xCount = 0;
        for (int j = 0; j < 4; j++)
        {
            if (game[j][i] == 'O' || game[j][i] == 'T')
                oCount++;
            if (game[j][i] == 'X' || game[j][i] == 'T')
                xCount++;
        }
        if (oCount == 4)
            return "O won";
        if (xCount == 4)
            return "X won";
    }

    int oCount = 0;
    int xCount = 0;
    for (int i = 0; i < 4; ++i)
    {
        if (game[i][i] == 'O' || game[i][i] == 'T')
            oCount++;
        if (game[i][i] == 'X' || game[i][i] == 'T')
            xCount++;
    }
    if (oCount == 4)
        return "O won";
    if (xCount == 4)
        return "X won";

    oCount = 0;
    xCount = 0;
    for (int i = 0; i < 4; ++i)
    {
        if (game[4 - i - 1][i] == 'O' || game[4 - i - 1][i] == 'T')
            oCount++;
        if (game[4 - i - 1][i] == 'X' || game[4 - i - 1][i] == 'T')
            xCount++;
    }
    if (oCount == 4)
        return "O won";
    if (xCount == 4)
        return "X won";

    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (game[i][j] == '.')
                return "Game has not completed";

    return "Draw";
}

int main(int argc, char **argv)
{
    ifstream ifs(argv[1]);

    int count;
    ifs >> count;

    for (int k = 0; k < count; k++)
    {
        vector<string> game(4);

        for (int i = 0; i < 4; i++)
        {
            game[i].resize(4);
            for (int j = 0; j < 4; j++)
            {
                ifs >> game[i][j];
            }
        }

        cout << "Case #" << k + 1 << ": " << process(game) << endl;
    }
    return 0;
}
