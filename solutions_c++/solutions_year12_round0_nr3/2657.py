#include <stdio.h>

int c[2000001];
int dig[2000001];
long long p10[10];
int u[2000001];
int list[2500000][2];

int main(){
    int TT,tt,i,j,A,B,r,s;
    long long x,y;
    p10[0]=1;
    for( i=1; i<10; i++ ){
        dig[i]=1;
        p10[i]=p10[i-1]*10;
    }
    r=0;
    for( i=10; i<=2000000; i++ ){
        dig[i]=dig[i/10]+1;
        x = (long long)i*(p10[dig[i]]+1);
        for( j=1; j<dig[i]; j++ ) {
            x/=10;
            y = x%p10[dig[i]];
            if(y<i && dig[y]==dig[i] && u[y]!=i){
                u[y]=i;
                list[r][0] = y;
                list[r][1] = i;
                r++;
            }
        }
    }
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d %d",&A,&B);
        s=0;
        for( i=0; i<r; i++ ){
            if(list[i][0]>=A && list[i][1]<=B){
                s++;
            }
        }
        printf("Case #%d: %d\n",tt+1,s);
    }
    return 0;
}
