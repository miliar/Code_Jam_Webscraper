#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <cmath>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;
int Q;
int N,C,L;

int dist[1024000][2];
long long T,sta,stao,res;
int main(){
  scanf("%d",&Q);
  for(int q=1;q<=Q;q++){
    scanf("%d %lld %d %d",&L,&T,&N,&C);
    for(int i=0;i<C;i++){
      scanf("%d",&dist[i][0]);
      dist[i][1]=0;
      }
    dist[C][0]=0;
    dist[C][1]=0;
    sta=0;
    for(int i=0;i<N;i++){ 
      stao=sta;
      if (sta>=T) dist[i%C][1]++;
      sta+=2*dist[(i)%C][0];
      if (stao<T && sta>=T){
      dist[C][0]=(sta-T)/2;
      dist[C][1]=1;}
    }
    res=sta;
    for(int i=0;i<C;i++)
    for(int j=i+1;j<=C;j++){
      if (dist[i][0]<dist[j][0]){
         int t1=dist[i][0],t2=dist[i][1];
         dist[i][0]=dist[j][0];         
         dist[i][1]=dist[j][1];
         dist[j][0]=t1;         
         dist[j][1]=t2;         
      }
    }
    //for(int i=0;i<=C;i++) printf("%d %d\n",dist[i][0],dist[i][1]);
    int it=0;
    while(L>0 && it<=C){
      if (L<dist[it][1]){
         res-=L*dist[it][0];
         L=0;
      }
      else{
        L-=dist[it][1];
        res-=dist[it][0]*dist[it][1];
      }
      it++;
    }
   printf("Case #%d: %lld\n",q,res);
  }
}
