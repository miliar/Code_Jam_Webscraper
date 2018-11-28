#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
  int t, n;
  int bPos, oPos, pos;
  int bTime, oTime, time;
  char robot;
  
  scanf("%d", &t);
  for (int i=1; i<=t; i++) {
    scanf("%d", &n);
    bPos = oPos = 1;
    bTime = oTime = time = 0;
    
    for (int j=1; j<=n; j++) {
      scanf(" %c %d", &robot, &pos);
      if (robot == 'B') {
        bTime = time = max(time, bTime + abs(pos - bPos)) + 1;
	bPos = pos;
      } else { /* robot == 'O' */
        oTime = time = max(time, oTime + abs(pos - oPos)) + 1;
	oPos = pos;
      }
      // printf("time = %d; O = %d [%d], B = %d [%d]\n", time, oPos, oTime, bPos, bTime);
    }
    
    printf("Case #%d: %d\n", i, time);
  }
  
  return 0;
}
