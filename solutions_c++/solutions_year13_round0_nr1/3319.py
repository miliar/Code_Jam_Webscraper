#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

int main()
{
    int T;
    int mat[4][4];
    string str[4];
    scanf("%d", &T);
    for(int cas=0; cas<T; cas++){
        memset(mat, 0, sizeof(mat));
        for(int i=0; i<4; i++)
            cin >> str[i];
        int draw = 0;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if( str[i][j] == 'X' )
                    mat[i][j] = 1;
                if( str[i][j] == 'O' )
                    mat[i][j] = 2;
                if( str[i][j] == 'T' )
                    mat[i][j] = 3;
                if( str[i][j] == '.' )
                    draw = 1;
            }
        }

        int Xwin[2][4], Owin[2][4];
        memset(Xwin, 1, sizeof(Xwin));
        memset(Owin, 2, sizeof(Owin));
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                Xwin[0][i] &= mat[i][j];
                Xwin[1][i] &= mat[j][i];
                Owin[0][i] &= mat[i][j];
                Owin[1][i] &= mat[j][i];
            }
        }
        int X=0, O=0, Xa=1, Xb=1, Oa=2, Ob=2;
        for(int i=0; i<4; i++){
            Xa = Xa & mat[i][i]; Xb = Xb & mat[i][3-i];
            Oa = Oa & mat[i][i]; Ob = Ob & mat[i][3-i];
            X = X | Xwin[0][i] | Xwin[1][i];
            O = O | Owin[0][i] | Owin[1][i];
        }
        X = X | Xa | Xb; O = O | Oa | Ob;
        printf("Case #%d: ", 1+cas);
        if(X)puts("X won");
        else if(O)puts("O won");
        else if(draw)puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}
