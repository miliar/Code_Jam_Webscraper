#include <stdio.h>

int N,L,H;
int nums[10001];

int main() {
  int T;
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%d %d %d\n", &N, &L, &H);
    for (int i=0;i<N;++i)
      scanf("%d", &nums[i]);
    bool hassol = false;
    int t=L;
    for (t=L;t<=H;++t) {
      hassol = true;
      for (int i=0;i<N;++i) {
	if (nums[i] % t != 0 && t % nums[i] != 0) {
	  hassol = false;
	  break;
	}
      }
      if (hassol) break;
    }
    if (hassol) printf("Case #%d: %d\n", TT, t);
    else printf("Case #%d: NO\n", TT);
  }
  return 0;
}
