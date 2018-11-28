#include<cstdio>
#include <iostream>
#include<algorithm>
using namespace std;

char flr[60][60];

int main(){
   int t,m,n;
   cin>>t;
   for (int z=0; z<t; z++){
       cin>>m>>n;
       for (int y=0; y<m;y++){
           for (int x=0; x<n;x++)
               cin>>flr[y][x];
       }
       for (int y=0; y<m;y++){
           for (int x=0; x<n;x++){
               if (flr[y][x]=='#' && flr[y][x+1]=='#' && flr[y+1][x+1]=='#' && flr[y+1][x]=='#'){
                      flr[y][x]='/';
                      flr[y][x+1]='\\';
                      flr[y+1][x+1]='/';
                      flr[y+1][x]='\\';
               }
           }
       }
       printf("Case #%d:\n",z+1);
       bool ok=1;
       for (int y=0; y<m;y++)
           for (int x=0; x<n;x++)
               if (flr[y][x]=='#'){
                   ok=0;
               }
       if (!ok)
         cout<<"Impossible"<<endl;
       else
         for (int y=0; y<m;y++){
           for (int x=0; x<n;x++)
                cout<<flr[y][x];
           cout<<endl;
         }
   }
}
