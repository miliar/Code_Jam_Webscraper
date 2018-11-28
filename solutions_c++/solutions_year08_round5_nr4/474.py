#include<iostream>
using namespace std;
#define N 108

int num[N][N];
bool flag[N][N];
    
int main(){
    freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\out.txt","w",stdout);
    int n, i, j, k, W, H, R, r, c;
    scanf("%d",&n);
    for(i=1; i<=n; i++){
        memset( flag, 0, sizeof(flag) );
        memset( num, 0, sizeof(num) );
        num[1][1] = 1; 
        scanf("%d%d%d",&H,&W,&R);
        for(j=0; j<R; j++){
            scanf("%d%d",&r,&c);
            flag[r][c] = true;
        }
        for(j=1; j<=H; j++){
            for(k=1; k<=W; k++){
                if( flag[j][k] ){ num[j][k]=0; continue;}
                if(k-2>=1&&j-1>=1){
                    num[j][k] += num[j-1][k-2];
                }
                if(j-2>=1&&k-1>=1){
                    num[j][k] += num[j-2][k-1];
                }
                num[j][k] %= 10007;
            }
        }
        printf(" Case #%d: %d\n",i,num[H][W]%10007);
    }
    return 0;
}
