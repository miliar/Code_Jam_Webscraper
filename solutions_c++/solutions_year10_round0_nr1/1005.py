#include<stdio.h>
#include<stdlib.h>
int main (){
    int n,k,i,ca = 0,T;
    int a[100];
    a[0] = 1;
    for( i=1 ;i < 31; i++ ){
        a[i] = a[i-1]*2;
    }
    scanf("%d",&T);
    for(ca = 1;ca<=T;ca++){
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",ca);
        if((k+1) % a[n] == 0){
            printf("ON\n");
        }
        else
            printf("OFF\n");
    }
    return 0;
}
