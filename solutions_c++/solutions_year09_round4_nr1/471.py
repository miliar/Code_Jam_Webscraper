#include <stdio.h>
#include <algorithm>
using namespace std;

int N;
int L[100][2];

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    printf("Case #%d: ", tc);
    int N;
    scanf("%d", &N);
    for (int i = 1; i <= N; i++) {
      char buf[100];
      scanf("%s", buf);
      L[i][0] = i;
      L[i][1] = 0;
      for (int j = N-1; j >= 0; j--) if (buf[j] == '1') { 
        L[i][1] = j+1;
        break;
      }
    }

    int R = 0;
    for (int i = 1; i <= N; i++) {
      int mi = -1;
      int movement = 1234567890;
      for (int j = 1; j <= N; j++) {
        if (L[j][0] >= i && L[j][1] <= i && movement > L[j][0]) {
          movement = L[j][0];
          mi = j;
        }
      }
      if (mi == -1) continue;
      int t = movement - i;
      for (int j = 1; j <= N; j++) if (i <= L[j][0] && L[j][0] < movement) L[j][0]++;
      L[mi][0] = i;
      R += t;
    }

    printf("%d\n", R);
  }
  return 0;
}
