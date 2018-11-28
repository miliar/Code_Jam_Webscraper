#include<algorithm>
#include<cstring>

using namespace std;

int main(void) {
    int N;
    scanf("%d", &N);

    for( int i=0; i<N; i++ ) {
        int k;
        char s[1001];
        scanf("%d\n%s", &k, s);

        int slen = strlen(s);

        int best = -1;

        int p[k];
        for( int j=0; j<k; j++ ) {
            p[j] = j;
        }

        do {
            char prev = '@';
            int act_res = 0;
            for( int j=0; j<slen; j++ ) {
                char act = s[ j-(j%k) + p[j%k] ];
                if( prev != act ) {
                    act_res ++;
                }
                prev = act;
            }
            if( act_res < best || best==-1 ) {
                best = act_res;
            }
        } while( next_permutation(p,p+k) );

        printf("Case #%d: %d\n", i+1, best );
    }
    return 0;
}
