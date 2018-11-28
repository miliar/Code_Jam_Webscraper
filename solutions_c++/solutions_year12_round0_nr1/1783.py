/**********************************************************************************/
/*  Problem: d550 "ª«¥ó±Æ§Ç" from Sort                                        */
/*  Language: CPP (781 Bytes)                                                     */
/*  Result: AC judge by zeroserver@ZeroJudge                                      */
/*  Author: pcsh810793 at 2010-06-22 19:13:03                                     */
/**********************************************************************************/


#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

int i,j;

struct abc{
int p[200];
}a[10000];

bool st(abc x,abc y){
   for(i=0; ;i++){
   if(x.p[i] != y.p[i])
   return x.p[i] < y.p[i];
   }
}

int input(){
char a;
int b=0;
   while(a = getchar())
     if(a!= ' ' && a!= '\n') break;
   b = a-48;
   while(a = getchar()){
   if(a == ' ' || a == '\n') break;
   b = b*10+a-48;
   }
   return b;
}

int main(){
int n,m;
   while(~scanf("%d%d",&n,&m)){
       for(i=0;i<n;i++){
          for(j=0;j<m;j++){
          a[i].p[j] = input();
          }
       }   
       sort(a , a+n , st);
       for(i=0;i<n;i++){
          for(j=0;j<m;j++){
          printf("%d " , a[i].p[j]);
          }
          printf("\n");
       }
   }
}
