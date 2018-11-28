#include <iostream>
using namespace std;
string board[4];
int dx[] = {0, 1, 1, -1};
int dy[] = {1, 0, 1, +1};

void run() {
    int o3 = 0, x3 = 0, dot = 0;
    for(int i = 0; i < 4; i++) cin >> board[i];
    for(int k = 0; k < 4; k++)
        for(int i = 0; i < 4; i++) 
            for(int j = 0; j < 4; j++) {
                if(board[i][j] == '.') dot = 1;
                if(i + dx[k] * 3 >= 0 && i + dx[k] * 3 < 4 &&
                   j + dy[k] * 3 >= 0 && j + dy[k] * 3 < 4) {
                    int cnto = 0, cntx = 0, cntt = 0;
                    for(int l = 0; l < 4; l++) {
                        char c = board[i + dx[k] * l][j + dy[k] * l];
                        if(c == 'O') cnto++;
                        else if(c == 'X') cntx++;
                        else if(c == 'T') cntt++;
                    }
                    if(cnto == 4 || (cnto == 3 && cntt == 1)) o3 = 1;
                    if(cntx == 4 || (cntx == 3 && cntt == 1)) x3 = 1;
                }
            }
    if(o3) printf("O won\n");
    else if(x3) printf("X won\n");
    else if(dot) printf("Game has not completed\n");
    else printf("Draw\n");
}

int main() {
    int t;
    cin >> t;
    for(int i = 1 ; i <= t;i++) {
        printf("Case #%d: ", i);
        run();
    }
    return 0;
}
