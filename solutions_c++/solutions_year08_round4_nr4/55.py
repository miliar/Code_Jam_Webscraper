#include <iostream>
#include <cmath>
using namespace std;
char word[500000];
int ans[16][16][1<<16];
int compare[16][16], comparelast[16][16];
int solve(int first, int recent, int left) {
    if (ans[first][recent][left]>=0) return ans[first][recent][left];
    int ret = 0;
    for (int i=0; i<16; i++) {
        if (left&(1<<i)) {
            int next = left&~(1<<i);            
            int poss = compare[recent][i];
            if (next!=0) {
                int poss = compare[recent][i]+solve(first,i,next);
                if (ans[first][recent][left]<0 || ans[first][recent][left]>poss) {
                    ans[first][recent][left]=poss;
                }
            } else {
                int poss = compare[recent][i]+comparelast[i][first];
                if (ans[first][recent][left]<0 || ans[first][recent][left]>poss) {
                    ans[first][recent][left]=poss;
                }                
            }
        }
    }
    //printf("%d %d %d: %d\n",first,recent,left,ans[first][recent][left]);
    return ans[first][recent][left];
}
int main() {
    int T;scanf("%d",&T);for (int t=1; t<=T; t++) {
        int k; scanf("%d",&k);
        scanf("%s",word);
        int len = strlen(word);
        int ret = 5000000;
        
        for (int i=0; i<k; i++)
        for (int j=0; j<k; j++)
        for (int kk=(1<<k)-1; kk>=0; kk--) ans[i][j][kk]=-1;
        
        for (int i=0; i<k; i++)
        for (int j=0; j<k; j++) {
            compare[i][j]=0;
            for (int kk=0; kk<len; kk+=k) {
                if (word[kk+i]!=word[kk+j]) compare[i][j]++;
            }
            comparelast[i][j]=0;
            for (int kk=k; kk<len; kk+=k) {
                if (word[kk-k+i]==word[kk+j]) comparelast[i][j]--;
            }
            //printf("Compare[%d][%d] = %d\n",i,j,compare[i][j]);
        }
        for (int i=0; i<k; i++) ret<?=len/k+solve(i,i,((1<<k)-1)&~(1<<i));
        printf("Case #%d: %d\n",t,ret);
    }
}
