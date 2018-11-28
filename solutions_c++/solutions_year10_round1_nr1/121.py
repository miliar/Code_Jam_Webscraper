#include <iostream>
using namespace std;
const int MaxN = 60;
char map[MaxN][MaxN];
int n, w, quesnum, rflag, bflag;
int u[MaxN][MaxN], l[MaxN][MaxN], ld[MaxN][MaxN], rd[MaxN][MaxN];
void inputint()
{
    scanf ( "%d %d", &n, &w );
    for (int i=0;i<n;i++) {
        scanf ( "%s\n", map[i] );
    }
}
void work()
{
    int i,j,k;
    for (i=0;i<n;i++) {
        k=n-1;
        for (j=n-1;j>=0;j--) {
            if (map[i][j]!='.') {
                map[i][k] = map[i][j];
                k--;
            }
        }
        for (;k>=0;k--) {
            map[i][k]='.';
        }
    }
    rflag = 0;
    bflag = 0;
    for (i=0;i<n;i++) {
        for (j=0;j<n;j++) {
            if (map[i][j]=='.') {
                u[i][j]=0;
                l[i][j]=0;
                ld[i][j]=0;
                rd[i][j]=0;
            }
            else {
                u[i][j]=1;
                if (i>0) {
                    if (map[i-1][j]==map[i][j]) {
                        u[i][j] = u[i-1][j]+1;
                    }
                }
                l[i][j]=1;
                if (j>0) {
                    if (map[i][j-1]==map[i][j]) {
                        l[i][j] = l[i][j-1]+1;
                    }
                }
                ld[i][j]=1;
                if ((i>0)&&(j>0)) {
                    if (map[i-1][j-1]==map[i][j]) {
                        ld[i][j] = ld[i-1][j-1]+1;
                    }
                }
                rd[i][j]=1;
                if ((i>0)&&(j<n-1)) {
                    if (map[i-1][j+1]==map[i][j]) {
                        rd[i][j] = rd[i-1][j+1]+1;
                    }
                }
            }
            if ((l[i][j]==w)||(u[i][j]==w)||(ld[i][j]==w)||(rd[i][j]==w)) {
                if (map[i][j]=='R') 
                    rflag = 1;
                if (map[i][j]=='B')
                    bflag = 1;
                if (rflag && bflag)
                    return;
            }
        }
    }
}
void outputint() 
{
    if (rflag&&bflag) {
        printf ( "Both\n" );
    }
    else if (rflag) {
        printf ( "Red\n" );
    }
    else if (bflag) {
        printf ( "Blue\n" );
    }
    else {
        printf ( "Neither\n" );
    }
}
int main()
{
    freopen ( "rotate.in", "r", stdin );
    freopen ( "rotate.out", "w", stdout );
    scanf ( "%d", &quesnum );
    for (int i=1;i<=quesnum;i++) {
        printf ( "Case #%d: ", i );
        inputint();
        work();
        outputint();
    }
    return 0;
}
