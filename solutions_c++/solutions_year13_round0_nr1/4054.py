#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <utility>
#include <set>
#include <map>
#include <bitset>
#include <iostream>
#include <ctype.h>

#define gc getchar  //unlocked linux
#define MOD 1000000007
#define INF numeric_limits<int>::max();
#define FOR(i,v,n) for(i=v;i<n;i++)
#define scan(i) scanf(" %d",&i)
#define print(i) printf("%d\n",i);
#define pb push_back 
#define sz(i) i.size()
#define reset(vec) memset(vec,0,sizeof(vec))
#define ord(vec) sort(vec.begin(),vec.end())
#define rev(vec) reverse(vec.begin(),vec.end())
#define MAX 55

using namespace std;

inline void scanint(int &x){
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int cmp_double(double a, double b, double eps = 1e-9){
    return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

int main(){
    int t,i,j,end;
    char tab[10][10];
    int xlin[4],xcol[4],xdiag[2];
    int ylin[4],ycol[4],ydiag[2];
    int dots,casos=1;
    scan(t);
    while(t--){
       FOR(i,0,4){
          scanf(" %s",&tab[i]);   
          xlin[i]=0; ylin[i]=0;
          xcol[i]=0; ycol[i]=0;
          xdiag[i]=0; ydiag[i]=0;        
       }
       dots=0;
       end=0;
       FOR(i,0,4){
          FOR(j,0,4){
              if (tab[i][j]=='X'){
                  xlin[i]++;                    
                  xcol[j]++;
                  if (i==j)
                     xdiag[0]++;          
                  if (i==0 && j==3 || i==1 && j==2 || i==2 && j==1 || i==3 && j==0)
                     xdiag[1]++;                 
              }else if (tab[i][j]=='O'){
                  ylin[i]++;                    
                  ycol[j]++;
                  if (i==j)
                     ydiag[0]++;          
                  if (i==0 && j==3 || i==1 && j==2 || i==2 && j==1 || i==3 && j==0)
                     ydiag[1]++;        
              }else if (tab[i][j]=='T'){
                  xlin[i]++;                    
                  xcol[j]++;
                  if (i==j)
                     xdiag[0]++;          
                  if (i==0 && j==3 || i==1 && j==2 || i==2 && j==1 || i==3 && j==0)
                     xdiag[1]++;          
                  ylin[i]++;                    
                  ycol[j]++;
                  if (i==j)
                     ydiag[0]++;          
                  if (i==0 && j==3 || i==1 && j==2 || i==2 && j==1 || i==3 && j==0)
                     ydiag[1]++;    
              }else if (tab[i][j]=='.')
                   dots++;       
                     
          }                  
       }
       printf("Case #%d: ",casos++);
       FOR(i,0,4){
          if (xlin[i]==4 || xcol[i]==4){
              end=1;
              printf("X won\n");
              break;           
          }           
       }
       if (end)
          continue;
       if (xdiag[0]==4 || xdiag[1]==4){
           printf("X won\n");            
           continue;            
       }
       FOR(i,0,4){      
          if (ylin[i]==4 || ycol[i]==4){
              end=1;
              printf("O won\n");
              break;           
          }           
       }
       if (end)
          continue;
       if (ydiag[0]==4 || ydiag[1]==4){
           printf("O won\n");            
           continue;            
       }
       if (dots==0){
           printf("Draw\n");         
       }else{
           printf("Game has not completed\n");   
       }   
       
    }
    
    
    
    return 0;
}




