#include <iostream>
#include <cstdio>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

int main()
{
    int t,d, c1, c2, c3,l = 1;
    char a[4][4];
    string s;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    while(t--) {

        d=-1;
        c1 = 0;
        c2 = 0;
        c3 = 0;
        for (int i = 0; i < 4; i++) {
            cin >> s;
            for (int j = 0; j < 4; j++) {
                a[i][j] = s[j];
                if (s[j] == '.')
                    d =1;
            }
        }
        // column check
        printf("Case #%d: ", l++);
        for (int j = 0; j < 4; j++){
            c1 = 0;
            c2 = 0;
            c3 = 0;
            for (int i = 0; i < 4; i++) {
                if (a[j][i] == 'O')
                    c1++;
                if (a[j][i] == 'X')
                    c2++;
                if (a[j][i] == 'T')
                    c3++;
            }
            if (c1 == 4 || (c1 == 3 && c3 == 1)) {
                printf("O won\n");
                d = 0;
                break;
            } else if (c2 == 4 || (c2 == 3 && c3 == 1)) {
                printf("X won\n");
               // printf("c2 = %d", c2);
                d = 0;
                break;
            }
        }
        if (d != 0) {
        for (int i = 0; i < 4; i++){
            c1 = 0;
            c2 = 0;
            c3 = 0;
            for (int j = 0; j < 4; j++) {
                if (a[j][i] == 'O')
                    c1++;
                if (a[j][i] == 'X')
                    c2++;
                if (a[j][i] == 'T')
                    c3++;
            }
            if (c1 == 4 || (c1 == 3 && c3 == 1)) {
                printf("O won\n");
                d = 0;
                break;
            } else if (c2 == 4 || (c2 == 3 && c3 == 1)) {
                printf("X won\n");
                d = 0;
                break;
            }
        }}
        if (d !=0 ) {
        c1 = 0;
        c2 = 0;
        c3 = 0;
        for (int i = 0; i < 4; i++) {
            int j = i;
                if (a[j][i] == 'O')
                    c1++;
                if (a[j][i] == 'X')
                    c2++;
                if (a[j][i] == 'T')
                    c3++;
        }
        if (c1 == 4 || (c1 == 3 && c3 == 1)) {
                printf("O won\n");
                d = 0;
                //break;
            } else if (c2 == 4 || (c2 == 3 && c3 == 1)) {
                printf("X won\n");
                d = 0;
               // break;
        }}
        if (d != 0) {
        c1 = 0;
        c2 = 0;
        c3 = 0;
        for (int i = 0; i < 4; i++) {
            int j = 4 - i - 1;
                if (a[j][i] == 'O')
                    c1++;
                if (a[j][i] == 'X')
                    c2++;
                if (a[j][i] == 'T')
                    c3++;
        }
        if (c1 == 4 || (c1 == 3 && c3 == 1)) {
                printf("O won\n");
                d = 0;
               // break;
            } else if (c2 == 4 || (c2 == 3 && c3 == 1)) {
                printf("X won\n");
                d = 0;
                //break;
        }}

        if (d == 1) {
            printf("Game has not completed\n");
        } else if (d == -1) {
            printf("Draw\n");
        }
    }

    return 0;
}
