#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

bool checkForO(char);
bool checkForX(char);
bool checkForDot(char);

namespace TTTT
{
enum Enum {NONE = 0, X_WON, O_WON, DRAW, N_OVER};
}


TTTT::Enum checkOneTestCase(char board[4][4])
{
    bool found_a_dot = false;

    bool x_win_cross1 = true;
    bool x_win_cross2 = true;
    bool o_win_cross1 = true;
    bool o_win_cross2 = true;

    for (int i=0; i<4; i++)
    {
        x_win_cross1 &= checkForX(board[i][i]);
        x_win_cross2 &= checkForX(board[(3-i)][i]);

        o_win_cross1 &= checkForO(board[i][i]);
        o_win_cross2 &= checkForO(board[(3-i)][i]);

        bool x_win_down = true;
        bool x_win_horizontal = true;

        bool o_win_down = true;
        bool o_win_horizontal = true;

        for (int j=0; j<4; j++)
        {
            x_win_down &= checkForX(board[i][j]);
            o_win_down &= checkForO(board[i][j]);

            x_win_horizontal&= checkForX(board[j][i]);
            o_win_horizontal&= checkForO(board[j][i]);

            if(!found_a_dot)
            {
                found_a_dot = checkForDot(board[i][j]);
            }
        }

        if (x_win_down || x_win_horizontal)
        {
            return TTTT::X_WON;
        }
        else if (o_win_down || o_win_horizontal)
        {
            return TTTT::O_WON;
        }
    }

    if (x_win_cross1 || x_win_cross2)
    {
        return TTTT::X_WON;
    }
    if (o_win_cross1 || o_win_cross2)
    {
        return TTTT::O_WON;
    }

    // No winner found
    if (found_a_dot)
    {
        return TTTT::N_OVER;
    }
    else
    {
        return TTTT::DRAW;
    }
}



bool checkForO(char in)
{
    if (in == 'O' || in == 'T')
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool checkForX(char in)
{
    if (in == 'X' || in == 'T')
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool checkForDot(char in)
{
    if (in == '.')
    {
        return true;
    }
    else
    {
        return false;
    }
}



int main(int argc, char *argv[])
{
    string input_path, output_path;

    if (argc == 1)
    {
        cout << "WARNING: NO INPUT AND OUTPUT FILE GIVEN" << endl;
    }
    else if (argc == 2)
    {
        cout << "WARNING: ONLY ONE PATH GIVEN. BUT WHICH?!" << endl;
    }
    else if (argc == 3)
    {
        // read FILENAMES
        input_path = argv[1];
        output_path = argv[2];
        cout << "IN: " << input_path << ", OUT: " << output_path << endl;
    }


    // Prepare output file
    fstream f_out;
    f_out.open(output_path.c_str(), ios::out|ios::app);
    f_out << flush;


    int num_test_cases;

    fstream f;
    f.open(input_path.c_str(), ios::in);

    // Get number of test cases
    string first_line;
    getline(f, first_line);
    num_test_cases = atoi(first_line.c_str());

    cout << "----------------------------------------" << endl;
    cout << "num_test_cases = " << num_test_cases << endl;
    cout << "----------------------------------------" << endl;


    for (int i=0; i<num_test_cases; i++)
    {
        char board[4][4];

        for (int j=0; j<4; j++)
        {
            string products_line;

            getline(f, products_line);
            stringstream linestream(products_line);

            for (int k=0; k<4; k++)
            {
                char value;
                linestream >> value;
                board[j][k] = value;
            }
        }

        string empty_line;
        getline(f, empty_line);

        TTTT::Enum result = checkOneTestCase(board);

        switch (result)
        {
        case TTTT::X_WON :
            cout << "Case #" << (i+1) << ": X won" << endl;
            f_out << "Case #" << (i+1) << ": X won" << endl;
            break;
        case TTTT::O_WON :
            cout << "Case #" << (i+1) << ": O won" << endl;
            f_out << "Case #" << (i+1) << ": O won" << endl;
            break;
        case TTTT::DRAW :
            cout << "Case #" << (i+1) << ": Draw" << endl;
            f_out << "Case #" << (i+1) << ": Draw" << endl;
            break;
        case TTTT::N_OVER :
            cout << "Case #" << (i+1) << ": Game has not completed" << endl;
            f_out << "Case #" << (i+1) << ": Game has not completed" << endl;
            break;
        }
    }
    cout << "----------------------------------------" << endl;

    f_out.close();
}









