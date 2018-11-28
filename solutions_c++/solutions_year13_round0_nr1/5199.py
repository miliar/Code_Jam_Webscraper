#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isvalid(char a, char p)
{
    return (a == p || a == 'T');
}

bool checkplayer(const vector<string>& b, char p)
{
    bool flag = false;
    // check row
    for (int i = 0; i < 4; i++)
    {
        bool isgood = true;
        for (int j = 0; j < 4; j++)
            isgood = isgood & isvalid(b[i][j], p);
        if (isgood)
            flag = true;
    }
    
    // check column
    for (int i = 0; i < 4; i++)
    {
        bool isgood = true;
        for (int j = 0; j < 4; j++)
            isgood = isgood & isvalid(b[j][i], p);
        if (isgood)
            flag = true;
    }
    
    // check diagonal    
    bool isgood = true;
    for (int i = 0; i < 4; i++)
        isgood = isgood & isvalid(b[i][i], p);
    if (isgood)
        flag = true;

    isgood = true;
    for (int i = 0; i < 4; i++)
        isgood = isgood & isvalid(b[i][3-i], p);
    if (isgood)
        flag = true;

    return flag;
}

bool checkdot(const vector<string> & b)
{
    for (int i = 0; i < 4; i++)
        for (int j =0 ;j < 4; j++)
            if (b[i][j] == '.')
                return false;

    return true;
}

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        vector<string> input;
        for (int k = 0; k < 4; k++)
        {
            string line;
            cin >> line;
            input.push_back(line);
        }

        // check
        bool isfinish = checkdot(input);
        bool xwon = checkplayer(input, 'X');
        bool owon = checkplayer(input, 'O');

        cout << "Case #" << i+1 << ": ";

        if (xwon && !owon)
            cout << "X won" << endl;
        else if (!xwon && owon)
            cout << "O won" << endl;
        else if (xwon && owon)
            cout << "Draw" << endl;
        else
        {
            if (isfinish)
                cout << "Draw" << endl;
            else
                cout << "Game has not completed" << endl;
        }

    }

    return 0;
}

