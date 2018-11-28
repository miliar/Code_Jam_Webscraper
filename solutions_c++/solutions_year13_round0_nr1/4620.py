//
//  main.cpp
//  a
//
//  Created by Louis St-Amour on 2013-04-13.
//  Copyright (c) 2013 Louis St-Amour. All rights reserved.
//

#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

bool check(char (*board)[16], char player, int pos1, int pos2, int pos3, int pos4) {
    //printf("Checking %c%c%c%c (%d, %d, %d, %d) for %c\n", (*board)[pos1], (*board)[pos2], (*board)[pos3], (*board)[pos4], pos1, pos2, pos3, pos4, player);
    if (((*board)[pos1] == player || (*board)[pos1] == 'T') &&
        ((*board)[pos2] == player || (*board)[pos2] == 'T') &&
        ((*board)[pos3] == player || (*board)[pos3] == 'T') &&
        ((*board)[pos4] == player || (*board)[pos4] == 'T')) {
        return true;
    }
    return false;
}

int main(int argc, const char * argv[])
{
    int tc; scanf("%d\n", &tc);
    for(int tci = 0; tci < tc; tci++) {
        bool success = false;
        static char board[16];
        for(int bi = 0; bi < 4; bi++) {
            scanf("%4[XO.T]\n", &board[bi*4]);
            if(!success && check(&board,'X',bi*4+0,bi*4+1,bi*4+2,bi*4+3)) {
                printf("Case #%d: X won\n", tci+1);
                success = true;
            }
            if(!success && check(&board,'O',bi*4+0,bi*4+1,bi*4+2,bi*4+3)) {
                printf("Case #%d: O won\n", tci+1);
                success = true;
            }
        }
        //printf("%s\n",board);
        scanf("\n");
        if(!success) {
            for(int bi = 0; !success && bi < 4; bi++) {
                if(!success && check(&board,'X',bi+0,bi+4,bi+8,bi+12)) {
                    printf("Case #%d: X won\n", tci+1);
                    success = true;
                }
                if(!success && check(&board,'O',bi+0,bi+4,bi+8,bi+12)) {
                    printf("Case #%d: O won\n", tci+1);
                    success = true;
                }
            }
            if(!success && check(&board,'X',0,5,10,15)) {
                printf("Case #%d: X won\n", tci+1);
                success = true;
            }
            if(!success && check(&board,'O',0,5,10,15)) {
                printf("Case #%d: O won\n", tci+1);
                success = true;
            }
            if(!success && check(&board,'X',3,6,9,12)) {
                printf("Case #%d: X won\n", tci+1);
                success = true;
            }
            if(!success && check(&board,'O',3,6,9,12)) {
                printf("Case #%d: O won\n", tci+1);
                success = true;
            }
            if(!success) {
                for(int bi = 0; !success && bi < 16; bi++) {
                    if (board[bi] == '.') {
                        printf("Case #%d: Game has not completed\n", tci+1);
                        success = true;
                    }
                }
                if (!success) {
                    printf("Case #%d: Draw\n", tci+1);
                }
            }
        }
    }
    return 0;
}

//  0  1  2  3
//  4  5  6  7
//  8  9 10 11
// 12 13 14 15