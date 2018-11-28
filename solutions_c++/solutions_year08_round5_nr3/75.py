#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_SIZE    (100)
#define MAX_PPL     (10)
int H, W;
bool cansit[MAX_SIZE][MAX_SIZE];
int best[1 << MAX_PPL];
int nextbest[1 << MAX_PPL];

int allowed(int front, int back, bool* cansitrow) {
    int i, j;
    bool lastsit = false;
    j = 0;
    for (i = 0; i < W; i++) {        
        if (back & (1 << i)) {
            if (!cansitrow[i]) return -1;
            if (lastsit) return -1;
            lastsit = true;
            j++;
        } else {
            lastsit = false;
        }
    }
    
    
    for (i = 0; i < W; i++) {
        if (front & (1 << i)) { //front is occupied
            if (i > 0) if (back & (1 << (i-1))) return -1;
            if (i < W) if (back & (1 << (i+1))) return -1;
        }
    }
    
    return j;
}

int main() {
    int NTc;
    scanf("%d", &NTc);
    char buf[1024];
    int i, j, k, m;
    for (int tc = 0; tc < NTc; tc++) {
        printf("Case #%d: ", tc+1);
        scanf("%d %d", &H, &W);
        
        for (i = 0; i < H; i++) {
            scanf("%s", buf);
            for (j = 0; j < W; j++) cansit[i][j] = buf[j] == '.';
        }
        
        memset(best, 0, sizeof(0));
        for (i = 0; i < (1 << W); i++) {
            bool lastsit = false;
            int init = 0;
            for (j = 0; j < W; j++) {
                if (cansit[0][j] && (i & (1 << j))) {
                    if (lastsit) {
                        init = 0;
                        break;
                    }
                    init++;
                    lastsit = true;
                } else {
                    lastsit = false;
                }
            }
            //printf("best[%d] = %d\n", i, init);
            best[i] = init;
        }
        
        //printf("START\n");
        for (k = 1; k < H; k++) {
            //printf("row %2\n", k);
            for (i = 0; i < (1 << W); i++) {
                //printf("for config %d\n", i);
                nextbest[i] = 0;
                for (j = 0; j < (1 << W); j++) {
                    //printf("vs config %d\n", j);
                    m = allowed(j, i, cansit[k]);
                    if (m >= 0) {
                        m += best[j];
                        if (m > nextbest[i]) nextbest[i] = m;
                    }
                }
            }
            memcpy(best, nextbest, sizeof(best));
        }
        
        int globalbest = 0;
        for (i = 0; i < (1 << W); i++) {
            if (best[i] > globalbest) globalbest = best[i];
        }
        printf("%d\n", globalbest);
    }
    return 0;
}
