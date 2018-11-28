// welcome to code jam
// w e l c o m t d j a 
// a c d e j l m o t w ' '
#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<math.h>
using namespace std;

string str;
char sfind[] = "welcome to code jam\0";
int DP[600],mDP[600];

int main(){
   int tests,i,j;
   freopen("Ulaz.txt","r",stdin);
   freopen("Izlaz.txt","w",stdout);
   cin>>tests>>ws;
   for( int t = 1 ; t<=tests;t++){
      memset(DP,0,sizeof(DP));
      getline(cin,str);
      int lens = strlen(sfind) , len = str.size();
      int cnt = 0;
      for( i=0 ; i < len ; i++ ){
         if( str[i] == 'w' )cnt++;
         DP[i] = cnt;
      }
      for( i=1 ; i < lens ; i++ ){
         cnt = 0;
         for( j = 0 ; j < len ; j ++ ){
            if( str[j] == sfind[i] )
               cnt = (cnt+DP[j-1])%10000;
            mDP[j] = cnt;
         }
         for( j = 0 ; j < len ; j ++ )DP[j] = mDP[j];
      }
      printf("Case #%d: %.4d\n",t,DP[ len-1] );
   }
   return 0;
}
