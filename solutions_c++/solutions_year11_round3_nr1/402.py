#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#define ii pair<int,int>

using namespace std;

int main()
{
   int t;
   cin>>t;
   for(int it=0;it<t;it++){
      int h,w;
      cin>>h>>w;
      string map[h];
      for(int i=0;i<h;i++)
         cin>>map[i];
      int nb=0;
      for(int i=0;i<h;i++){
         for(int j=0;j<w;j++){
            if(map[i][j]=='#')
               nb++;
         }
      }
      
      for(int i=0;i<h-1;i++){
         for(int j=0;j<w-1;j++){
            if(map[i][j]=='#' && map[i+1][j]=='#' && map[i][j+1]=='#' && map[i+1][j+1]=='#'){
               nb-=4;
               map[i][j]='/';
               map[i+1][j]='\\';
               map[i][j+1]='\\';
               map[i+1][j+1]='/';
            }
            
         }
      }    
      cout<<"Case #"<<(it+1)<<":"<<endl;
      if(nb){
          cout<<"Impossible"<<endl;
      }else{
         for(int i=0;i<h;i++)
            cout<<map[i]<<endl;
      }
     
   }
     return 0;
}
