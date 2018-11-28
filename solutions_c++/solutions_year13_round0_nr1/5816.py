#include <iostream>
#include <cstdio>

using namespace std;

char board[10][10];
bool fin;
bool owin, xwin;

bool check(char ch)
{
    for(int i = 1; i <= 4; i++) {
        int cnt = 0;
        for(int j = 1; j <= 4; j++) {
            if(board[i][j] == ch || board[i][j] == 'T')
                cnt++;
        }
        if(cnt >= 4) return true;
    }
    for(int i = 1; i <= 4; i++) {
        int cnt = 0;
        for(int j = 1; j <= 4; j++) {
            if(board[j][i] == ch || board[j][i] == 'T')
                cnt++;
        }
        if(cnt >= 4) return true;
    }
    int cnt = 0;
    for(int i = 1, j = 1; i <= 4; i++, j++) {
        if(board[i][j] == ch || board[i][j] == 'T')
            cnt++;
    }
    if(cnt >= 4) return true;
    cnt = 0;
    for(int i = 1, j = 4; i <= 4; i++, j--) {
        if(board[i][j] == ch || board[i][j] == 'T')
            cnt++;
    }
    if(cnt >= 4) return true;
    return false;
}

int main()
{
    int t;
    scanf("%d", &t);
    freopen("a.out", "w", stdout);
    for(int i = 1; i <= t; i++) {
        bool fin = true;
        getchar();
        for(int j = 1; j <= 4; j++) {
            scanf("%s", board[j] + 1);
            for(int k = 1; k <= 4; k++) {
                if(board[j][k] == '.') fin = false;
            }
            getchar();
        }
        owin = false, xwin = false;
        owin = check('O');
        xwin = check('X');
        printf("Case #%d: ", i);
        if(owin) puts("O won");
        else if(xwin) puts("X won");
        else if(fin) puts("Draw");
        else puts("Game has not completed");
    }
        
    return 0;
}

