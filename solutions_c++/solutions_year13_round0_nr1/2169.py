#include <cstdlib>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream in("tictac.in");
    ofstream out("tictac.out");
    int N;
    in>>N;
    char board[4][4];
    for(int i=0;i<N;i++) {
        bool full=true;
        for(int i2=0;i2<4;i2++)
            for(int i3=0;i3<4;i3++) {
                in>>board[i2][i3];
                if(board[i2][i3]=='.')
                    full=false;
            }
        bool xWon=false;
        bool oWon=false;
        //Check for X
        for(int i2=0;i2<4 && !xWon;i2++) {
            bool rowGood=true;
            for(int i3=0;i3<4 && rowGood;i3++)
                if(board[i2][i3]!='X' && board[i2][i3]!='T')
                    rowGood=false;
            if(rowGood)
                xWon=true;
        }
        for(int i2=0;i2<4 && !xWon;i2++) {
            bool rowGood=true;
            for(int i3=0;i3<4 && rowGood;i3++)
                if(board[i3][i2]!='X' && board[i3][i2]!='T')
                    rowGood=false;
            if(rowGood)
                xWon=true;
        }
        if(!xWon && (board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T')) {
            xWon=true;
        }
        if(!xWon && (board[3][0]=='X' || board[3][0]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[0][3]=='X' || board[0][3]=='T')) {
            xWon=true;
        }
        for(int i2=0;i2<4 && !oWon;i2++) {
            bool rowGood=true;
            for(int i3=0;i3<4 && rowGood;i3++)
                if(board[i2][i3]!='O' && board[i2][i3]!='T')
                    rowGood=false;
            if(rowGood)
                oWon=true;
        }
        for(int i2=0;i2<4 && !oWon;i2++) {
            bool rowGood=true;
            for(int i3=0;i3<4 && rowGood;i3++)
                if(board[i3][i2]!='O' && board[i3][i2]!='T')
                    rowGood=false;
            if(rowGood)
                oWon=true;
        }
        if(!oWon && (board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T')) {
            oWon=true;
        }
        if(!oWon && (board[3][0]=='O' || board[3][0]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[0][3]=='O' || board[0][3]=='T')) {
            oWon=true;
        }
        if(xWon)
            out<<"Case #"<<(i+1)<<": X won\n";
        else if(oWon)
            out<<"Case #"<<(i+1)<<": O won\n";
        else if(full)
            out<<"Case #"<<(i+1)<<": Draw\n";
        else
            out<<"Case #"<<(i+1)<<": Game has not completed\n";
    }
    out.close();
    return 0;
}

