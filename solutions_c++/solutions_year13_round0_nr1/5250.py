#include <cstdio>
using namespace std;

static char board[4][10];
static bool hasD(char player, int sX, int sY, int dX, int dY) {
    for(int i=0; i<4; i++) {
        if(board[sX][sY] != player && board[sX][sY] != 'T')
            return false;
        sX += dX, sY += dY;
    }
    return true;
}
static bool has(char player) {
    for(int i=0; i<4; i++) {
        if(hasD(player, 0, i, 1, 0))
            return true;
        if(hasD(player, i, 0, 0, 1))
            return true;
    }
    if(hasD(player,0,0,1,1))
        return true;
    if(hasD(player,3,0,-1,1))
        return true;
    return false;
}

int main() {
    int _nT; scanf("%d", &_nT);
    for(int _T=0; _T<_nT; _T++) {
        for(int i=0; i<4; i++)
            scanf("%s", board[i]);

        bool hasX = has('X'), hasO = has('O');

        bool hasEmpty = false;
        for(int y=0; y<4; y++)
            for(int x=0; x<4; x++)
                if(board[y][x] == '.')
                    hasEmpty = 1;

        printf("Case #%d: ", _T+1);
        if(hasX && !hasO)
            printf("X won\n");
        else if(!hasX && hasO)
            printf("O won\n");
        else if((hasX && hasO) || !hasEmpty)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    return 0;
}

