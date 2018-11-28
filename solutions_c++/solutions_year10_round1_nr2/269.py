#include <stdio.h>
#include <cstring>
#include <iostream>
using namespace std;

const int MAXV = 0x3f3f3f3f;

int cost[2][256];
bool used[256];

int main(){
    int testnum, D, I, M, N, a, b, p, mi, mj, cnt, tmp;

    scanf("%d", &testnum);
    for(int test = 1;test <= testnum;test++){
        scanf("%d%d%d%d", &D, &I, &M, &N);
        memset(cost[0], 0, sizeof(cost[0]));
        a = 0;b = 1;
        for(int i = 0;i < N;i++){
            //for(int j = 0;j < 256;j++)
            //    printf("%d:%d\t", j, cost[a][j]);
            scanf("%d", &p);
            memset(cost[b], 0x3f, sizeof(cost[b]));
            for(int j = 0;j < 256;j++){
                if(cost[a][j] < MAXV)
                    cost[b][j] = min(cost[b][j], cost[a][j] + D);
                int tmp = abs(j - p);
                for(int k = max(0, j - M);k < 256 && k <= j + M;k++){
                    if(cost[a][k] < MAXV)
                        cost[b][j] = min(cost[b][j], cost[a][k] + tmp);
                }
            }
            memset(used, false, sizeof(used));
			if(M != 0)
            for(int ii = 0;ii < 256;ii++){
                mi = MAXV;mj = -1;
                for(int j = 0;j < 256;j++)
                    if(!used[j] && cost[b][j] < mi){
                        mi = cost[b][j];mj = j;
                    }
                used[mj] = true;
                for(int j = 0;j < 256;j++){
                    if(!used[j] && cost[b][j] > (tmp = mi + (((abs(j - mj) - 1) / M) + 1) * I)){
                        cost[b][j] = tmp;
                    }
                }
            }
            a = b; b ^= 1;
        }
        //for(int j = 0;j < 256;j++)
        //    printf("%d:%d\t", j, cost[a][j]);
        printf("Case #%d: ", test);
        mi = MAXV;
        for(int i = 0;i < 256;i++){
            if(cost[a][i] < mi)
                mi = cost[a][i];
        }
        printf("%d\n", mi);
    }
    return 0;
}
