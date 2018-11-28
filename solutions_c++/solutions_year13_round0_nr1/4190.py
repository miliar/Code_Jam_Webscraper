#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
using namespace std;
char b[4][4];
char cn(){
    char wr=' ';
    int cnt=0;
    for (int j=0;j<4;j++){
        wr=' ';
        for (int k=0;k<4;k++){
            if (b[j][k]=='T' && k==3) return wr;
            else if (b[j][k]=='T' && k!=3) continue;
            else if (b[j][k]=='.') break;
            else if (b[j][k]!=wr && wr!=' ') break;
            else if (b[j][k]!=wr) wr=b[j][k];
            else if ((b[j][k]==wr || b[j][k]=='T')&& k==3) return wr;
        }
        wr=' ';
        for (int k=0;k<4;k++){
            if (b[k][j]=='T' && k==3) return wr;
            else if (b[k][j]=='T' && k!=3) continue;
            else if (b[k][j]=='.') break;
            else if (b[k][j]!=wr && wr!=' ') break;
            else if (b[k][j]!=wr) wr=b[k][j];
            else if ((b[k][j]==wr || b[k][j]=='T') && k==3) return wr;
        }
        wr=' ';
        if (j==0){
            for (int k=0;k<4;k++){
                if (b[k][k]=='T' && k==3) return wr;
                else if (b[k][k]=='T' && k!=3) continue;
                else if (b[k][k]=='.') break;
                else if (b[k][k]!=wr && wr!=' ') break;
                else if (b[k][k]!=wr) wr=b[k][k];
                else if ((b[k][k]==wr || b[k][k]=='T') && k==3) return wr;
            }
        }
        wr=' ';
        if (j==3){
            for (int k=0;k<4;k++){
                if (b[k][3-k]=='T' && k==3) return wr;
                else if (b[k][3-k]=='T' && k!=3) continue;
                else if (b[k][3-k]=='.') break;
                else if (b[k][3-k]!=wr && wr!=' ') break;
                else if (b[k][3-k]!=wr) wr=b[k][3-k];
                else if ((b[k][3-k]==wr || b[k][3-k]=='T') && k==3) return wr;
            }
        }
    }
    for (int i=0;i<4;i++) for (int j=0;j<4;j++) if (b[i][j]=='.') return 'I';
    return 'D';
}


int main(){
    int n;
    bool x,o;
    string msg;
    char res;

    scanf("%i\n",&n);
    for (int i=0;i<n;i++){
        for (int l=0;l<4;l++) scanf("%c%c%c%c\n",&b[l][0],&b[l][1],&b[l][2],&b[l][3]);
        res = cn();
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
