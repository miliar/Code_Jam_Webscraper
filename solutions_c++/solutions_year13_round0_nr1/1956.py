// First.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        bool full_field = true;
        bool x_win = false, o_win = false;
        vector <vector <char> > field (4, vector <char> (4));
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                cin >> field [j][k];
                if (field [j][k] == '.')
                    full_field = false;
            }
        }
        for (int j = 0; j < 4; ++j)
        {
            bool x = true;
            bool o = true;
            for (int k = 0; k < 4; ++k)
            {
                if ((field [j][k] == 'X') || (field [j][k] == '.'))
                    o = false;
                if ((field [j][k] == 'O') || (field [j][k] == '.'))
                    x = false;
            }
            if (x)
                x_win = x;
            if (o)
                o_win = o;
        }
        for (int k = 0; k < 4; ++k)
        {
            bool x = true;
            bool o = true;
            for (int j = 0; j < 4; ++j)
            {
                if ((field [j][k] == 'X') || (field [j][k] == '.'))
                    o = false;
                if ((field [j][k] == 'O') || (field [j][k] == '.'))
                    x = false;
            }
            if (x)
                x_win = x;
            if (o)
                o_win = o;
        }
        bool x = true;
        bool o = true;
        for (int j = 0; j < 4; ++j)
        {
            if ((field [j][j] == 'X') || (field [j][j] == '.'))
                o = false;
            if ((field [j][j] == 'O') || (field [j][j] == '.'))
                x = false;
        }
        if (x)
            x_win = x;
        if (o)
            o_win = o;
        x = true;
        o = true;
        for (int j = 0; j < 4; ++j)
        {
            if ((field [j][3 - j] == 'X') || (field [j][3 - j] == '.'))
                o = false;
            if ((field [j][3 - j] == 'O') || (field [j][3 - j] == '.'))
                x = false;
        }
        if (x)
            x_win = x;
        if (o)
            o_win = o;
        cout << "Case #" << i + 1 << ": ";
        if (x_win)
        {
            cout << "X won" << endl;
        }
        else if (o_win)
        {
            cout << "O won" << endl;
        }
        else if (full_field)
        {
            cout << "Draw" << endl;
        }
        else
        {
            cout << "Game has not completed" << endl;
        }
    }
	return 0;
}

