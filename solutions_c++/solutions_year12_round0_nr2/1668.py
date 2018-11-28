#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAXN 1000

int score[MAXN];

int main(){
    int T, N, p, s, count, tc = 1;
    
    scanf("%d", &T);
    while(T--){
               count = 0;
               scanf("%d %d %d", &N, &s, &p);
               for(int i = 0; i < N; i++){
                       scanf("%d", &score[i]);
                       
                       int base = score[i]/3;
                       switch(score[i] % 3){
                              case 0:
                                   {
                                       if (base >= p)
                                          count++;
                                       else{
                                            if (s > 0 && base > 0 && base + 1 >= p){            
                                               count++;
                                               s--;
                                            }            
                                       }   
                                       break; 
                                   }   
                              case 1:
                                   {
                                       if (base >= p || base + 1 >= p)
                                          count++;
                                       else{
                                            if (s > 0 and base + 1 >= p){
                                               count++;
                                               s--;
                                            }
                                       }
                                       break;
                                   }  
                              case 2:
                                   {
                                       if (base + 1 >= p || base >= p)
                                          count++;
                                       else{
                                            if (s > 0 and base + 2 >= p){
                                               count++;
                                               s--;
                                            }
                                       }
                                       break;
                                   }
                       }
               }
               printf("Case #%d: %d\n", tc, count);
               tc++;
    }
    return 0;
}
