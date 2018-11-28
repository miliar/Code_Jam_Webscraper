#include<iostream>
#include<cstdio>
#include<cassert>
using namespace std;
char a[4][4];
bool isRowComp(int row, char ch) {
    for (int i = 0; i < 4; i++) {
        if (a[row][i] == ch || a[row][i] == 'T') continue;
        else return false;
    }
    return true;
}
bool isColComp(int col, char ch) {
    for (int i = 0; i < 4; i++) {
        if(a[i][col] == ch || a[i][col] == 'T') continue;
        else return false;
    }
    return true;
}
bool isDiagComp(char ch) {
    bool isComp = true;
    for (int i = 0;i < 4;i++) {
        if (a[i][i] == ch || a[i][i] == 'T') continue;
        else { isComp = false; break; }
    }
    if (isComp) return isComp;
    for (int i = 0; i < 4; i++) {
        if (a[3-i][i] == ch || a[3-i][i] == 'T') continue;
        else return false;
    }
    return true;
}
int main() {
    int tc;
    scanf("%d ", &tc);
    for(int i = 0; i<tc; i++) {
        int ans=0; 
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++) a[j][k]=getchar();
            getchar();
        }
        if (!ans) {
            for(int j=0;j<4;j++) {
                if (isRowComp(j,'X') || isColComp(j,'X')) ans = 1;
                if (isRowComp(j,'O') || isColComp(j,'O')) ans = 2;
                if (ans) break;
            }
            if (!ans) {
                if (isDiagComp('X')) ans = 1;
                else if(isDiagComp('O')) ans = 2;
            }
            if (!ans) {
                for (int j=0;j<4;j++) for(int k=0;k<4;k++) if (a[j][k] == '.') { ans = 3; break;}
            }
        }
        switch(ans) {
            case 0:
                printf ("Case #%d: Draw\n", i + 1);
                break;
            case 1:
                printf ("Case #%d: X won\n", i + 1);
                break;
            case 2:
                printf ("Case #%d: O won\n", i+1);
                break;
            case 3:
                printf("Case #%d: Game has not completed\n", i+1);
                break;
            default:
                assert(2>3);
                break;
        }
        getchar();
    }
    return 0;
}
