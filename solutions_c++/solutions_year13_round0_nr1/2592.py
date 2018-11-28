#include <cstdio>

char map[4][4];

bool four(char x){
    int lcount = 0, rcount = 0;
    for(int i = 0; i < 4; i++){
        int count = 0;
        for(int j = 0; j < 4; j++){
            if(map[i][j] == x){
                count++;
            }else{
                break;
            }
        }
        if(count == 4)return 1;
        count = 0;
        for(int j = 0; j < 4; j++){
            if(map[j][i] == x){
                count++;
            }else{
                break;
            }
        }
        if(count == 4)return 1;
        if(map[i][i] == x)lcount++;
        if(map[i][3 - i] == x)rcount++;
    }
    if(lcount == 4 || rcount == 4)return 1;
    return false;
}

int judge(){
    bool done = true;
    int tr = -1, tc = -1;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(map[i][j] == '.'){
                done = false;
            }else if(map[i][j] == 'T'){
                tr = i;
                tc = j;
            }
        }
    }
    if(tr != -1) map[tr][tc] = 'X';
    if(four('X'))return 1;
    if(tr != -1) map[tr][tc] = 'O';
    if(four('O'))return 2;
    if(done)return 3;
    return 0;
}

int main(){
    char rs[4][100] = {"Game has not completed", "X won", "O won", "Draw"};
    int t;
    scanf("%d\n", &t);
    int ca = 1;
    while(t--){
        for(int i = 0; i < 4; i++){
            scanf("%s\n", map[i]);
        }
        scanf("\n");
        printf("Case #%d: %s\n", ca++, rs[judge()]);
    }
    return 0;
}