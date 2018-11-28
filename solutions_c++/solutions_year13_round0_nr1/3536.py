#include <iostream>
#include <fstream>
using namespace std;

string message(int n)
//-1 = X wins
//0 = draw
//1 = O wins
//2 = not complete
{
    if(n == -1) return "X won";
    if(n == 1) return "O won";
    if(n == 0) return "Draw";
    if(n == 2) return "Game has not completed";
}

string processboard(string board[])
{
    int xcount, ocount;
    bool full = true;
    for(int row=0; row < 4; row++)
    {
        xcount = 0;
        ocount = 0;
        for(int col=0; col < 4; col++)
        {
            if(board[row][col] == 'X') xcount++;
            else if(board[row][col] == 'O') ocount++;
            else if(board[row][col] == 'T')
            {
                xcount++;
                ocount++;
            }
            else full = false;
        }
        if((xcount == 4) || (ocount == 4))
        {
            if(xcount == 4) return message(-1);
            return message(1);
        }
    }
    for(int col=0; col < 4; col++)
    {
        xcount = 0;
        ocount = 0;
        for(int row=0; row < 4; row++)
        {
            if(board[row][col] == 'X') xcount++;
            if(board[row][col] == 'O') ocount++;
            if(board[row][col] == 'T')
            {
                xcount++;
                ocount++;
            }
            if((xcount == 4) || (ocount == 4))
            {
                if(xcount == 4) return message(-1);
                return message(1);
            }
        }
    }
    for(int diag=0; diag < 2; diag++)
    {
        xcount = 0;
        ocount = 0;
        for(int rowcol = 0; rowcol < 4; rowcol++)
        {
            if(board[rowcol][3*(1 - diag) + (2*diag - 1)*rowcol] == 'X') xcount++;
            if(board[rowcol][3*(1 - diag) + (2*diag - 1)*rowcol] == 'O') ocount++;
            if(board[rowcol][3*(1 - diag) + (2*diag - 1)*rowcol] == 'T')
            {
                xcount++;
                ocount++;
            }
            if((xcount == 4) || (ocount == 4))
            {
                if(xcount == 4) return message(-1);
                return message(1);
            }
        }
    }
    if(full) return message(0);
    return message(2);
}

int main()
{
    ifstream tictac("A-large.in");
    ofstream tictacres("tictaclargeres.txt");

    string board[4];
    int numboards;
    tictac >> numboards;
    tictac.ignore(256,'\n');

    for(int i=1; i <= numboards; i++)
    {
        for(int row=0; row < 4; row++)
        {
            getline(tictac,board[row]);
        }
        tictacres << "Case #" << i << ": " << processboard(board);
        if(i != numboards) tictacres << endl;
        getline(tictac,board[0]);
    }
    return 0;
}
