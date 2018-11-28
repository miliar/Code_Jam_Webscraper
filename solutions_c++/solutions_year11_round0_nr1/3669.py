#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define ABS(X) ((X) >= 0 ? (X) : -(X))
int main()
{
  int T;
  scanf("%d", &T);
  for(int cas = 1 ; cas <= T ; cas ++) {
    int ans = 0, N, opos = 1, otime = 0, bpos = 1, btime = 0, button;
    char color;

    scanf("%d", &N);
    while(N --) {
      scanf(" %c %d", &color, &button);
      if(color == 'O') {
        ans += (1 + max(0, ABS(button - opos) - (ans - otime)));
        opos = button, otime = ans;
      }
      else {
        ans += (1 + max(0, ABS(button - bpos) - (ans - btime)));
        bpos = button, btime = ans;
      }
    }

    printf("Case #%d: %d\n", cas, ans);
  }
}
