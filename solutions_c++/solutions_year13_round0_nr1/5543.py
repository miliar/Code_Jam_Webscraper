#include <cstdio>

char field[5][5];
int t;

char abs(char x){
    if(x >= 0)
        return x;
    return -x;
}
char sgn(char x){
    if(x > 0)
        return 1;
    if(x < 0)
        return -1;
    return 0;
}
char q(char x){
    if(x == 1)
        return 'X';
    if(x == -1)
        return 'O';
    return 0;
}
int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++){
        gets(field[0]);
        for(int j = 0; j < 4; j ++)
            gets(field[j]);
        char cols[4] = {0}, rows[4] = {0}, diags[2] = {0}, tx = -1, ty = -1;
        bool fin = true;
        for(int x = 0; x < 4; x ++)
            for(int y = 0; y < 4; y ++){
                char inc = (field[x][y] == 'X') ? 1 : ( (field[x][y] == 'O') ? -1 : 0);
                rows[x] += inc;
                cols[y] += inc;
                if(x == y)
                    diags[0] += inc;
                if(x + y == 3)
                    diags[1] += inc;
                if(field[x][y] == 'T'){
                    tx = x;
                    ty = y;
                }
                if(field[x][y] == '.')
                    fin = false;
            }
        //gets(field[0]);
        printf("Case #%d: ", i);
        char st = 0;
        for(int j = 0; j < 4; j ++){
            if((abs(cols[j]) == 4) || ((abs(cols[j]) == 3) && (ty == j))){
                st = sgn(cols[j]);
                break;
            }
            if((abs(rows[j]) == 4) || ((abs(rows[j]) == 3) && (tx == j))){
                st = sgn(rows[j]);
                break;
            }
        }
        if(st != 0){
            printf("%c won\n", q(st));
            continue;
        }
        if((abs(diags[0]) == 4) || ((abs(diags[0]) == 3) && (tx == ty))){
            st = sgn(diags[0]);
        }
        if(st != 0){
            printf("%c won\n", q(st));
            continue;
        }
        if((abs(diags[1]) == 4) || ((abs(diags[1]) == 3) && (tx + ty == 3))){
            st = sgn(diags[1]);
        }
        if(st != 0){
            printf("%c won\n", q(st));
            continue;
        }
        if(fin)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    fflush(stdout);
}
