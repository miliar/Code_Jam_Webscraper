#include <stdio.h>

int T;

int N,S,p,t;

int main() {
  scanf("%d", &T);
  for (int tc = 1; tc<=T;++tc) {
    scanf("%d %d %d", &N, &S, &p);
    int ans = 0;
    for (int i=0;i<N;++i) {
      scanf("%d", &t);
      if (t % 3 && t/3 + 1 >= p || t % 3 == 0 && t/3 >= p) ++ans;
      else if (S > 0) {
	if (t % 3 == 0 && t/3 == p-1 && p>= 2 || t % 3 == 2 && t/3 == p-2 && p>=2) { --S; ++ans; }
      }
    }
    printf("Case #%d: %d\n", tc, ans);
  }
  return 0;
}
