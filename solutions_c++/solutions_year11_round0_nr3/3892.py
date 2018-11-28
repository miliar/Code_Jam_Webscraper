#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

void inc(int bin[]) {
     int i = 0;
     while(bin[i] == 1) {
        bin[i] = 0;
        i++;
     }     
     bin[i] = 1;
     return;
}     

int teste(int bin[], int doces[], int n) {
    int sean = 0, patrick = 0; 
    int soma1 = 0, soma2 = 0;   
    for(int i = 0;i < n;i++) {
        if(bin[i]) {
            patrick = patrick^doces[i];
            soma2 += doces[i];
        }
        else {
            sean = sean^doces[i];
            soma1 += doces[i];
        }               
    }        
    if(sean == patrick) return max(soma1,soma2);
    else return -1;
}    

int main() {
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++) {
         int n;
         scanf("%d",&n);
         int doces[20];
         for(int j = 0;j < n;j++) 
              scanf("%d",&doces[j]);        
         int bin[20];
         int soma = -100, soma_aux;
         memset(bin,0,sizeof(bin));
         for(int j = 0;j < 1<<(n-1);j++) {
             inc(bin);
             soma_aux = teste(bin,doces,n);
             if(soma_aux > 0 && soma_aux > soma) 
                   soma = soma_aux;                           
         }
         if(soma < 0) printf("Case #%d: NO\n",i);
         else printf("Case #%d: %d\n",i,soma);
    }        
    return 0;
}    
