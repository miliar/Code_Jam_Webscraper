#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("A-large.in");
    int t;
    input >> t;
    char board[4][4];
    bool x=false, o=false;
    ofstream output("A-large.out");
    bool draw;
    for (int i=0; i<t; i++)
    {
        draw=false;
        for (int z=0; z<4; z++)
        {
            for (int y=0; y<4; y++)
            {
                input >> board[z][y];
                if(board[z][y]=='.')
                draw=true;
            }
        }
                for (int z=0; z<4; z++)
        {
            for (int y=0; y<4; y++)
            {
                cout << board[z][y];
            }
            cout <<endl;
        }
        x=false;
        o=false;
        if ((board[0][0]== 'X' || board[0][0] == 'T')&&(board[0][1]== 'X' || board[0][1] == 'T')&&(board[0][2]== 'X' || board[0][2] == 'T')&&(board[0][3]== 'X' || board[0][3] == 'T'))
            x=true;
        else if ((board[1][0]== 'X' || board[1][0] == 'T')&&(board[1][1]== 'X' || board[1][1] == 'T')&&(board[1][2]== 'X' || board[1][2] == 'T')&&(board[1][3]== 'X' || board[1][3] == 'T'))
            x=true;
        else if ((board[2][0]== 'X' || board[2][0] == 'T')&&(board[2][1]== 'X' || board[2][1] == 'T')&&(board[2][2]== 'X' || board[2][2] == 'T')&&(board[2][3]== 'X' || board[2][3] == 'T'))
            x=true;
        else if ((board[3][0]== 'X' || board[3][0] == 'T')&&(board[3][1]== 'X' || board[3][1] == 'T')&&(board[3][2]== 'X' || board[3][2] == 'T')&&(board[3][3]== 'X' || board[3][3] == 'T'))
            x=true;
        else if ((board[0][0]== 'X' || board[0][0] == 'T')&&(board[1][0]== 'X' || board[1][0] == 'T')&&(board[2][0]== 'X' || board[2][0] == 'T')&&(board[3][0]== 'X' || board[3][0] == 'T'))
            x=true;
        else if ((board[0][1]== 'X' || board[0][1] == 'T')&&(board[1][1]== 'X' || board[1][1] == 'T')&&(board[2][1]== 'X' || board[2][1] == 'T')&&(board[3][1]== 'X' || board[3][1] == 'T'))
            x=true;
        else if ((board[0][2]== 'X' || board[0][2] == 'T')&&(board[1][2]== 'X' || board[1][2] == 'T')&&(board[2][2]== 'X' || board[2][2] == 'T')&&(board[3][2]== 'X' || board[3][2] == 'T'))
            x=true;
        else if ((board[0][3]== 'X' || board[0][3] == 'T')&&(board[1][3]== 'X' || board[1][3] == 'T')&&(board[2][3]== 'X' || board[2][3] == 'T')&&(board[3][3]== 'X' || board[3][3] == 'T'))
            x=true;
        else if ((board[0][0]== 'X' || board[0][0] == 'T')&&(board[1][1]== 'X' || board[1][1] == 'T')&&(board[2][2]== 'X' || board[2][2] == 'T')&&(board[3][3]== 'X' || board[3][3] == 'T'))
            x=true;
        else if ((board[0][3]== 'X' || board[0][3] == 'T')&&(board[1][2]== 'X' || board[1][2] == 'T')&&(board[2][1]== 'X' || board[2][1] == 'T')&&(board[3][0]== 'X' || board[3][0] == 'T'))
            x=true;
        if ((board[0][0]== 'O' || board[0][0] == 'T')&&(board[0][1]== 'O' || board[0][1] == 'T')&&(board[0][2]== 'O' || board[0][2] == 'T')&&(board[0][3]== 'O' || board[0][3] == 'T'))
            o=true;
        else if ((board[1][0]== 'O' || board[1][0] == 'T')&&(board[1][1]== 'O' || board[1][1] == 'T')&&(board[1][2]== 'O' || board[1][2] == 'T')&&(board[1][3]== 'O' || board[1][3] == 'T'))
            o=true;
        else if ((board[2][0]== 'O' || board[2][0] == 'T')&&(board[2][1]== 'O' || board[2][1] == 'T')&&(board[2][2]== 'O' || board[2][2] == 'T')&&(board[2][3]== 'O' || board[2][3] == 'T'))
            o=true;
        else if ((board[3][0]== 'O' || board[3][0] == 'T')&&(board[3][1]== 'O' || board[3][1] == 'T')&&(board[3][2]== 'O' || board[3][2] == 'T')&&(board[3][3]== 'O' || board[3][3] == 'T'))
            o=true;
        else if ((board[0][0]== 'O' || board[0][0] == 'T')&&(board[1][0]== 'O' || board[1][0] == 'T')&&(board[2][0]== 'O' || board[2][0] == 'T')&&(board[3][0]== 'O' || board[3][0] == 'T'))
            o=true;
        else if ((board[0][1]== 'O' || board[0][1] == 'T')&&(board[1][1]== 'O' || board[1][1] == 'T')&&(board[2][1]== 'O' || board[2][1] == 'T')&&(board[3][1]== 'O' || board[3][1] == 'T'))
            o=true;
        else if ((board[0][2]== 'O' || board[0][2] == 'T')&&(board[1][2]== 'O' || board[1][2] == 'T')&&(board[2][2]== 'O' || board[2][2] == 'T')&&(board[3][2]== 'O' || board[3][2] == 'T'))
            o=true;
        else if ((board[0][3]== 'O' || board[0][3] == 'T')&&(board[1][3]== 'O' || board[1][3] == 'T')&&(board[2][3]== 'O' || board[2][3] == 'T')&&(board[3][3]== 'O' || board[3][3] == 'T'))
            o=true;
        else if ((board[0][0]== 'O' || board[0][0] == 'T')&&(board[1][1]== 'O' || board[1][1] == 'T')&&(board[2][2]== 'O' || board[2][2] == 'T')&&(board[3][3]== 'O' || board[3][3] == 'T'))
            o=true;
        else if ((board[0][3]== 'O' || board[0][3] == 'T')&&(board[1][2]== 'O' || board[1][2] == 'T')&&(board[2][1]== 'O' || board[2][1] == 'T')&&(board[3][0]== 'O' || board[3][0] == 'T'))
            o=true;
        if (x==true)
        {
            output << "Case #" << i+1 << ": X won" << endl;
        }
        else if (o==true)
        {
            output << "Case #" << i+1 << ": O won" << endl;
        }
        else if (draw==false)
        {
            output << "Case #" << i+1 << ": Draw" << endl;
        }
        else if (x==false && o==false)
        {
            output << "Case #" << i+1 << ": Game has not completed" << endl;
        }
        cout << x <<  o << endl;
    }
    input.close();
    output.close();
    return 0;
}
