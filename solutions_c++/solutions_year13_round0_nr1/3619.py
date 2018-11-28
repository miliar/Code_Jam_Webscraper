#include<stdio.h>
#include<stdlib.h>
char tab[5][5];
int main () {
    int ta;
    scanf("%d", &ta);
    for (int lo = 1; lo <= ta; lo++) {
        for (int c = 1; c <= 4; c++) {
            for (int g = 1; g <= 4; g++) {
                scanf(" %c", &tab[c][g]);
            }
        }
        int res = 0;
        for (int c = 1; c <= 4; c++) {
            int x = 0;
            int o = 0;
            bool t = false;
            for (int g = 1; g <= 4; g++) {
                if (tab[c][g] == 'X') x++;
                if (tab[c][g] == 'O') o++;
                if (tab[c][g] == 'T') t = true;
            }
            if (t && x == 3) res = 1;
            if (t && o == 3) res = -1;
            if (o == 4) res = -1;
            if (x == 4) res = 1;
        }
        for (int c = 1; c <= 4; c++) {
            int x = 0;
            int o = 0;
            bool t = false;
            for (int g = 1; g <= 4; g++) {
                if (tab[g][c] == 'X') x++;
                if (tab[g][c] == 'O') o++;
                if (tab[g][c] == 'T') t = true;
            }
            if (t && x == 3) res = 1;
            if (t && o == 3) res = -1;
            if (o == 4) res = -1;
            if (x == 4) res = 1;
        }
        int x = 0;
        int o = 0;
        bool t = false;
        for (int c = 1; c <= 4; c++) {
            if (tab[c][c] == 'X') x++;
            if (tab[c][c] == 'O') o++;
            if (tab[c][c] == 'T') t = true;
        }
        if (t && x == 3) res = 1;
        if (t && o == 3) res = -1;
        if (o == 4) res = -1;
        if (x == 4) res = 1;
        x = 0;
        o = 0;
        t = false;
        for (int c = 1; c <= 4; c++) {
            if (tab[c][5-c] == 'X') x++;
            if (tab[c][5-c] == 'O') o++;
            if (tab[c][5-c] == 'T') t = true;
            }
        if (t && x == 3) res = 1;
        if (t && o == 3) res = -1;
        if (o == 4) res = -1;
        if (x == 4) res = 1;
        printf("Case #%d: ", lo);
        if (res == 1) printf("X won\n");
        else if (res == -1) printf("O won\n");
        else {
            bool d = true;
            for (int c = 1; c <= 4; c++)
                for (int g = 1; g <= 4; g++)
                    if (tab[c][g] == '.')
                        d = false;
            if (d) printf("Draw\n");
            else printf("Game has not completed\n");
        }
    }
    return 0;
}
    
