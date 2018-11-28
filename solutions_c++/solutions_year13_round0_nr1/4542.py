#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int isX(const char &a, const char &b, const char &c, const char &d)
{
    if(((a == 'T') && (b == 'X') && (c == 'X') && (d == 'X')) ||
       ((a == 'X') && (b == 'T') && (c == 'X') && (d == 'X')) ||
       ((a == 'X') && (b == 'X') && (c == 'T') && (d == 'X')) ||
       ((a == 'X') && (b == 'X') && (c == 'X') && (d == 'T')) ||
       ((a == 'X') && (b == 'X') && (c == 'X') && (d == 'X'))) return 1;
    return 0;
}

int isO(const char &a, const char &b, const char &c, const char &d)
{
    if(((a == 'T') && (b == 'O') && (c == 'O') && (d == 'O')) ||
       ((a == 'O') && (b == 'T') && (c == 'O') && (d == 'O')) ||
       ((a == 'O') && (b == 'O') && (c == 'T') && (d == 'O')) ||
       ((a == 'O') && (b == 'O') && (c == 'O') && (d == 'T')) ||
       ((a == 'O') && (b == 'O') && (c == 'O') && (d == 'O'))) return 1;
    return 0;
}

int main(int argc, char* argv[])
{
    int T; cin >> T;

    for(int i = 0; i < T; ++i){
        char c[4][4];
        int isPoint = 0;
        for(int x = 0; x < 4; ++x){
            string s;
            cin >> s;
            for(int y = 0; y < 4; ++y){
                c[x][y] = s.c_str()[y];
                if(c[x][y] == '.') isPoint = 1;
                //printf("%c", c[x][y]);
            }
            //printf("\n\r");
        }
        //printf("\n\r");
        //rows
        for(int x = 0; x < 4; ++x){
            if(isX(c[x][0], c[x][1], c[x][2], c[x][3])){
                printf("Case #%d: X won", i+1);
                goto nextT;
            }
            if(isO(c[x][0], c[x][1], c[x][2], c[x][3])){
                printf("Case #%d: O won", i+1);
                goto nextT;
            }
        }
        //columns
        for(int y = 0; y < 4; ++y){
            if(isX(c[0][y], c[1][y], c[2][y], c[3][y])){
                printf("Case #%d: X won", i+1);
                goto nextT;
            }
            if(isO(c[0][y], c[1][y], c[2][y], c[3][y])){
                printf("Case #%d: O won", i+1);
                goto nextT;
            }
        }
        //main diagonal
        if(isX(c[0][0], c[1][1], c[2][2], c[3][3])){
            printf("Case #%d: X won", i+1);
            goto nextT;
        }
        if(isO(c[0][0], c[1][1], c[2][2], c[3][3])){
            printf("Case #%d: O won", i+1);
            goto nextT;
        }
        //second diagonal
        if(isX(c[0][3], c[1][2], c[2][1], c[3][0])){
            printf("Case #%d: X won", i+1);
            goto nextT;
        }
        if(isO(c[0][3], c[1][2], c[2][1], c[3][0])){
            printf("Case #%d: O won", i+1);
            goto nextT;
        }

        if(isPoint == 0) printf("Case #%d: Draw", i+1);
        else printf("Case #%d: Game has not completed", i+1);
nextT:
        cout << endl;
    }
	return 0;
}

