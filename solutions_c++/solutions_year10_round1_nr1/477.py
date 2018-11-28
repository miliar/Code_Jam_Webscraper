#include "stdio.h"
#include "math.h"
#include "string.h"

char board[50][51];
char rotate[50][51];
int winner;
int n,k;

void findWinner(void){
   int near;
   bool flag;
   bool fB=true,fR=true;
   for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
         if(fB==false&&fR==false)break;

         char p=rotate[i][j];

         if(p=='.')continue;
         if(p=='B'&&fB==false)continue;
         if(p=='R'&&fR==false)continue;

         if(n-i>=k){
            flag=true;
            near=i+k;
            for(int q=i+1;q<near;q++){
               if(rotate[q][j]!=p){
                  flag=false;
                  break;
               }
            }
            if(flag){
               if(p=='B'){
                  fB=false;
                  winner+=2;
               }
               else{
                  fR=false;
                  winner+=1;
               }
               continue;
            }
            if(n-j>=k){
               flag=true;
               near=k;
               for(int q=1;q<near;q++){
                  if(rotate[i+q][j+q]!=p){
                     flag=false;
                     break;
                  }
               }
               if(flag){
                  if(p=='B'){
                     fB=false;
                     winner+=2;
                  }
                  else{
                     fR=false;
                     winner+=1;
                  }
                  continue;
               }
            }
            if(j+1>=k){
               flag=true;
               near=k;
               for(int q=1;q<near;q++){
                  if(rotate[i+q][j-q]!=p){
                     flag=false;
                     break;
                  }
               }
               if(flag){
                  if(p=='B'){
                     fB=false;
                     winner+=2;
                  }
                  else{
                     fR=false;
                     winner+=1;
                  }
                  continue;
               }
            }
         }
         if(n-j>=k){
            flag=true;
            near=j+k;
            for(int q=j+1;q<near;q++){
               if(rotate[i][q]!=p){
                  flag=false;
                  break;
               }
            }
            if(flag){
               if(p=='B'){
                  fB=false;
                  winner+=2;
               }
               else{
                  fR=false;
                  winner+=1;
               }
               continue;
            }
         }
      }
   }
}

int main(void){
   freopen("rl.in","r",stdin);
   freopen("rl.out","w",stdout);
   int T;
   scanf("%d",&T);
   for(int t=0;t<T;t++){
      winner=0;
      scanf("%d %d",&n,&k);
      for(int i=0;i<n;i++){
         scanf("%s",&board[i]);
      }
      for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
            rotate[i][j]='.';
         }
      }
      for(int i=0;i<n;i++){
         int jr=0;
         for(int j=n-1;j>=0;j--){
            if(board[i][j]!='.'){
               rotate[i][jr++]=board[i][j];
            }
         }
      }
      findWinner();
      if(winner==0)
         printf("Case #%d: Neither\n",t+1);
      else if(winner==1)
         printf("Case #%d: Red\n",t+1);
      else if(winner==2)
         printf("Case #%d: Blue\n",t+1);
      else if(winner==3)
         printf("Case #%d: Both\n",t+1);
   }
   return 0;
}
