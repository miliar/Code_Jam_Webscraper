# include <stdio.h>
# include <stdlib.h>
int main(){
    int c,n,i,j,temp,sum;
    freopen("out.txt","w",stdout);
    scanf("%d",&c);
    for(j=1;j<=c;j++){
        sum=0;
        scanf("%d",&n);
        for(i=1;i<=n;i++){
            scanf("%d",&temp);
            if(temp!=i){
                sum++;
            }
        }
        printf("Case #%d: %d.000000\n",j,sum);
    }
    return 0;
}
