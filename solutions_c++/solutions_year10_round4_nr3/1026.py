#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <climits>
#include <sstream>

using namespace std;

#define MAXN 104
int M[2][MAXN][MAXN];
int t,r;

bool notall(int idx){
   for(int i=0;i<MAXN;++i)
    for(int j=0;j<MAXN;++j)
     if(M[idx][i][j]==1) return false;
   return true;
  
}

void generate(){
  
 
  for(int i=1;i<MAXN;++i)
   for(int j=1;j<MAXN;++j) {
    if(M[0][i-1][j]==0 && M[0][i][j-1]==0) M[1][i][j]=0;
    else if(M[0][i-1][j]==1 && M[0][i][j-1]==1) M[1][i][j]=1;
    else M[1][i][j]=M[0][i][j];
  }

}

int main(){
  
  freopen("C-small-attempt0.in","r",stdin);
  freopen("out.txt","w",stdout);
  
  scanf("%d",&t);
  int z=0;
  while(t--){
    scanf("%d",&r);
  
    ++z;
    memset(M,0,sizeof(M));
    
    for(int i=0;i<r;++i){
      int x1,x2,y1,y2; scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
      if(x1>x2) swap(x1,x2); if(y1>y2) swap(y1,y2);
     
      for(int j=x1;j<=x2;++j)
       for(int k=y1;k<=y2;++k)
        M[0][j][k]=1;
    }
    
    
    int tm=0;
    while(notall(0)==false){
      
      generate();
      memcpy(M[0],M[1],sizeof(M[1]));
      ++tm;
    }
    printf("Case #%d: %d\n",z,tm);
  }
  
  return 0;
}
  
  

