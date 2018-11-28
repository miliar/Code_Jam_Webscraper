#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    int i, j;
    int T, N, K;
    double dn, dk;
    double result;
    
    //how many case input
    scanf("%d", &T);

    //each case input
    for(i=0; i<T;i++){
        scanf("%d %d", &N, &K);
        dn=(double)N;
        dk=(double)K;
        dn=pow(2.0, dn);
        result = fmod(dk, dn);
        //printf("dn %f k %f result %f\n", dn, dk, result);
      
        //output    
        if(result==dn-1.0){
            printf("Case #%d: ON\n", i+1);
        }else{
            printf("Case #%d: OFF\n", i+1);
        } 
    }
    
    //system("PAUSE");
    return 0;
}
