#include <iostream>
#include <cmath>
using namespace std;
char input[500][501];
int sums[500][500];
int sum1K[500][500], sum2K[500][500];
int getsum(int a, int b, int c, int d) {
    return sums[c][d] - (a>0?sums[a-1][d]:0) - (b>0?sums[c][b-1]:0) + (a>0 && b>0?sums[a-1][b-1]:0);
}
int mults[500];
int x,y,sum1,sum2,K;
void shiftup() {
    sum2 -= mults[0] * getsum(x,y,x+K-1,y);
    sum2 += mults[K-1] * getsum(x,y+K,x+K-1,y+K);
    sum2 += (K%2==0?2:1)*getsum(x,y+1,x+K-1,y+K-1);
    
    sum1 -= sum2K[x][y];
    sum1 += sum2K[x][y+K];
    //printf("sum1 -= %d, += %d\n",sum2K[x][y],sum2K[x][y+K]);
    y++;

}
void shiftdown() {
    sum2 -= mults[K-1] * getsum(x,y+K-1,x+K-1,y+K-1);
    sum2 += mults[0] * getsum(x,y-1,x+K-1,y-1);
    sum2 -= (K%2==0?2:1)*getsum(x,y,x+K-1,y+K-2);
    
    sum1 -= sum2K[x][y+K-1];
    sum1 += sum2K[x][y-1];    
    y--;
}
void shiftright() {
    sum1 -= mults[0] * getsum(x,y,x,y+K-1);
    sum1 += mults[K-1] * getsum(x+K,y,x+K,y+K-1);
    sum1 += (K%2==0?2:1)*getsum(x+1,y,x+K-1,y+K-1);
    
    sum2 -= sum1K[x][y];
    sum2 += sum1K[x+K][y];

    x++;
}
bool ok() {
    // x,y to x+K-1,y+K-1
    int tot1 = mults[0]*((input[x][y]-'0' + input[x][y+K-1]-'0')-(input[x+K-1][y]-'0' + input[x+K-1][y+K-1]-'0'));
    int tot2 = mults[0]*((input[x][y]-'0' + input[x+K-1][y]-'0')-(input[x][y+K-1]-'0' + input[x+K-1][y+K-1]-'0'));    


    if (sum1==tot1 && sum2==tot2) return true;
    return false;
}
int main() {
    int T; scanf("%d",&T); for (int tt=1; tt<=T; tt++) {
        int R,C,D; scanf("%d %d %d",&R,&C,&D);
        for (int i=0; i<R; i++) scanf("%s",input[i]);
        
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                sums[i][j] = input[i][j]-'0' + (i>0?sums[i-1][j]:0) + (j>0?sums[i][j-1]:0) - (i>0 && j>0 ? sums[i-1][j-1]:0);
            }
        }
        
        int found = -1;
        for (K=max(R,C); K>=3; K--) {
           // printf("Testing %d\n",K);
            if (K%2==0) {
                for (int i=0; i<K; i++) {
                    mults[i] = K-1-2*i;
                }
            } else {
                for (int i=0; i<K; i++) {
                    mults[i] = K/2-i;
                    ///printf("mults[%d] = %d\n",i,mults[i]);
                }
            }            
            for (int i=0; i<R; i++) {
                int start = 0;
                for (int j=0; j<K; j++) start += mults[j] * (input[i][j]-'0');
                sum1K[i][0] = start;
//                printf("Start with %d\n",start);
                for (int j=1; j+K-1<C; j++) {
                    start+=mults[K-1] * (input[i][j+K-1]-'0') - mults[0] * (input[i][j-1]-'0') + (K%2==0?2:1)*getsum(i,j,i,j+K-2);
                    sum1K[i][j] = start;
                //    printf("Add %d*%d - %d*%d + %d*%d\n",mults[K-1],(input[i][j+K-1]-'0'),mults[0],(input[i][j-1]-'0'),K%2==0?2:1,getsum(i,j,i,j+K-2));
                }
              //  printf("\n");
            }

            for (int i=0; i<C; i++) {
                int start = 0;
                for (int j=0; j<K; j++) start += mults[j] * (input[j][i]-'0');
                sum2K[0][i] = start;
                for (int j=1; j+K-1<R; j++) {
                    start += mults[K-1] * (input[j+K-1][i]-'0') - mults[0] * (input[j-1][i]-'0') + (K%2==0?2:1)*getsum(j,i,j+K-2,i);
                    sum2K[j][i] = start;
                }
            }
 
            // start by finding sum of bottom left hand corner

            sum1 = 0;sum2 = 0;
            for (int i=0; i<K; i++) {
                sum2 += mults[i] * getsum(0,i,K-1,i);
                sum1 += mults[i] * getsum(i,0,i,K-1);
            }

            x=0;y=0;
            
            while (x+K<=R) {
                //printf("%d,%d: %d %d\n",x,y,sum1,sum2);
                if (ok()) {
                    found=K;
                    goto done;
                }
                // test this position
//                printf("Testing %d,%d to %d,%d\n",x,y,x+K-1,y+K-1);
                
                if (x%2==0) {
                    if (y+K<C) shiftup();
                    else shiftright();
                } else {
                    if (y>0) shiftdown();
                    else shiftright();
                }
            }
//            printf("\n");
        }
        done:;
        printf("Case #%d: ",tt);
        if (found==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",found);
        
    }
}
