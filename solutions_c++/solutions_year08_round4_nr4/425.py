#include<stdio.h>
#include<string.h>
#include<math.h>
#include<memory.h>
#include<algorithm>
using namespace std;
int k;
int p[32];
char s[100001], t[100001];

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int N;
    scanf("%d", &N);
    for ( int nc = 1 ; nc <= N ; ++nc ) {
        scanf("%d", &k);
        scanf("%s", s);
        for ( int i = 0 ; i < k ; ++i ) {
            p[i] = i;
        }
        int len = strlen(s);
        int cnt = 0;
        int res = len;
        memset(t, 0, sizeof(t));
        do {
            for ( int i = 0 ; i < len ; i+=k) {
                for ( int j = 0 ; j < k ; ++j ) {
                    t[i+j] = s[i+p[j]];
                }
            }
            t[len] = 0;
            int tmp = 0;
            for ( int i = 0 ; i < len ; ) {
                int j = i+1;
                ++tmp;
                while ( j < len && t[j] == t[i] ) ++j;
                i = j;
            }
            if ( tmp < res ) {
                res = tmp;
            }
          //  printf("t[%s] len%d %d %d\n", t, len, tmp, res);
            ++cnt;
        } while ( next_permutation(p, p+k) );
        
        
        // output
        printf("Case #%d: %d\n", nc, res);
        // ......
        //printf("%d %d %d\n", N, M, A);
        
    }
    return 0;
}

