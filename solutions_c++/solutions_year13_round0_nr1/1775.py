
#include <cstdlib>
#include <cstdio>

using namespace std;

char board[4][5];

bool isWins(char pl){
    int i, j;
    bool win = false;
    for(i = 0; i < 4; i++){
        for(j = 0; j < 4; j++){
            if(board[i][j] != pl && board[i][j] != 'T')
                break;
        }
        if(j == 4) win = true;
    }
    for(i = 0; i < 4; i++){
        for(j = 0; j < 4; j++){
            if(board[j][i] != pl && board[j][i] != 'T')
                break;
        }
        if(j == 4) win = true;
    }
    for(i = 0; i < 4; i++){
        if(board[i][i] != pl && board[i][i] != 'T')
            break;
    }
    if(i == 4) win = true;
    for(i = 0; i < 4; i++){
        if(board[i][3-i] != pl && board[i][3-i] != 'T')
            break;
    }
    if(i == 4) win = true;
    return win;
}

bool complete(){
    int i, j;
    for(i = 0; i < 4; i++){
        for(j = 0; j < 4; j++){
            if(board[i][j] == '.')
                return false;
        }
    }
    return true;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, i, kase = 0;
    scanf("%d", &t);
    while(t--){
        for(i = 0; i < 4; i++)
            scanf("%s", board[i]);
        printf("Case #%d: ", ++kase);
        if(isWins('X')) printf("X won\n");
        else if(isWins('O')) printf("O won\n");
        else if(complete())  printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
