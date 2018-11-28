#include <stdio.h>
#include <string>
#include <vector>

#define MAX_NSE (200)
#define MAX_NLEN (200)
#define MAX_Q (2000)
using namespace std;


int NSE, NQ;
char engineName[MAX_NSE][MAX_NLEN];

int main() {
    int i, j, k;
    int N;
    char buf[1000];
    
    gets(buf);
    sscanf(buf, "%d", &N);
    for (i = 0; i < N; i++) {
                
        printf("Case #%d: ", i+1);
        gets(buf);
        sscanf(buf, "%d", &NSE);
        for (j = 0; j < NSE; j++) {
            gets(engineName[j]);            
        }
        gets(buf);
        sscanf(buf, "%d", &NQ);
        int queries[MAX_Q];
        for (j = 0; j < NQ; j++) {
            gets(buf);
            for (k = 0; k < NSE; k++) {
                if (!strcmp(buf, engineName[k])) {
                    queries[j] = k; 
                    break;
                }
            }
        }
        
        if (NQ == 0) {
            printf("0\n");
            continue;
        }

        int currId = queries[0];
        int res = 0;
        for (j = 0; j < NQ; j++) {
            if (currId != queries[j]) continue;
            
            res++;
            int nextUsed[MAX_NSE];
            memset(nextUsed, -1, sizeof(nextUsed));
            nextUsed[currId] = j;
            for (k = j+1; k < NQ; k++) {
                if (queries[k] == currId) continue;
                if (nextUsed[queries[k]] == -1) {
                    nextUsed[queries[k]] = k;
                }
            }

            for (k = 0; k < NSE; k++) {
                if (nextUsed[k] == -1) {
                    currId = k;
                    break;
                }
                if (nextUsed[k] > nextUsed[currId]) {
                    currId = k;
                }
            }
        }
        
        printf("%d\n", res-1); 
    }
    return 0;
}
