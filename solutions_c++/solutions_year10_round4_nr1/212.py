#include <iostream>
using namespace std;
int nums[500][500];
int K;
int getit(int x, int y) {
    // first square is at position (0,K-1)
    x>?=2*K-2-x;
    y>?=2*K-2-y;  
    /*
    // extend top left edge down
    // top left edge has points (m,K-1-m)
    */
    int ystart = y-(K-1-x);
    int xstart = x-(K-1-y);
    return max(xstart,ystart)+1;
}
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);
        memset(nums,-1,500*500*sizeof(int));
        scanf("%d",&K);
        int numdigs = 0;
        for (int i=0; i<K; i++) {
            for (int j=K-1-i; j<=K-1+i; j+=2) {
                scanf("%d",&nums[i][j]);
                numdigs++;
            }
        }
        for (int i=K; i<2*K-1; i++) {
            for (int j=i-K+1; j<=2*K-3-(i-K); j+=2) {             
                scanf("%d",&nums[i][j]);
                numdigs++;
            }
        }
        int best = 1000000;
        for (int x=0; x<2*K-1; x++) {
            for (int y=0; y<2*K-1; y++) {
//                printf("At %d,%d\n",x,y);
                bool ok = true;
                for (int l=0; l<2*K+1; l++)
                for (int m=0; m<2*K+1; m++) {
                    if (nums[l][m]==-1) continue;
                    int newl = 2*x-l;
                    int newm = 2*y-m;
                    
                    if (newl>=0 && newl<2*K-1) {
                        if (nums[newl][m]!=-1 && nums[newl][m]!=nums[l][m]) goto nope;
                    }
                    if (newm>=0 && newm<2*K-1) {
                        if (nums[l][newm]!=-1 && nums[l][newm]!=nums[l][m]) goto nope;
                    }                    
                }
                {
                int both = getit(x,y);
               // printf("Returning %d\n",both);
                best<?=both;
                }
                continue;
                nope:;
                
            }
        }
        printf("%d\n",best*best-K*K);
    }
}
