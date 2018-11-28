#include <iostream>
using namespace std;
const int oo = 1000000000; 
int dp[11][2048][11];
int p;
int a[2048];
int c[11][2048];
void inputint()
{
    int i, j;
    scanf ( "%d", &p );
//    printf ( "%d\n", 1<<p );
    for (i=0;i<1<<p;i++) {
        scanf ( "%d", &a[i] );
//        printf ( "%d ", a[i] );
        for (j=0;j<=a[i];j++)
            dp[0][i][j] = 0;
        for (j=a[i]+1;j<=p+1;j++)
            dp[0][i][j] = oo;
    }
//    printf ( "\n" );
    int len = 1<<(p-1);
    for (i=1;i<=p;i++) {
        for (j=0;j<len;j++) {
            scanf ( "%d", &c[i][j] );
//            printf ( "%d ", c[i][j] );
        }
//        printf ("\n" );
        len = len/2;
    }
}
void work()
{
    int len=1<<(p-1);
//    printf ("len =%d\n", len );
    int i, j, k;
    for (i=1;i<=p;i++) {
        for (j=0;j<len;j++) {
            for (k=p;k>=0;k--) {
//                printf ("j=%d, k=%d", j, k );
                dp[i][j][k] = oo;
                if (k<p) 
                    dp[i][j][k] = dp[i-1][j*2][k+1]+dp[i-1][j*2+1][k+1];
//                printf ( " %d", dp[i][j][k] );
                if (dp[i][j][k]>dp[i-1][j*2][k]+dp[i-1][j*2+1][k]+c[i][j]) {
                    dp[i][j][k] = dp[i-1][j*2][k]+dp[i-1][j*2+1][k]+c[i][j];
                }
//                printf ( " %d", dp[i][j][k] );
                if ((dp[i][j][k]>dp[i][j][k+1])&&(k<p)) {
                    dp[i][j][k] = dp[i][j][k+1];
                }
//                printf ( " %d", dp[i][j][k] );
                if (dp[i][j][k]>oo)
                    dp[i][j][k] = oo;
//                printf ( " %d\n", dp[i][j][k] );
            }
        }
        len = len/2;
//        printf ("\n" );
    }
    printf ( "%d\n", dp[p][0][0] );
}
int main()
{
    freopen ( "b-large.in", "r", stdin );
    freopen ( "b.out", "w", stdout );
    int ques;
    scanf ( "%d", &ques );
    for (int i=1;i<=ques;i++) {
        printf ( "Case #%d: ", i );
        inputint();
        work();
    }
}
