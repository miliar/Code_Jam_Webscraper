#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

int main(){
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int N;
    scanf("%d", &N);
    int oPos = 1, bPos = 1;
    int oTime = 0, bTime = 0;
    int time = 1;
    for(int i = 0; i < N; i++) {
      char c[100];
      int pos;
      scanf("%s%d", c, &pos);
      if(c[0] == 'O') {
        oTime = time = max(time, oTime + abs(oPos-pos) + 1);
        oPos = pos;
        //        printf("O %d %d\n", oTime, oPos);
      } else {
        bTime = time = max(time, bTime + abs(bPos-pos) + 1);
        bPos = pos;
        //        printf("B %d %d\n", bTime, bPos);
      }
      time ++;
    }

    printf("Case #%d: %d\n", t, time-1);
  }

}
