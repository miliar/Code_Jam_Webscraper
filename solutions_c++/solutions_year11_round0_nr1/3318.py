#include "stdio.h"
#include "stdlib.h"

int pos[2] = {1,1}; //o for O, 1  for B
int t, n, i, j;
int p, r, totalTime, lastTime = 0, turn, neededTime, last;

int main(){
    FILE *file;
    
    file = fopen("output.txt","w");
    scanf("%d", &t);
    for(i = 0; i < t; i++){
          scanf("%d", &n);
          
          for(j = 0; j < n; j++){
                scanf(" %c %d", &r, &p);
                r == 'O' ? turn = 0 : turn = 1; 
                if(j == 0){
                       last = turn;     
                       totalTime = p;
                       lastTime = totalTime;
                } else if(last == turn){
                       neededTime = abs(p - pos[turn]) + 1;
                       lastTime += neededTime;
                       totalTime += neededTime;
                } else {                       
                       neededTime = abs(p - pos[turn]) + 1;
                       if(lastTime >= neededTime-1){
                              totalTime++;
                              lastTime = 1;                                                     
                       } else {                                    
                              totalTime += neededTime - lastTime;
                              lastTime = neededTime - lastTime; 
                       }                      
                }                
                pos[turn] = p;
                last = turn;
          }    
          fprintf(file,"Case #%d: %d\n",i+1, totalTime);    
          lastTime = 0;
          totalTime = 0;    
          pos[0] = 1;
          pos[1] = 1;
    }
    fclose(file);
    return 0;    
}
