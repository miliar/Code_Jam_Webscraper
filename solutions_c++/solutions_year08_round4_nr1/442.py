#include <stdio.h>
#include <string.h>

int val[20000];
int type[20000];
int changeable[20000];
int dpmat[20000][2];

#define IMPOSSIBLE 20000

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int n,v;
        scanf("%d%d", &n,&v);
//        printf("> %d %d\n", (n-1)/2, n-(n-1)/2);
        for (int i=0;i<(n-1)/2;i++){
            scanf("%d%d", &type[i+1], &changeable[i+1]);
        }   
        for (int i=(n-1)/2;i<n;i++){
            scanf("%d", &val[i+1]);
        }
        
        for (int i=1;i<=n;i++)
            dpmat[i][0]=dpmat[i][1]=IMPOSSIBLE;
        for (int i=n;i>0;i--){
            if (2*i>n){
                // leaf
                dpmat[i][val[i]] = 0;
            } else {                
                // internal
                int left = i*2;
                int right = i*2+1;
                if (type[i]){
                    // AND            
                    dpmat[i][0]<?=dpmat[left][0]+dpmat[right][0];        
                    dpmat[i][0]<?=dpmat[left][1]+dpmat[right][0];        
                    dpmat[i][0]<?=dpmat[left][0]+dpmat[right][1];        
                    dpmat[i][1]<?=dpmat[left][1]+dpmat[right][1];        
                    if (changeable[i]){
                        dpmat[i][0]<?=dpmat[left][0]+dpmat[right][0]+1;        
                        dpmat[i][1]<?=dpmat[left][1]+dpmat[right][0]+1;        
                        dpmat[i][1]<?=dpmat[left][0]+dpmat[right][1]+1;        
                        dpmat[i][1]<?=dpmat[left][1]+dpmat[right][1]+1;    
                    }                    
                } else {
                    // OR
                    dpmat[i][0]<?=dpmat[left][0]+dpmat[right][0];        
                    dpmat[i][1]<?=dpmat[left][1]+dpmat[right][0];        
                    dpmat[i][1]<?=dpmat[left][0]+dpmat[right][1];        
                    dpmat[i][1]<?=dpmat[left][1]+dpmat[right][1];     
                    if (changeable[i]){
                        dpmat[i][0]<?=dpmat[left][0]+dpmat[right][0]+1;        
                        dpmat[i][0]<?=dpmat[left][1]+dpmat[right][0]+1;        
                        dpmat[i][0]<?=dpmat[left][0]+dpmat[right][1]+1;        
                        dpmat[i][1]<?=dpmat[left][1]+dpmat[right][1]+1;        
                    }                       
                }
            }
        }
        
        printf("Case #%d: ", ++ttc);
        if (dpmat[1][v]>=IMPOSSIBLE){
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", dpmat[1][v]);
        }
    }
    
    return 0;
}
