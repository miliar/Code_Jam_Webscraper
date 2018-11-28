#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int T,Ti;
    cin >> T;
    char N[30] = {0};
    char next[30] = {0};
    for (Ti=0; Ti<T; ++Ti) {
        cin >> N;
        int L = strlen(N);
        int j;
        for (j=L-1; j>=1; --j) {
            if (N[j] > N[j-1]) break;
        }
        // printf("j=%d\n", j);
        if (j >=1 ) {
            int k;
            for (k=L-1; k>=j; k--) if (N[j-1] < N[k]) break;
            char tmp = N[k]; N[k] = N[j-1]; N[j-1] = tmp;
            for (k=0; k<L; ++k) {
                if (k < j) next[k] = N[k];
                else next[k] = N[L-1-k+j];
            }
            next[k] = '\0';
        } else {
            int k;
            for (k=L-1; k>=0; k--) if (N[k]!='0') break;
            next[0] = N[k]; N[k] = '0'; next[L] = '\0'; next[L+1] = '\0';
            for (k=L-1; k>=0; k--) {
                next[L-k] = N[k];
            }
        }
        printf("Case #%d: %s\n", Ti+1, next);
    }

    return 0;
}
