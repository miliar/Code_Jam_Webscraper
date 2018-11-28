#include <iostream>
#include <fstream>

using namespace std;

char board[4][4];
bool draw;
int solve();

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    int answer;
    fin >> T;
    for (int i=0;i<T;i++)
    {
        draw=true;
        for (int k=0;k<4;k++)
            for (int m=0;m<4;m++)
                fin >> board[k][m];
        answer=solve();
        if (answer==1) fout << "Case #" << i+1 << ": X won" << endl;
        else if (answer==2) fout << "Case #" << i+1 << ": O won" << endl;
        else if (answer==0 && draw) fout << "Case #" << i+1 << ": Draw" << endl;
        else fout << "Case #" << i+1 << ": Game has not completed" << endl;
    }
}

int solve()
{
    int column,row;
    for (int i=0;i<4;i++)
    {
        column=0;
        row=0;
        for (int j=0;j<4;j++)
        {
            row+=board[i][j];
            column+=board[j][i];
            if (board[i][j]=='.') draw=false;
        }
        if (column==348 || column==352) return 1;
        if (column==316 || column==321) return 2;
        if (row==348 || row==352) return 1;
        if (row==316 || row==321) return 2;
    }
    int diagonal=0;
    diagonal=board[0][0]+board[1][1]+board[2][2]+board[3][3];
    if (diagonal==348 || diagonal==352) return 1;
    if (diagonal==316 || diagonal==321) return 2;
    diagonal=board[0][3]+board[1][2]+board[2][1]+board[3][0];
    if (diagonal==348 || diagonal==352) return 1;
    if (diagonal==316 || diagonal==321) return 2;
    return 0;
}
