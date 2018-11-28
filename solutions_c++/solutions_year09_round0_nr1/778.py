#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<math.h>
#include<cstdlib>
#include<string>
using namespace std;

int chars,words,tests;
char W[5005][30];
char str[10000000];
bool has[50][200];

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
   int i,j,k,g;
   scanf("%d%d%d",&chars,&words,&tests);
   for(i=0;i<words;i++)scanf("%s",W[i]);

   for(i=0;i<tests;i++){
      memset(has,0,sizeof(has));
      scanf("%s",str);
      g=0;
      for(j=0;j<strlen(str);j++){
         if( str[j]=='(' ){
            j++;
            while( str[j]!=')' )has[g][ str[j]-'a' ] = true,j++;
            g++;
         }else{
            has[g++][ str[j]-'a' ] = true;
         }
      }

      int sol = 0;
      for(j=0;j<words;j++){
         int len = strlen(W[j]);
         bool ok = true;
         for(k=0;k<len && ok;k++)ok = has[k][ W[j][k]-'a' ];
         sol += ok;
      }
      
      printf("Case #%d: %d\n",i+1,sol);
   }
   return 0;
}
