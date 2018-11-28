#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <cmath>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;
int Q,N;
int tab[110][110];
double val[110][4];
char buf[150];
int main(){
  scanf("%d",&Q);
  for(int q=1;q<=Q;q++){
    printf("Case #%d:\n",q);
    scanf("%d",&N);
    for(int i=0;i<N;i++){
      for(int j=0;j<4;j++)       val[i][j]=0;
      scanf("%s",buf);
      for(int j=0;j<N;j++){
        switch(buf[j]){
          case '1':
               val[i][0]++;
               val[i][3]++;
               tab[i][j]=1;
               break;
          case '0':
               tab[i][j]=0;
               val[i][3]++;
               break;
          case '.':
               tab[i][j]=-1;
        }
      }
    }
    for(int i=0;i<N;i++){
      for(int j=0;j<N;j++){
        if (i!=j && (tab[i][j]!=-1))
        val[i][1]+=(val[j][0]-(tab[i][j]==0))/(val[j][3]-(tab[i][j]!=-1));
        //printf("%d %d %llf\n",i,j,val[i][1]);
      }
    }
    for(int i=0;i<N;i++)
      for(int j=0;j<N;j++)
        if((i!=j) && (tab[i][j]!=-1))
          val[i][2]+=val[j][1]/val[j][3];
        
    for(int i=0;i<N;i++)
      //printf("%llf %llf %llf %llf\n ",val[i][0],val[i][1],val[i][2],val[i][3]);
      printf("%.9Lf\n",val[i][0]/(val[i][3]*4)+val[i][1]/(val[i][3]*2)+val[i][2]/(val[i][3]*4));

  }
}
