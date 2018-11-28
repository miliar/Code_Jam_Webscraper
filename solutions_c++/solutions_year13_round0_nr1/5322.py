#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

string readBoard(void)
{
    // vector<string> result;
    // string str;
    // for(size_t i = 0; i != 4; +i)
    // {
    //     cin >> str;
    //     result.push_back(str);
    // }

    string result;
    string str;
    for(size_t i = 0; i != 4; ++i)
    {
        //getline(cin, str);
        cin >> str;
        //cout << "read row: " << str << endl;
        result += str;
    }

    return result;
}

unsigned short int binarizeBoard(string board, char c)
{
    unsigned short int result(0);
    for(size_t i = 0; i != 16; ++i)
    {
        if(board[i] == c || board[i] == 'T')
        {
            result |= 1 << (15-i);
        }
    }
    return result;
}

bool isWon(unsigned short int board)
{
    static unsigned short int maps[10] = {
    0xF000,
    0x0F00,
    0x00F0,
    0x000F,
    0x8888,
    0x4444,
    0x2222,
    0x1111,
    0x8421,
    0x1248
    };

    //cout << hex << board << " : received as input" << endl;

    for(size_t i = 0; i != 10; ++i)
    {
        unsigned short int tmpBrd = board;
        if(((board & maps[i]) ^ maps[i]) == 0)
        {
            return true;
        }
    }

    return false;
}

bool gameFinished(string board)
{
    for(size_t i = 0; i != 16; ++i)
    {
        if(board[i] == '.')
        {
            return false;
        }
    }
    return true;
}

int main(int argc, char* args[])
{



    size_t T;
    cin >> T;
    bool xWon(false);
    bool oWon(false);

    for(size_t i = 0; i != T; ++i)
    {
        string curBoard = readBoard();
        //cout << "read board: " << curBoard << endl;
        unsigned short int binBoard = binarizeBoard(curBoard, 'X');
        xWon = isWon(binBoard);
        if(xWon)
        {
            cout << "Case #" << i+1 << ": X won" << endl;
            continue;
        }
        else
        {
            binBoard = binarizeBoard(curBoard, 'O');
            oWon = isWon(binBoard);
            if(oWon)
            {
                cout << "Case #" << i+1 << ": O won" << endl;
                continue;
            }
            else
            {
                if(gameFinished(curBoard))
                {
                    cout << "Case #" << i+1 << ": Draw" << endl;
                }
                else
                {
                    cout << "Case #" << i+1 << ": Game has not completed" << endl;
                }
            }
        }
    }




    return 0;
}