#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <iostream>

using namespace std;

char extract_winner(const std::string& line)
{
    if (line.size() == count_if(line.begin(), line.end(),
                                [](char c) {return c == 'X' || c == 'T';}))
    {
        return 'X';
    }
    else if (line.size() == count_if(line.begin(), line.end(),
                                     [](char c) {return c == 'O' || c == 'T';}))
    {
        return 'O';
    }
    else
    {
        return '-';
    }
}

int main()
{
    int ntests;

    cin >> ntests;

    for (int test = 0; test < ntests; ++test) {
        vector<string> field;
        bool full = true;

        for (int ind = 0; ind < 4; ++ind) {
            string row;
            cin >> row;
            field.push_back(row);

            if (row.find('.') != string::npos) {
                full = false;
            }
        }

////////////////////////////////////////
        char winner = '-';
        vector<string> lines;
        string diag1;
        string diag2;

        for (int i = 0; i < 4; ++i) {
            string row;
            string col;

            diag1.push_back(field[i][i]);
            diag2.push_back(field[i][3 - i]);
            
            for (int j = 0; j < 4; ++j) {
                row.push_back(field[i][j]);
                col.push_back(field[j][i]);
            }

            lines.push_back(row);
            lines.push_back(col);
        }

        lines.push_back(diag1);
        lines.push_back(diag2);

        for (int i = 0; i < lines.size(); ++i) {
            winner = extract_winner(lines[i]);

            if (winner != '-')
                break;
        }

///////////////////////////////
        string message;

        if (winner != '-') {
            message.push_back(winner);
            message += " won";
        } else if (full == false) {
            message = "Game has not completed";
        } else {
            message = "Draw";
        }


        printf("Case #%d: %s\n", test + 1, message.c_str());
        getline(cin, message); // skip empty line after each test
    }


    return 0;
}
