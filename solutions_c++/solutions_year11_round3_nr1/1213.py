#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <vector>

enum color {
    WHITE,
    BLUE,
    REDupleft,
    REDupright,
    REDdownleft,
    REDdownright
};

using namespace std;
int main ()
{
    int num_games, game_num, r, c;
    string result;
    vector< vector< color > > picture;

    cin >> num_games;

    for (game_num = 1; game_num <= num_games; game_num++ )
    { 
        cin >> r >> c;

        string s;
        char cc;
        for ( int row = 0; row < r; ++row) {
            picture.push_back(vector<color>());
            cin >> s;
            for ( int col = 0; col < c; ++col) {
                cc = s[col];
                switch (cc) {
                    case '\n':
                        --col;
                        break;
                    case '.':
                        picture[row].push_back(WHITE);
                        break;
                    case '#':
                        picture[row].push_back(BLUE);
                        break;
                }
            }
        }

        for ( int row = 0; row < r; ++row) {
            for ( int col = 0; col < c; ++col) {
            }
        }
        

        // map is populated

        bool possible = true;
        for ( int row = 0; possible && (row < r); ++row) {
            for (int col = 0; possible && col < c; ++col) {
                if ( picture[row][col] == BLUE ) {
                    if ( row == r - 1 ||
                        col == c - 1 ||
                        picture[row + 1][col] != BLUE ||
                        picture[row][col+1] != BLUE ||
                        picture[row+1][col+1] != BLUE) {
                        possible = false;
                    } else {
                        picture[row][col] = REDupleft;
                        picture[row+1][col] = REDdownleft;
                        picture[row][col+1] = REDupright;
                        picture[row+1][col+1] = REDdownright;
                    }
                }
            }
        }

        result += "Case #";
        stringstream cvert;
        cvert.flush();
        cvert << game_num;
        result += cvert.str();
        result += ":\n";

        if (!possible) {
            result += "Impossible\n";
        } else {
            for ( int row = 0; row < r; ++row) {
                for ( int col = 0; col < c; ++col) {
                    switch (picture[row][col]) {
                        case WHITE:
                            result += ".";
                            break;
                        case REDupleft:
                        case REDdownright:
                            result += "/";
                            break;
                        case REDupright:
                        case REDdownleft:
                            result += "\\";
                            break;
                        default:
                            result += "?";
                            break;
                    }
                }
                result += "\n";
            }
        }

        for (int row = 0; row < r; ++row){
            picture[row].clear();
        }
        picture.clear();
    }


    cout << result;
    return 0;
}


