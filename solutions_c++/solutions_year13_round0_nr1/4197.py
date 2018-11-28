#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int T;
bool empty;
char chessboard[4][4];
void output(int who, int num);
void check(int num){
    int countX = 0, countO = 0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(chessboard[i][j]=='X'||chessboard[i][j]=='T') countX++;
            if(chessboard[i][j]=='O'||chessboard[i][j]=='T') countO++;
        }
        if(countX==4){
            output(1, num);
            return;
        }
        if(countO==4){
            output(2, num);
            return;
        }
        countX = 0;
        countO = 0;
        for(int j=0;j<4;j++){
            if(chessboard[j][i]=='X'||chessboard[j][i]=='T') countX++;
            if(chessboard[j][i]=='O'||chessboard[j][i]=='T') countO++;
        }
        if(countX==4){
            output(1, num);
            return;
        }
        if(countO==4){
            output(2, num);
            return;
        }
        countX = 0;
        countO = 0;
    }
    countX = 0;
    countO = 0;
    for(int i=0;i<4;i++){
        if(chessboard[i][i]=='X'||chessboard[i][i]=='T') countX++;
        if(chessboard[i][i]=='O'||chessboard[i][i]=='T') countO++;
    }
    if(countX==4){
        output(1, num);
        return;
    }
    if(countO==4){
        output(2, num);
        return;
    }
    countX = 0;
    countO = 0;
    if(chessboard[3][0]=='X'||chessboard[3][0]=='T') countX++;
    if(chessboard[3][0]=='O'||chessboard[3][0]=='T') countO++;
    if(chessboard[2][1]=='X'||chessboard[2][1]=='T') countX++;
    if(chessboard[2][1]=='O'||chessboard[2][1]=='T') countO++;
    if(chessboard[1][2]=='X'||chessboard[1][2]=='T') countX++;
    if(chessboard[1][2]=='O'||chessboard[1][2]=='T') countO++;
    if(chessboard[0][3]=='X'||chessboard[0][3]=='T') countX++;
    if(chessboard[0][3]=='O'||chessboard[0][3]=='T') countO++;
    if(countX==4){
        output(1, num);
        return;
    }
    if(countO==4){
        output(2, num);
        return;
    }
    output(0, num);
}

void output(int who, int num){
    if(who==1) cout<<"Case #"<<num<<": X won"<<endl;
    if(who==2) cout<<"Case #"<<num<<": O won"<<endl;
    if(who==0){
        if(empty){
            cout<<"Case #"<<num<<": Game has not completed"<<endl;
        }
        else{
            cout<<"Case #"<<num<<": Draw"<<endl;
        }
    }
}

int main(){
    cin>>T;
    for(int i=0;i<T;i++){
        empty = false;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin>>chessboard[j][k];
                if(chessboard[j][k]=='.') empty = true;
            }
        }
        check(i+1);
    }
}


