#include<cstdio>
#include<algorithm>
using namespace std;
int a[6][6],TT,mm;
char ch;
void won(int r) {
    if (r == 1) printf("X won\n");
    else printf("O won\n");
}
void ends(int r) {
    if (r) printf("Draw\n");
    else printf("Game has not completed\n");
}
void work() {
    for (int j,tl,i = 1; i <= 4; ++i) {
        for (tl = 3,j = 1; j <= 4; ++j) tl &= a[i][j];
        if (tl) {won(tl); return ;}
        for (tl = 3,j = 1; j <= 4; ++j) tl &= a[j][i];
        if (tl) {won(tl); return ;}
    }
    int i,tl;
    for (i = 1, tl = 3; i <= 4; ++i) tl &= a[i][i];
    if (tl) {won(tl); return ;}
    for (i = 1, tl = 3; i <= 4; ++i) tl &= a[5-i][i];
    if (tl) {won(tl); return;}
    tl = 1;
    for (i = 1; i <= 4; ++i)
        for (int j = 1; j <= 4; ++j) tl = tl && (a[i][j]);
    ends(tl);
}
void read_(char &ch) {
    for (ch = '\n'; (ch < 'A' || ch > 'Z') && ch != '.'; ch = getchar());
}
int main() {
    for (scanf("%d", &TT), mm = TT; TT; --TT) {
        printf("Case #%d: ", mm-TT+1);
        for (int i = 1; i <= 4; ++i) 
            for (int j = 1; j <= 4; ++j) {
                read_(ch);
                if (ch == 'X') a[i][j] = 1;
                else if (ch == 'O') a[i][j] = 2;
                else if (ch == 'T') a[i][j] = 3;
                else a[i][j] = 0;
            }
        work();
    }
    return 0;
}
