#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

char str[50001];
char str2[50001];
int perm[16];

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t) {

        int K, N;
        scanf("%d %s", &K, str);
        N = strlen(str);

        for(int i=0;i<K;++i) {
            perm[i]=i;
        }

        int resp = N+1;
        do {
            for(int i=0;i<N;i+=K) {
                for(int j=0;j<K;++j) {
                    str2[i+j] = str[i+perm[j]];
                }
            }

            int len = unique(str2, str2+N) - str2;
            resp = min(resp, len);
        } while(next_permutation(perm, perm+K));

        printf("Case #%d: %d\n", t, resp);
    }
    return 0;
}
