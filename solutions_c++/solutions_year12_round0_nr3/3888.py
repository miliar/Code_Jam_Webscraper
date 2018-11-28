#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<set>
using namespace std;
char str[50];
int hash[2100000];
int main() {
    int T;
    scanf ( "%d", &T );
    for ( int t = 1; t <= T;++t ) {
        int A, B;
        memset ( hash, 0, sizeof ( hash ) );
        scanf ( "%d%d", &A, &B );
        int ans = 0;
        for ( int i = A;i <= B;++i ) {
            int k = sprintf ( str, "%d", i );
            sprintf ( str + k, "%d", i );
            //printf ( "%s\n", str );
            for ( int j = k - 1;j > 0;--j ) {
                if ( str[j] == '0' ) continue;
                str[j+k] = 0;
                int p;
                sscanf ( str + j, "%d", &p );
                if ( p <= B && p > i && hash[p] != i ) {
                    //printf ( "%d - %d: ", hash[p], i );
                    hash[p] = i;
                    //printf ( "(%d, %d)\n", i, p );
                    ++ans;
                }
            }
        }
        printf ( "Case #%d: ", t );
        printf ( "%d\n", ans );
    }
    return 0;
}