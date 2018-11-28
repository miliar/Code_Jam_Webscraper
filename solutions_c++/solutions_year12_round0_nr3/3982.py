#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv){


int num, nums = 0;
int A,B, k , l;
char s[12][1000];
scanf("%d\n", &num);


for(int i = 0 ; i < num ; ++i){
        scanf("%d %d\n", &A, &B);
        nums = 0;
                  for(int j = A; j < B ; ++j){
                          
                          memset(s[0],0,sizeof(char)*1000);                          
                          sprintf(s[0],"%d\0", j);

                         // printf("%d\n",strlen(s[0]));
                          for(int k = 1; k < strlen(s[0]); ++k){
                          memset(s[k],0,sizeof(char)*1000);
                                  strcpy(s[k],&s[0][k]);
                                  strncat(s[k],s[0], k);
                          
                          for(l = 1; l < k ; ++l){
                          if(strcmp(s[l],s[k]) == 0)
                          break;
                          }
                          if(l != k)
                          continue;
                                     
                          if(atoi(s[k]) <= B && atoi(s[k]) > j){
                          ++nums;
                          }
                          }

                          }
        
        printf("Case #%d: %d\n", i + 1, nums);
        
        }

return 0;
}
