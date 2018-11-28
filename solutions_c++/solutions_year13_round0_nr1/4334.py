//
//  main.cpp
//  TestCppCode
//

#include <iostream>
#include <list>
#include <map>
using namespace std;

int main() {
    char a[4][4];
    int tc; scanf("%d\n", &tc);
    for (int test = 1; test <= tc; test++) {
//        printf("\nThis is case# (%d/%d)\n\n", test, tc);
        for (int r = 0; r < 4; r++) {
            scanf("%c%c%c%c\n", &a[r][0], &a[r][1], &a[r][2], &a[r][3]);
        }
//        printf("----- start ------\n");
//        for (int r = 0; r < 4; r++) {
//            printf("%c%c%c%c\n", a[r][0], a[r][1], a[r][2], a[r][3]);
//        }
//        printf("------ end -------\n");

        bool winnerDecided = false;
        int totalBlanks = 0;
        int X = 0, O = 0, T = 0, B = 0;
        
        // row scan
        for (int r = 0; r < 4; r++) {
            X = 0, O = 0, T = 0, B = 0;
            for (int c = 0; c < 4; c++) {
                switch (a[r][c]) {
                    case 'X':
                        X++; break;
                    case 'O':
                        O++; break;
                    case 'T':
                        T++; break;
                    default:
                        B++; totalBlanks++; break;
                }
            }
            if (B == 0) {
                if (X == 0) {
                    printf("Case #%d: O won\n", test);
                    winnerDecided = true;
                    break;
                } else if (O == 0) {
                    printf("Case #%d: X won\n", test);
                    winnerDecided = true;
                    break;
                }
            }
        }
        if (winnerDecided) continue;

        // column scan
        for (int c = 0; c < 4; c++) {
            X = 0, O = 0, T = 0, B = 0;
            for (int r = 0; r < 4; r++) {
                switch (a[r][c]) {
                    case 'X':
                        X++; break;
                    case 'O':
                        O++; break;
                    case 'T':
                        T++; break;
                    default:
                        B++; break;
                }
            }
            if (B == 0) {
                if (X == 0) {
                    printf("Case #%d: O won\n", test);
                    winnerDecided = true;
                    break;
                } else if (O == 0) {
                    printf("Case #%d: X won\n", test);
                    winnerDecided = true;
                    break;
                }
            }
        }
        if (winnerDecided) continue;

        // left diagonal scan
        X = 0, O = 0, T = 0, B = 0;
        for (int r=0,c=0; r<4; r++,c++) {
            switch (a[r][c]) {
                case 'X':
                    X++; break;
                case 'O':
                    O++; break;
                case 'T':
                    T++; break;
                default:
                    B++; break;
            }
        }
        if (B == 0) {
            if (X == 0) {
                printf("Case #%d: O won\n", test);
                winnerDecided = true;
            } else if (O == 0) {
                printf("Case #%d: X won\n", test);
                winnerDecided = true;
            }
        }
        if (winnerDecided) continue;

        // right diagonal scan
        X = 0, O = 0, T = 0, B = 0;
        for (int r=0,c=3; r<4; r++,c--) {
            switch (a[r][c]) {
                case 'X':
                    X++; break;
                case 'O':
                    O++; break;
                case 'T':
                    T++; break;
                default:
                    B++; break;
            }
        }
        if (B == 0) {
            if (X == 0) {
                printf("Case #%d: O won\n", test);
                winnerDecided = true;
            } else if (O == 0) {
                printf("Case #%d: X won\n", test);
                winnerDecided = true;
            }
        }
        if (winnerDecided) continue;

        // if result is not decided yet, the game is either draw or unfinished.
        if (!totalBlanks) {
            printf("Case #%d: Draw\n", test);
        } else {
            printf("Case #%d: Game has not completed\n", test);
        }
    }
}