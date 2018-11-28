#include <cstdio>

char win(char a, char b, char c, char d) {
    if(a=='T') a=b;
    if(b=='T') b=a;
    if(c=='T') c=a;
    if(d=='T') d=a;
    if(a==b && b==c && c==d) return a;
    return 0;
}

int main() {
    int n; scanf("%d", &n);
    for(int i=0; i<n; i++) {
        char b[5][5];
        for(int j=0; j<4; j++) {
            for(int k=0; k<4; k++) {
                scanf(" %c", &b[j][k]);
            }
        }
        int res=-1;
        char x;
        for(int j=0; j<4; j++) {
            // check horizontals
            x = win(b[j][0], b[j][1], b[j][2], b[j][3]);
            if(x=='O' || x=='X') {
                printf("Case #%d: %c won\n", i+1, x);
                goto next;
            }
            // check verticals
            x = win(b[0][j], b[1][j], b[2][j], b[3][j]);
            if(x=='O' || x=='X') {
                printf("Case #%d: %c won\n", i+1, x);
                goto next;
            }
        }
        // check diagonals
        x = win(b[0][0], b[1][1], b[2][2], b[3][3]);
        if(x=='O' || x=='X') {
            printf("Case #%d: %c won\n", i+1, x);
            goto next;
        }
        x = win(b[0][3], b[1][2], b[2][1], b[3][0]);
        if(x=='O' || x=='X') {
            printf("Case #%d: %c won\n", i+1, x);
            goto next;
        }
        for(int j=0; j<4; j++) for(int k=0; k<4; k++) {
            if(b[j][k]=='.') {
                printf("Case #%d: Game has not completed\n", i+1);
                goto next;
            }
        }
        printf("Case #%d: Draw\n", i+1);
        next:;
    }
}
