#include <stdio.h>

char grid[10][10];

void Solve(int caseNo){
    bool dot = false;
    int i, j;
    int cntX, cntO, cntT;
    
    for (i=0; i<4; i++){
        cntX = cntO = cntT = 0;
        for (j=0; j<4; j++){
            switch(grid[i][j]){
                case 'X':
                    cntX++; break;
                case 'O':
                    cntO++; break;
                case 'T':
                    cntT++; break;
                case '.':
                    dot=true; break;
            }
        }
        if (cntX+cntT==4){
            printf("Case #%d: X won\n", caseNo);
            return;
        }
        else if (cntO+cntT==4){
            printf("Case #%d: O won\n", caseNo);
            return;
        }
    }
    
    for (j=0; j<4; j++){
        cntX = cntO = cntT = 0;
        for (i=0; i<4; i++){
            switch(grid[i][j]){
                case 'X':   cntX++; break;
                case 'O':   cntO++; break;
                case 'T':   cntT++; break;
                //default :   break;
            }
        }
        if (cntX+cntT==4){
            printf("Case #%d: X won\n", caseNo);
            return;
        }
        else if (cntO+cntT==4){
            printf("Case #%d: O won\n", caseNo);
            return;
        }
    }
    
    cntX = cntO = cntT = 0;
    for (i=0; i<4; i++){
        switch(grid[i][i]){
            case 'X':   cntX++; break;
            case 'O':   cntO++; break;
            case 'T':   cntT++; break;
            //default :   break;
        }
    }
    if (cntX+cntT==4){
            printf("Case #%d: X won\n", caseNo);
            return;
        }
    else if (cntO+cntT==4){
        printf("Case #%d: O won\n", caseNo);
        return;
    }
    
    cntX = cntO = cntT = 0;
    for (i=0; i<4; i++){
        switch(grid[i][3-i]){
            case 'X':   cntX++; break;
            case 'O':   cntO++; break;
            case 'T':   cntT++; break;
            //default :   break;
        }
    }
    if (cntX+cntT==4){
            printf("Case #%d: X won\n", caseNo);
            return;
        }
    else if (cntO+cntT==4){
        printf("Case #%d: O won\n", caseNo);
        return;
    }
    
    if (dot) printf("Case #%d: Game has not completed\n", caseNo);
    else     printf("Case #%d: Draw\n", caseNo);
}

void PrintGrid(){
    printf("Grid:\n");
    for (int i=0; i<4; i++)
        printf("%s\n", grid[i]);
}

int main(){
    int T, t, i, j;
    scanf("%d", &T);
    fgetc(stdin);
    for (t=1; t<=T; t++){
        for (i=0; i<4; i++)
            scanf("%s", grid[i]);
        fgetc(stdin);
        Solve(t);
    }
    
    return 0;
}

