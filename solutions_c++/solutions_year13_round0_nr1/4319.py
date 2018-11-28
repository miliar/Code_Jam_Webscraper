#include <cstdio>
#include <iostream>
using namespace std;

bool full(char a[][5]) {
    for ( int i=0;i<4;i++ ) {
        for ( int j=0;j<4;j++ ) {
            if ( a[i][j]=='.' )
                return true;
        }
    }
    return false;
}

bool judge(char a[][5],char c) {
    int i,j;
    for ( i=0;i<4;i++ ) {
        j = 0;
        while ( (j<4) && ( (a[i][j]==c) || (a[i][j]=='T') ) ) {
            j++;
        }
        if ( j>=4 ) return true;
    }
    for ( i=0;i<4;i++ ) {
        j = 0;
        while ( (j<4) && ( (a[j][i]==c) || (a[j][i]=='T') ) ) {
            j++;
        }
        if ( j>=4 ) return true;
    }
    i = 0;
    while ( (i<4) && ( (a[i][i]==c) || (a[i][i]=='T') ) ) {
        i++;
    }
    if ( i>=4 ) return true;
    i = 0;
    while ( (i<4) && ( (a[i][3-i]==c) || (a[i][3-i]=='T') ) ) {
        i++;
    }
    if ( i>=4 ) return true;
    return false;
}

int main() {
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    char a[4][5];
    scanf("%d",&T);
    gets(a[0]);
    for (int Ti=1;Ti<=T;Ti++) {
        for (int i=0;i<4;i++) {
            gets(a[i]);
        }
        printf("Case #%d: ",Ti);
        if ( judge(a,'X') ) {
            puts("X won");
        }
        else if ( judge(a,'O') ) {
            puts("O won");
        }
        else {
            bool flag = full(a);
            if ( flag ) {
                puts("Game has not completed");
            }
            else {
                puts("Draw");
            }
        }
        gets(a[0]);
    }
    return 0;
}
