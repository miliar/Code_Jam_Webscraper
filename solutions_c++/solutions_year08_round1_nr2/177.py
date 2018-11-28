#include <cstdio>
#include <algorithm>

using namespace std;

int MALTED[2048];
bool LIKES[2048][2048]; // [customer][shake]
int CNT[2048];

int NEEDS_MALTING[2048]; // 0 = not malted, 1 = waiting, 2 = already malted

int C, N, M;

int main() {
    scanf("%d", &C);
    for (int c=0; c<C; c++) {
        scanf("%d%d", &N, &M);
        fill(NEEDS_MALTING, NEEDS_MALTING+2048, 0);
        fill(MALTED, MALTED+2048, -1);
        fill(CNT, CNT+2048, 0);
        for (int i=0; i<N; i++)
            for (int j=0; j<M; j++)
                LIKES[j][i]=false;
        for (int m=0; m<M; m++) {
            int t;
            scanf("%d", &t);
            for (int i=0; i<t; i++) {
                int x, y; scanf("%d%d", &x, &y); x--;
                if (LIKES[m][x]) MALTED[m]=-2;
                else if (y==1) MALTED[m]=x;
                else LIKES[m][x]=true, CNT[m]++;
            }
        }
        
        for (int i=0; i<M; i++) {
            if (MALTED[i]>=0 && CNT[i]==0)
                NEEDS_MALTING[MALTED[i]]=1, CNT[i]--, MALTED[i]=-2;
        }
        
        while (true) {
            int wix=0;
            while (wix<N && NEEDS_MALTING[wix]!=1) wix++;
            if (wix==N) {
                // print result + break
                printf("Case #%d:", c+1);
                for (int i=0; i<N; i++) printf(" %d", NEEDS_MALTING[i]/2);
                printf("\n");
                break;
            }
            
            for (int i=0; i<M; i++) {
                if (MALTED[i]==-2) continue;
                if (!LIKES[i][wix]) continue;
                CNT[i]--;
                if (CNT[i]==0 && MALTED[i]==-1) {
                    printf("Case #%d: IMPOSSIBLE\n", c+1);
                    goto bye;
                }
                if (CNT[i]==0 && NEEDS_MALTING[MALTED[i]]==0) NEEDS_MALTING[MALTED[i]]=1;
            }
            
            NEEDS_MALTING[wix]=2;
            
        }
        
        bye:{}
    }

    return 0;
}
