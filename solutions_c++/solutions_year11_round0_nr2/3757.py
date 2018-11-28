#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++) {
         int c,d,n;
         char cmb[5], oppo[5];
         scanf("%d",&c);
         if(c == 1) {
              scanf("%s",cmb);        
         }
         scanf("%d",&d);
         if(d == 1) {
              scanf("%s",oppo);
         }
         scanf("%d",&n);
         char elem;
         char list[20];
         scanf(" %c",&list[0]);
         int aux = 1;
         int aux2 = 1;
         for(int j = 1;j < n;j++) {
             scanf(" %c",&elem);
             aux2 = 1;
             if(c == 1 && aux > 0 && (elem == cmb[0] && list[aux-1] == cmb[1]) || (elem == cmb[1] && list[aux-1] == cmb[0])) {
                   list[aux-1] = cmb[2];      
                   aux--;
                   if(d == 1 && list[aux-1] == oppo[0]) {     
                        for(int k = 0;k < aux;k++) {
                             if(list[k] == oppo[1]) {
                                aux = -1;
                                break;
                             }
                        }
                   }
                   if(d == 1 && list[aux-1] == oppo[1]) {     
                       for(int k = 0;k < aux;k++) {
                           if(list[k] == oppo[0]) {
                              aux = -1;
                              break;
                           }
                       }
                   }
                   aux2 = 0;             
             }
             if(d == 1 && elem == oppo[0] && aux2) {     
                 for(int k = 0;k < aux;k++) {
                     if(list[k] == oppo[1]) {
                          aux = -1;
                          aux2 = 0;
                          break;
                     }
                 }
             }
             if(d == 1 && elem == oppo[1] && aux2) {     
                 for(int k = 0;k < aux;k++) {
                     if(list[k] == oppo[0]) {
                          aux = -1;
                          aux2 = 0;
                          break;
                     }
                 }
             }
             if(aux2) {
                  list[aux] = elem;  
             }                   
             aux++;                  
         }
         printf("Case #%d: [",i);    
         for(int j = 0; j < aux-1;j++) {
               printf("%c, ",list[j]);          
         }
         if(aux > 0)
                printf("%c]\n",list[aux-1]);
         else printf("]\n");                      
    }
    return 0;
}    
