#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <list>
#include <numeric>
#include <sstream>
#include <functional>
#include <utility>

#define INFINITO  (1<<30)

using namespace std;

int T,N,M,A[102][102],vis[102][102],actualX,actualY;
int pivote,newX,newY,repos;
int dx[]={-1, 0, 0, 1};
int dy[]={ 0,-1, 1, 0};


int main(){

  scanf("%d",&T);
  
   for(int caso=1;caso<=T;caso++){
       
      scanf("%d%d",&N,&M);
      
      for(int i=0;i<N;i++)
       for(int j=0;j<M;j++)
        scanf("%d",&A[i][j]);  
       
        memset(vis,-1,sizeof(vis));
        repos = 0;
       
        for(int i=0;i<N;i++){
          for(int j=0;j<M;j++){
            if( vis[i][j]!=-1) continue;           
            
            vector<int> listaX,listaY;
             listaX.push_back(i);
             listaY.push_back(j);
             actualX = i; actualY = j;
             pivote = A[actualX][actualY];
             
                 while(1){
                      
                   for(int k=0;k<4;k++)
                     if( actualX + dx[k]>=0 && actualX+dx[k]<N &&                              
                         actualY + dy[k]>=0 && actualY+dy[k]<M && 
                         A[actualX+dx[k]][actualY+dy[k]] < pivote){
                          
                           pivote = A[actualX+dx[k]][actualY+dy[k]];
                           newX = actualX+dx[k];
                           newY = actualY+dy[k];
                         } 
                   
                       if( pivote == A[actualX][actualY] ){
                          for(int k=0;k<listaX.size();k++) vis[listaX[k]][listaY[k]] = repos;
                          repos++;
                          break;
                       }
                       else{
                          actualX = newX; actualY = newY;
                          pivote = A[actualX][actualY];
                          listaX.push_back(actualX);
                          listaY.push_back(actualY);
                            if( vis[actualX][actualY]!=-1){
                              for(int k=0;k<listaX.size();k++) vis[listaX[k]][listaY[k]] = vis[actualX][actualY];
                               break;
                            }
                      }                                                       
            
                 }
              
                     
          }
        }     
    printf("Case #%d:\n",caso);
    int llego[30];
    memset(llego,-1,sizeof(llego));
    int x = 0;
    
        for(int i=0;i<N;i++){
          for(int j=0;j<M;j++){
             if(j) printf(" ");
             if(llego[vis[i][j]]==-1) printf("%c",'a'+x),llego[vis[i][j]]=x,x++; 
             else printf("%c",'a'+llego[vis[i][j]]);
          } 
         puts("");
        }
    
   }
}

