#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
using namespace std;
char board[4][4];
char check_win(){
    char winner=' ';
    int cnt=0;
    for (int j=0;j<4;j++){
        winner=' ';
        for (int k=0;k<4;k++){
            if (board[j][k]=='T' && k==3) return winner;
            else if (board[j][k]=='T' && k!=3) continue;
            else if (board[j][k]=='.') break;
            else if (board[j][k]!=winner && winner!=' ') break;
            else if (board[j][k]!=winner) winner=board[j][k];
            else if ((board[j][k]==winner || board[j][k]=='T')&& k==3) return winner;
        }
        winner=' ';
        for (int k=0;k<4;k++){
            if (board[k][j]=='T' && k==3) return winner;
            else if (board[k][j]=='T' && k!=3) continue;
            else if (board[k][j]=='.') break;
            else if (board[k][j]!=winner && winner!=' ') break;
            else if (board[k][j]!=winner) winner=board[k][j];
            else if ((board[k][j]==winner || board[k][j]=='T') && k==3) return winner;
        }
        winner=' ';
        if (j==0){
            for (int k=0;k<4;k++){
                if (board[k][k]=='T' && k==3) return winner;
                else if (board[k][k]=='T' && k!=3) continue;
                else if (board[k][k]=='.') break;
                else if (board[k][k]!=winner && winner!=' ') break;
                else if (board[k][k]!=winner) winner=board[k][k];
                else if ((board[k][k]==winner || board[k][k]=='T') && k==3) return winner;
            }
        }
        winner=' ';
        if (j==3){
            for (int k=0;k<4;k++){
                if (board[k][3-k]=='T' && k==3) return winner;
                else if (board[k][3-k]=='T' && k!=3) continue;
                else if (board[k][3-k]=='.') break;
                else if (board[k][3-k]!=winner && winner!=' ') break;
                else if (board[k][3-k]!=winner) winner=board[k][3-k];
                else if ((board[k][3-k]==winner || board[k][3-k]=='T') && k==3) return winner;
            }
        }
    }
    for (int i=0;i<4;i++) for (int j=0;j<4;j++) if (board[i][j]=='.') return 'I';
    return 'D';
}


int main(){
    int n;
    bool x,o;
    string msg;
    char res;

    scanf("%i\n",&n);
    for (int i=0;i<n;i++){
        for (int l=0;l<4;l++) scanf("%c%c%c%c\n",&board[l][0],&board[l][1],&board[l][2],&board[l][3]);
        res = check_win();
        switch (res){
            case 'D':
                msg="Draw";
                break;
            case 'I':
                msg="Game has not completed";
                break;
            case 'X':
                msg="X won";
                break;
            default:
                msg="O won";
        }
        printf("Case #%i: %s\n",(i+1),msg.c_str());

    }

    return 0;
}
