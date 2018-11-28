#include <stdio.h>
#include <string.h>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

int dpmat[101][101];
int spos[101][101];

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int h,w,r;
        scanf("%d%d%d", &h,&w,&r);
        memset(dpmat,0,sizeof(dpmat));
        dpmat[0][0]=1;
        memset(spos,0,sizeof(spos));
        while (r--){
            int a,b;
            scanf("%d%d", &a,&b);
            a--;b--;
            spos[a][b]=1;
        }
        for (int i=0;i<h;i++)
        for (int j=0;j<w;j++)
        if (!spos[i][j]){
            if (i>0 && j>1){
                dpmat[i][j]+=dpmat[i-1][j-2];
                dpmat[i][j]%=10007;
            }
            if (i>1 && j>0){
                dpmat[i][j]+=dpmat[i-2][j-1];
                dpmat[i][j]%=10007;
            }
        }
        
        printf("Case #%d: %d\n", ++ttc, dpmat[h-1][w-1]);
    }
    
    return 0;
}
