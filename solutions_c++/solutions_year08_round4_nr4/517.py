#include <stdio.h>
#include <string.h>

#define MAX_LEN (10000)

char source[MAX_LEN];
char final[MAX_LEN];
int K;
int L;

void fillFinal(int level, int chosen) {
    for (int i = 0; i < L; i+=K) {
        final[i + level] = source[i + chosen];
    }
}

int bestRes;

void goCount() {
    //printf("final=%s\n", final);
    int res = 0;
    char last = ' ';
    for (int i = 0; i < L; i++) {
        if (final[i] != last) {
            res++;
            last = final[i];
        }
    }
    if (res < bestRes) bestRes = res;
}

int main() {
    int NTc;
    scanf("%d", &NTc);
    int i, j, k, m, n;
    for (int tc = 0; tc < NTc; tc++) {
        printf("Case #%d: ", tc+1);
        scanf("%d", &K);
        scanf("%s", source);
        L = strlen(source);
        bool used[20];
        memset(used, 0, sizeof(used));
        memset(final, 0, sizeof(final));
        bestRes = L;
        
        for (i = 0; i < K; i++) {
            if (used[i]) continue;
            used[i] = true;
            fillFinal(0, i);
            for (j = 0; j < K; j++) {
                if (used[j]) continue;
                used[j] = true;
                fillFinal(1, j);
                if (K == 2) goCount();
                else {
                    for (k = 0; k < K; k++) {
                        if (used[k]) continue;
                        used[k] = true;
                        fillFinal(2, k);
                        if (K == 3) goCount();
                        else {
                            for (m = 0; m < K; m++) {
                                if (used[m]) continue;
                                used[m] = true;
                                fillFinal(3, m);
                                if (K == 4) goCount();
                                else {
                                    for (n = 0; n < K; n++) {
                                        if (used[n]) continue;
                                        used[n] = true;
                                        fillFinal(4, n);
                                        if (K == 5) goCount();
                                        used[n] = false;
                                    }
                                }                
                                used[m] = false;
                            }
                        }                
                        used[k] = false;
                    }
                }                
                used[j] = false;
            }
            used[i] = false;
        }
        
        printf("%d\n", bestRes);
    }
    return  0;
}
