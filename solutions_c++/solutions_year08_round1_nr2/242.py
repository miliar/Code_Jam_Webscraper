#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

#define MAX_FLAVORS (10000)
#define MAX_CUST    (10000)
int C, N, M;

vector<int> pref[MAX_CUST];
int currFlav[MAX_FLAVORS];

int bestMalted;
int bestFlav[MAX_FLAVORS];

void check() {
    int i, j, k;
    for (i = 0; i < M; i++) {
        bool satisfied = false;
        for (j = 0; j < N; j++) {
            for (k = 0; k < pref[i].size(); k++) {
                if (pref[i][k] == currFlav[j]) {
                    satisfied = true;
                    goto nextcust;
                }
            }
        }
        nextcust:
        if (!satisfied) return;
    }
    
    int nMalted = 0;
    for (j = 0; j < N; j++) {
        if (currFlav[j] > 0) nMalted++;
    }
    
    if (bestMalted == -1 || nMalted < bestMalted) {
        bestMalted = nMalted;
        memcpy(bestFlav, currFlav, sizeof(bestFlav));
    }
}

void doit(int lev) {
    if (lev == N) {
        check();
        return;
    }
    
    currFlav[lev] = (lev + 1);
    doit(lev+1);
    currFlav[lev] = -(lev + 1);
    doit(lev+1);
}

int main() {
    int tc;
    scanf("%d", &C);
    int i, j, k, m, n;
    for (tc = 0; tc < C; tc++) {
        printf("Case #%d:", tc+1);
        scanf("%d %d", &N, &M);
                
        for (i = 0; i < M; i++) {
            pref[i].clear();
            scanf("%d", &j);
            for (k = 0; k < j; k++) {
                scanf("%d %d", &m, &n);
                pref[i].push_back(m * (n*2-1));
            }
        }
        
        bestMalted = -1;
        doit(0);
        if (bestMalted >= 0) {
            for (i = 0; i < N; i++) {
                printf(" %d", bestFlav[i] > 0);
            }
            printf("\n");
        } else {
            printf(" IMPOSSIBLE\n");
        }
    }
    
    return 0;
}
