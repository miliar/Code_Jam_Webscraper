#include <stdio.h>
#include <limits.h>
int nume[2000];
int N;
int suma;
int minimo;
int XOR;
int main(){
    int nt;
    scanf("%d",&nt);
    for(int test=1;test <= nt;test++){
        printf("Case #%d: ",test);
        suma = 0;
        minimo = INT_MAX;
        XOR = 0;
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%d",&nume[i]);
            suma+=nume[i];
            if( minimo > nume[i]){
                minimo = nume[i];
            }
            XOR ^= nume[i];
        }
        if( XOR == 0){
            printf("%d",suma-minimo);
        }else{
            printf("NO");
        }
        printf("\n");
    }
    return 0;
}
