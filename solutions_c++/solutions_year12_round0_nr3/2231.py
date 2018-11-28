#include<stdio.h>

int tenPow[10];
int visited[2000010];
int countDigits(int a){
    int dig=1;
    for(int i=1;;i++,dig++)
        if(a<tenPow[i]) break;
    return dig;
}

int main(){
    int T,A,B;
    tenPow[0]=1;
    for(int i=1;i<8;i++)
        tenPow[i]=tenPow[i-1]*10;
    scanf("%d",&T);
    int count=1;
    for(int k=1;k<=T;k++){
        int ans=0;
        scanf("%d%d",&A,&B);
        for(int i=A;i<=B;i++,count++){
            int aux=i,dig;
            int lim=countDigits(i)-1;
            for(int j=0;j<lim;j++){
                dig=aux%10;
                aux=(aux/10)+(tenPow[lim]*dig);
                if(countDigits(aux)==lim+1&&aux<i&&aux>=A&&visited[aux]<count){
                    visited[aux]=count;
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
