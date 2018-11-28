#include <cstdio>
#include <algorithm>

using namespace std;

int T, N;

int main(){
  scanf("%d", &T);

  for (int ttt=1; ttt<=T; ttt++){
    scanf("%d", &N);

    int left[2]={0,0};
    int tar,time=0;
    int pos[2]={1,1};
    char rob;

    for (int i=0; i<N; i++){
      scanf(" %c %d", &rob, &tar);
      int t = (rob=='O');
      int o = !t;
      int dt=max(1, abs(tar-pos[t])-left[t]+1);
      pos[t]=tar;
      left[o]+=dt;
      time += dt;
      left[t]=0;
    }
    
    printf("Case #%d: %d\n", ttt, time);
  }
}
