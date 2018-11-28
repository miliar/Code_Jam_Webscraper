#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int i, j, k;
    int T, N;
    int count=0;
    int *a;
    int *b;
    
    //how many case input
    scanf("%d", &T);

    //each case input
    for(i=0; i<T;i++){
        scanf("%d", &N);
        a= new int[N];
        b= new int[N];
        for(j=0; j<N; j++){
            scanf("%d %d", &a[j], &b[j]);
        }
        count=0;
        for(j=0;j<N;j++){
            for(k=j+1;k<N;k++){
                if(a[j]>a[k] && b[j]<b[k]){
                    count++;        
                }else if(a[j]<a[k] &&  b[j]>b[k])
                    count++;                   
            }
        }
        
        //output    
        printf("Case #%d: %d\n", i+1, count);
    }
    
    //system("PAUSE");
    return 0;
}
