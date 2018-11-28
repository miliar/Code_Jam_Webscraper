#include <cstdio>
#include <cstring>

void f(int now,int type) {
    switch ( type ) {
        case 0:
            printf("Case #%d: X won\n",now);
            break;
        case 1:
            printf("Case #%d: O won\n",now);
            break;
        case 2:
            printf("Case #%d: Draw\n",now);
            break;
        case 3:
            printf("Case #%d: Game has not completed\n",now);
            break;
    }
}
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int z = 1 ; z <= tc; z++ ) {
        char a[11][11];
        bool ok = false;
        for ( int i = 0 ; i < 4 ; i++ ) 
            scanf("%s",a[i]);
        for ( int i = 0 ; i < 4 ; i++ ) {
            for ( int j = 0 ; j < 4; j++ ) {
                if ( a[i][j] == '.' ) ok = true;
                if ( (i == 0&&j == 0) ) {
                    int Ocnt =0,Xcnt = 0,Tcnt=0;
                    for ( int k = 0 ; k < 4; k++ ) {
                        if ( a[k][k] == 'O' ) Ocnt++;
                        else if ( a[k][k] == 'X' ) Xcnt++;
                        else if ( a[k][k] == 'T' ) Tcnt++;
                    }
                    if ( Ocnt == 4 || (Ocnt==3 && Tcnt==1) ) {
                        f(z,1);goto RET;}
                    else if ( Xcnt == 4 ||(Xcnt==3 && Tcnt==1) ){
                        f(z,0);goto RET;}
                }
                else if(i == 0&&j==3 ) {
                    int Ocnt =0,Xcnt = 0,Tcnt=0;
                    for ( int k = 0 ; k < 4; k++ ) {
                        if ( a[k][3-k] == 'O' ) Ocnt++;
                        else if ( a[k][3-k] == 'X' ) Xcnt++;
                        else if ( a[k][3-k] == 'T' ) Tcnt++;
                    }
                    if ( Ocnt == 4 || (Ocnt==3 && Tcnt==1) ){
                        f(z,1);goto RET;
                    }
                    else if ( Xcnt == 4 ||(Xcnt==3 && Tcnt==1) ){
                        f(z,0);goto RET;
                    }
                }
                int Ocnt =0,Xcnt = 0,Tcnt=0;
                for ( int k = 0 ; k < 4; k++ ) {
                    if ( a[i][k] == 'O' ) Ocnt++;
                    else if ( a[i][k] == 'X' ) Xcnt++;
                    else if ( a[i][k] == 'T' ) Tcnt++;
                }
                if ( Ocnt == 4 || (Ocnt==3 && Tcnt==1) ){
                    f(z,1);goto RET;}
                else if ( Xcnt == 4 ||(Xcnt==3 && Tcnt==1) ){
                    f(z,0);goto RET;}
                Ocnt =0,Xcnt = 0,Tcnt=0;
                for ( int k = 0 ; k < 4; k++ ) {
                    if ( a[k][j] == 'O' ) Ocnt++;
                    else if ( a[k][j] == 'X' ) Xcnt++;
                    else if ( a[k][j] == 'T' ) Tcnt++;
                }
                if ( Ocnt == 4 || (Ocnt==3 && Tcnt==1) ){
                    f(z,1);goto RET;}
                else if ( Xcnt == 4 ||(Xcnt==3 && Tcnt==1) ){
                    f(z,0);goto RET;}
            }
        }
        if ( ok ) f(z,3);
        else f(z,2);
RET:;
    }
    return 0;
}
