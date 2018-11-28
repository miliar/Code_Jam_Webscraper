#include <sstream>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
// for do 0 ateh n, exclusive
#define FOR( i , n ) for (int i = 0; i < n ; i++ )
int H,W;

int tab[105][105];
int g[105][105];
int cur;
int calc(int a, int b){
    int h[4];
    if (g[a][b]!=-1) return g[a][b];
    h[0]=tab[a-1][b];
    h[1]=tab[a][b-1];
    h[2]=tab[a][b+1];
    h[3]=tab[a+1][b];
    int mini = h[0];
    FOR(i,4)
      if(h[i]<mini) mini=h[i];
    if(mini>=tab[a][b])
      return g[a][b]= cur++;
    if(h[0]==mini)
    return g[a][b] = calc(a-1,b);
    if(h[1]==mini)
    return g[a][b] = calc(a,b-1);
    if(h[2]==mini)
    return g[a][b] = calc(a,b+1);
    if(h[3]==mini)
    return g[a][b] = calc(a+1,b);
}

int main() {
int T;
cin>>T;
  FOR(cas,T){
           cin>>H>>W;
           FOR(h,H+2)
             tab[h][0]=tab[h][W+1]=1000000;             
           FOR(w,W+2)
             tab[0][w]=tab[H+1][w]=1000000;    
           FOR(h,H+2)
            FOR(w,W+2)
             g[h][w]=-1;
           FOR(h,H)
             FOR(w,W)
              cin>>tab[h+1][w+1];
           cur=0;
           FOR(h,H)
             FOR(w,W)
               calc(h+1,w+1);
           char cl[27];
           char ccur = 'a';
           FOR(i,27) cl[i]='.';

           FOR(h,H)
             FOR(w,W)
               if(cl[g[h+1][w+1]]=='.')
                 cl[g[h+1][w+1]] = ccur++;
                                    
           cout<<"Case #"<<cas+1<<":"<<endl;
           FOR(h,H){
             FOR(w,W)
               {
               if(w>0)cout<<" ";
               cout<<cl[g[h+1][w+1]];
               }
             cout<<endl;
             }

           }



return 0;
}
