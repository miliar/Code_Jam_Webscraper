#include<stdio.h>
int aa[31]={5, 27, 143, 751, 935, 607, 903, 991, 335, 47,
            943, 471, 55, 447,463, 991, 95, 607, 263, 151, 
            855, 527, 743, 351, 135, 407, 903, 791, 135, 647};
int main(){
    int N,n,k;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    scanf("%d",&N);
    for(k=1;k<=N;++k){
        scanf("%d",&n);
        printf("Case #%d: %03d\n",k,aa[n-1]);
    }
    return 0;
}        
