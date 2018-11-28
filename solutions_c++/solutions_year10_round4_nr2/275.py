#include <iostream>
using namespace std;
int canmiss[1040];
int prices[1040][15];
int ans[1040][15][15];
int themin[1040][15];
int getmin(int start, int len) {
    if (themin[start][len]!=-1) return themin[start][len];
    if (len==0) {
        int ans = themin[start][len]=canmiss[start];
        return themin[start][len]=ans;
    }
    else {
        int ans = min(getmin(start,len-1),getmin(start+(1<<(len-1)),len-1));
        return themin[start][len]=ans;
    }
}
int get(int start, int len, int subtracted) {
    if (len==0) return 0;
    if (ans[start][len][subtracted]!=-1) return ans[start][len][subtracted];
    // how much does it cost?
    int costhere = prices[start][len];
    // case 1: we buy this game
    int poss = costhere + get(start,len-1,subtracted) + get(start+(1<<(len-1)),len-1,subtracted);
    
    // can we skip this game?
    //printf("Minimum skippable for positions %d to %d is %d\n",start,start+(1<<len)-1,getmin(start,len));
    if (getmin(start,len)-subtracted>=1) {
        int poss2 = get(start,len-1,subtracted+1) + get(start+(1<<(len-1)),len-1,subtracted+1);
        poss <?= poss2;
    }
    return ans[start][len][subtracted]=poss;
    
}
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);
        int P; scanf("%d",&P);
        for (int i=0; i<(1<<P); i++) {
            scanf("%d",&canmiss[i]);
        }
        int pow2 = 1;
        for (int i=0; i<P; i++) {
            pow2 *= 2;
            for (int j=0; j<(1<<P); j+=pow2) {
                scanf("%d",&prices[j][i+1]);
            }
        }
        memset(ans,-1,1040*15*15*sizeof(int));
        memset(themin,-1,1040*15*sizeof(int));
        printf("%d\n",get(0,P,0));
        
    }
}
