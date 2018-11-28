#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;
typedef long long LL;
const int Max = 512;
int R,C,sz;
int A[Max][Max];
char st[Max];
int check(int K){
    bool find = false;
    int mk = (K+1) / 2-1,dk = (K+1) & 1;
    //printf("K = %d | mk = %d\n",K,mk);
    for (int i = 1;i+K <= R+1 && !find;i++)
        for (int j = 1;j+K <= C+1 && !find;j++){
            int sumX = 0,sumY = 0;
            for (int x = 0;x < K;x++)
                for (int y = 0;y < K;y++){
                    if (x == 0 && y == 0) continue;
                    if (x == 0 && y+1 == K) continue;
                    if (x+1 == K && y == 0) continue;
                    if (x+1 == K && y+1 == K) continue;
                    int dx = (x-mk)*2-dk;
                    int dy = (y-mk)*2-dk;
                    sumX += dx*A[x+i][y+j];
                    sumY += dy*A[x+i][y+j];
                    //printf("at %d,%d(%d,%d) %d | %d %d\n",x,y,dx,dy,A[x+i][y+j],sumX,sumY);
                }
            //printf("check %d %d: %d %d\n",i,j,sumX,sumY);
            if (sumX == 0 && sumY == 0){
                find = true;
                break;
            }
        }
    //printf("%d : %d\n",K,find);
    return find;
}
int main(){
    int T;
    scanf("%d",&T);
    for (int ct = 1;ct <= T;ct++){
        int D;
        scanf("%d%d%d",&R,&C,&D);
        for (int i = 1;i <= R;i++){
            scanf("%s",st);
            for (int j = 1;j <= C;j++){
                A[i][j] = st[j-1]-'0';
            }
        }
        sz = min(R,C);
        int Res = -1;
        for (int K = 3;K <= sz;K++)
            if (check(K))
                Res = K;
        if (Res >= 3)
            printf("Case #%d: %d\n",ct,Res);
        else
            printf("Case #%d: IMPOSSIBLE\n",ct);
    }
    return 0;
}
