#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<set>
using namespace std;
char str[50];
int hash[2100000];
int main() {
    freopen("/Users/martreenl/Downloads/C-large.in", "r", stdin);
    freopen("/Users/martreenl/Downloads/C-large.out", "w", stdout);
    
    int T;
    scanf ("%d", &T);
    for (int t=1;t <= T;++t) {
        int A, B;
        memset (hash, 0, sizeof ( hash ));
        scanf ("%d%d", &A, &B);
        int ans = 0;
        for (int i = A;i <= B;++i) {
            int k = sprintf ( str, "%d", i );
            sprintf ( str + k, "%d", i );
            for (int j = k - 1;j > 0;--j) {
                if ( str[j] == '0' ) continue;
                str[j+k] = 0;
                int p;
                sscanf ( str + j, "%d", &p );
                if ( p <= B && p > i && hash[p] != i ) {
                    hash[p] = i;
                    ++ans;
                }
            }
        }
        printf ("Case #%d: %d\n", t, ans);
    }
    return 0;
}