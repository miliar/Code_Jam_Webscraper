// Tic-Tac-Tomek
// Problem A for the Google Code Jam Qualifiers
// Solution by 64Mega

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct st_gamestate
{
    string board[4];
};

vector<st_gamestate> games;

void readinput(string fname)
{
    games.clear();

    ifstream in(fname);
    if(!in.is_open())
    {
        cout << "Error opening input!" << endl;
        abort();
    }

    int num = 0;
    in >> num;

    cout << "Reading " << num << " test cases..." << endl;

    for(int i = 0; i < num; i++)
    {
        st_gamestate t;
        for(int k = 0; k < 4; k+=1)
        {
            in >> t.board[k];
            cout << t.board[k];
            cout << endl;
        }
        cout << endl;
        //in.get();
        games.push_back(t);
    }

    in.close();
}

enum gamestates
{
    XWON,
    OWON,
    DRAW,
    PROG
};

int main(int argc, char** argv)
{
    readinput("input.txt");

    // Process

    vector<gamestates> states;
    for(int i = 0; i < games.size(); i++)
    {
        // Diagonal tests
        int x = 0, o = 0, d = 0;
        bool found = false;
        for(int j = 0; j < 4; j++)
        {
            if(games[i].board[j][j] == 'X')x++;
            if(games[i].board[j][j] == 'O')o++;
            if(games[i].board[j][j] == 'T'){o++;x++;}
            if(games[i].board[j][j] == '.'){d++;}
        }
        if(x == 4)
        {
            states.push_back(XWON);
            continue;
        }
        if(o == 4)
        {
            states.push_back(OWON);
            continue;
        }

        x = o = 0;

        for(int j = 0; j < 4; j++)
        {
            if(games[i].board[j][3-j] == 'X')x++;
            if(games[i].board[j][3-j] == 'O')o++;
            if(games[i].board[j][3-j] == 'T'){o++;x++;}
            if(games[i].board[j][3-j] == '.'){d++;}
        }
        if(x == 4)
        {
            states.push_back(XWON);
            continue;
        }
        if(o == 4)
        {
            states.push_back(OWON);
            continue;
        }
        x = o = 0;

        // Horizontal check
        for(int iy = 0; iy < 4; iy++)
        {
            x = o = 0;
            for(int ix = 0; ix < 4; ix++)
            {
                if(games[i].board[iy][ix] == 'X')x++;
                if(games[i].board[iy][ix] == 'O')o++;
                if(games[i].board[iy][ix] == 'T'){o++;x++;}
                if(games[i].board[iy][ix] == '.'){d++;}
            }
            if(x == 4)
            {
                states.push_back(XWON);
                found = true;
                break;
            }
            if(o == 4)
            {
                states.push_back(OWON);
                found = true;
                break;
            }

        }
        if(found)continue;
        x = o = 0;

        // Vertical Check
        for(int ix = 0; ix < 4; ix++)
        {
            x = o = 0;
            for(int iy = 0; iy < 4; iy++)
            {
                if(games[i].board[iy][ix] == 'X')x++;
                if(games[i].board[iy][ix] == 'O')o++;
                if(games[i].board[iy][ix] == 'T'){o++;x++;}
                if(games[i].board[iy][ix] == '.'){d++;}
            }

            if(x == 4)
            {
                states.push_back(XWON);
                found = true;
                break;
            }
            if(o == 4)
            {
                states.push_back(OWON);
                found = true;
                break;
            }

        }

        if(!found)
        {
            if(o != 4 && x != 4 && d == 0)
            {
                states.push_back(DRAW);
            }
            else
            {
                states.push_back(PROG);
            }
        }
    }

    ofstream out("output.txt");
    for(int i = 0; i < states.size(); i++)
    {
        out << "Case #" << i+1 << ": ";
        if(states[i] == XWON)out << "X won" << endl;
        if(states[i] == OWON)out << "O won" << endl;
        if(states[i] == DRAW)out << "Draw" << endl;
        if(states[i] == PROG)out << "Game has not completed" << endl;
    }
    out.close();

    return 0;
}
