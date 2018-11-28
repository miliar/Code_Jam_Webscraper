#include <stdio.h>
int main() {
    int G[1000];
    int R;
    int k;
    int N;
    int T;
    int initBoardNext;
    int boardNext;
    int currSize;
    int totalEuro;
    scanf("%d", &T);
    for(int casenum = 0; casenum < T; ++casenum) {
        scanf("%d %d %d", &R, &k, &N);
        for(int i = 0; i < N; ++i) {
            scanf("%d", G+i);
        }
        initBoardNext = 0;
        boardNext = 0;
        totalEuro = 0;
        for(int currRun = 0; currRun < R; ++currRun) {
            currSize = 0;
            while(currSize <= k) {
                if( currSize + G[boardNext] > k )
                    break;
                
                // else
                currSize += G[boardNext];
                boardNext = (boardNext + 1) % N;
                if(boardNext == initBoardNext)
                    break;
            }
            totalEuro += currSize;
            initBoardNext = boardNext;
        }
        printf("Case #%d: %d\n", casenum+1, totalEuro);
    }
    return 0;
}
            
        
        
        
