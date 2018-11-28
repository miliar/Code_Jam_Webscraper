#include<stdio.h>
#include<stdlib.h>

int cal(int i,int j){
    for(int k=0;k<i;k++){
        if(j%2==0)return 0;
        j/=2;
    }
    return 1;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,n,k;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d %d",&n,&k);
        if(cal(n,k)){
            printf("Case #%d: ON\n",i);
        }
        else{
            printf("Case #%d: OFF\n",i);
        }
    }
}
