#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

char str[550];
char pattern[50]="welcome to code jam";
int c[20][550];
void printC(int len){
    int i,j;
    for(i=0;i<20;i++){
        for(j=0;j<len;j++)
            printf("%6d", c[i][j]);
        printf("\n");
    }    
}    
int main(){
   int n, len;
   int i,j,k,kk, ans;
   scanf("%d\n",&n);
   for(kk=0;kk<n;kk++){
      cin.getline(str, 545);
      len = strlen(str);
      for(j=0;j<len;j++)
          c[0][j] = ((str[j]==pattern[0])? 1:0);
      for(i=1;i<20;i++){
          for(j=0;j<len;j++){
              c[i][j]=0;
              if(str[j] == pattern[i]){
                  for(k=0;k<j;k++)
                      c[i][j]+=c[i-1][k];
                  c[i][j]%=10000;
              } 
          }    
      }   
      //printC(len);
      ans=0;       
      for(j=0;j<len;j++)
          ans+=c[18][j];
      printf("Case #%d: %04d\n", kk+1, ans%10000);   
   }    
   
   //scanf("%d",&i);
   return 0;
}    
