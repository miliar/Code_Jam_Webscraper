#include <iostream>
#define SIZE 4

using namespace std;

void process(char bod, int &row)
{

            switch (bod)
            {
                case 'O':
                    if (row == 1)
                        row = -2;
                    if (row == 0)
                        row = 2;
                    break;
                case 'X':
                    if (row == 2)
                        row = -2;
                    if (row == 0)
                        row = 1;
                    break;
                case '.':
                    row = -2;
            }
}

void real_main(int no)
{
    cout<<"Case #"<<no<<": ";
    char board[SIZE][SIZE];
    for (int i=0; i<SIZE; i++)
        for (int j=0; j<SIZE; j++)
            cin>>board[i][j];
    bool ALL_OCC = true;

    for (int i=0; i<SIZE;i++) // By Row
    {
        int row = 0;
        for (int j=0; j<SIZE;j++)
        {
            if (board[i][j]=='.') ALL_OCC = false;
            process(board[i][j], row);
        }
        if (row ==1)
            cout<<"X won"<<endl;
        if (row ==2)
            cout<<"O won"<<endl;
        if (row>0) return;
    }


    for (int i=0; i<SIZE;i++) // By column
    {
        int row = 0;
        for (int j=0; j<SIZE;j++)
            process(board[j][i], row);
        if (row ==1)
            cout<<"X won"<<endl;
        if (row ==2)
            cout<<"O won"<<endl;
        if (row>0) return;
    }

    int diag = 0, diag2 = 0;
    for (int i = 0; i<SIZE;i++)
    {
        process(board[i][i], diag);
        process(board[i][SIZE-i-1], diag2);
    }
    if (diag == 1 || diag2 == 1 )
    {
        cout<<"X won"<<endl;
        return;
    }
    if (diag == 2 || diag2 == 2)
    {
        cout<<"O won"<<endl;
        return;
    }
        

    if (ALL_OCC)
        cout<<"Draw"<<endl;
    else
        cout<<"Game has not completed"<<endl;
}

int main()
{
    int T; cin>>T;
    for (int i=0;i<T;i++)
        real_main(i+1);
    return 0;
}
