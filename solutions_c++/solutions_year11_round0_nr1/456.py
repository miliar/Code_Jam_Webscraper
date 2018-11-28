#include<cstdio>
#include<cmath>
#include<algorithm>
#include<numeric>
using namespace std;
int t,n;
main(){
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    scanf("%d",&n);
    int pos[2]={1,1},time=0,last[2]={};
    while(n--){
      char side;
      int nr;
      scanf(" %c %d",&side,&nr);
      int which=side=='O';
      int dist=abs(pos[which]-nr),bonus=time-last[which];
      bonus=min(bonus,dist);
      dist-=bonus;
      time+=dist;
      last[which]=++time;
      pos[which]=nr;
    }
    printf("Case #%d: %d\n",tt,time);
  }
}

