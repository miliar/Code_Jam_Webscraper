#include <stdio.h>
#include <stdlib.h>
long long int N,L,H;
long long int num[10005];
bool sePueden(long long int numbe){
    for(int  i=0;i<N;i++){
       if( (numbe%num[i]) !=0 && (num[i]%numbe) !=0){
            return false;
       }
    }
    return true;
}
void resuelve(){
    scanf("%lld%lld%lld",&N,&L,&H);
    for(int i=0;i<N;i++){
        scanf("%lld",&num[i]);
    }
    for(long long i = L;i<=H;i++){
        if( sePueden(i)){
            printf("%lld",i);
            return;
        }
    }
    printf("NO");
}
int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        resuelve();
        printf("\n");
    }
    return 0;
}
