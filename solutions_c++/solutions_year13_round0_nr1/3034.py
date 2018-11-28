#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int T;
int xrows[5];
int trows[5];
int xcols[5];
int tcols[5];

int main() {
    char name[50];
    char a[50], b[50];
    scanf("%s", name);
    strcpy(a, name);   strcpy(b, name);
    strcat(a, ".in");  strcat(b, ".out");
    FILE *in=fopen(a, "r"), *out=fopen(b,"w");

    fscanf(in, "%d", &T);

    int r;
    int c;
    char x;
    bool over;
    int winner;
    char ldag, rdag;

    for(int i=1; i<=T; i++) {
        memset(xrows, 0, sizeof(xrows));
        memset(trows, 0, sizeof(trows));
        memset(xcols, 0, sizeof(xcols));
        memset(tcols, 0, sizeof(tcols));
        over = true;
        winner = 0;
        ldag = rdag = ' ';

        for(r=1; r<=4; r++) {
            for(c=1; c<=4; c++) {
                fscanf(in, " ");
                fscanf(in, "%c", &x);
                if(r == c && x != 'T') {
                    if(ldag == ' ') ldag = x;
                    else if(ldag != x) ldag = '-';
                }
                if(r + c == 5 && x != 'T') {
                    if(rdag == ' ') rdag = x;
                    else if(rdag != x) rdag = '-';
                }
                if(x == '.') {
                    over = false;
                    continue;
                }
                if(x != 'X') {
                    trows[r]++;
                    tcols[c]++;
                }
                if(x != 'O') {
                    xrows[r]++;
                    xcols[c]++;
                }
            }
        }

        for(r=1; r<=4; r++) {
//            cout << xrows[r] << " ";
//            cout << trows[r] << " ";
//            cout << xcols[r] << " ";
//            cout << tcols[r] << " ";
//            cout << endl;
            if(xrows[r] == 4) winner = 1;
            if(trows[r] == 4) winner = 2;
            if(xcols[r] == 4) winner = 1;
            if(tcols[r] == 4) winner = 2;
        }
//        cout << "winner: " << winner << endl;
//        cout << ldag << " " << rdag << endl;
//        cout << (ldag == 'O') << endl;

        if(winner == 1 || ldag == 'X' || rdag == 'X') {
            fprintf(out, "Case #%d: X won\n", i);
        }
        else if(winner == 2 || ldag == 'O' || rdag == 'O') {
            fprintf(out, "Case #%d: O won\n", i);
        }
        else if(winner == 0 && over) {
            fprintf(out, "Case #%d: Draw\n", i);
        }
        else if(winner == 0 && !over) {
                fprintf(out, "Case #%d: Game has not completed\n", i);
        }
    }

    return 0;
}
