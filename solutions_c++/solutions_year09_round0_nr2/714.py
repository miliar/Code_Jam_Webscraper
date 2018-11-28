#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 

int M[105][105];
char ind;
char mem[105][105];
int moves[][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int H,W;
char go(int x,int y){
   if(mem[x][y]!='6') return mem[x][y];
   int at = M[x][y];
   int indi = -1;
   FOR(i,0,4){
      int xp = x+moves[i][0];
      int yp = y+moves[i][1];
      if(xp<0 || yp<0 || xp>=H || yp>=W) continue;
      if(M[xp][yp]<at){
         indi = i;
         at = M[xp][yp];
      }
   }
   if(indi==-1){
      mem[x][y] = ind;
      ind++;
      return mem[x][y];
   }
   else return mem[x][y] = go(x+moves[indi][0],y+moves[indi][1]);
}

int main(){
   int T;scanf("%d",&T);
   FORE(t,1,T){
      scanf("%d%d",&H,&W);
      FOR(i,0,H){
         FOR(j,0,W) scanf("%d",&M[i][j]);
      }      
      ind = 'a';
      FOR(i,0,H) FOR(j,0,W) mem[i][j] = '6';
         
      printf("Case #%d:\n",t);
      FOR(i,0,H){
         FOR(j,0,W) printf("%c ",go(i,j));
         printf("\n");
      }
   }

}
