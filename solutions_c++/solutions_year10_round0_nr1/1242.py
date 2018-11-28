#include<stdio.h>

int in[35];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int C,N,K;
    scanf("%d",&C);
    in[1]=1;
    for(int i=2;i<=30;i++) in[i]=in[i-1]*2+1;
    for(int c=0;c<C;c++){
        scanf("%d %d",&N,&K);
        if(K<in[N]) printf("Case #%d: OFF\n",c+1);
        else if(K==in[N]) printf("Case #%d: ON\n",c+1);    
        else {
            if(K%(in[N]+1)==in[N]) printf("Case #%d: ON\n",c+1);
            else printf("Case #%d: OFF\n",c+1);
        }
    }    
return 0;
}
