#include<cstdio>

char board[10][10];
char pp[2] = {'X', 'O'};

bool check(int p){
    bool win = false;
    for(int i = 0; i < 4; i++){
        win = true;
        for(int j = 0; j < 4 && win; j++){
            if(board[i][j] != pp[p] && board[i][j] != 'T')
                win = false;
        }
        if(win) return true;
    }
    for(int i = 0; i < 4; i++){
        win = true;
        for(int j = 0; j < 4 && win; j++){
            if(board[j][i] != pp[p] && board[j][i] != 'T')
                win = false;
        }
        if(win) return true;
    }
    win = true;
    for(int i = 0; i < 4 && win; i++){
        if(board[i][i] != pp[p] && board[i][i] != 'T')
            win = false;
    }
    if(win) return true;
    win = true;
    for(int i = 0; i < 4 && win; i++){
        if(board[3-i][i] != pp[p] && board[3-i][i] != 'T')
            win = false;
    }
    return win;
}
bool full(void){
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(board[i][j] == '.') return false;
        }
    }
    return true;
}

int main(){
    freopen("paout.txt", "w", stdout);
    int T;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        for(int i = 0; i < 4; i++){
            scanf("%s", board[i]);
        }
        printf("Case #%d: ", ++cnt);
        if(check(0)) printf("X won\n");
        else if(check(1)) printf("O won\n");
        else if(full()) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
