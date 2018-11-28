#include <cstdio>
#include <cstdlib>
#include <algorithm>

int main()
{
  int T;
  scanf("%d", &T);
  for(int cases=1; cases<=T; ++cases) {
    int pO=1, pB=1;
    int tO=0, tB=0;
    int N;
    scanf("%d", &N);
    for(int i=0; i<N; ++i) {
      char R;
      int P;
      scanf(" %c%d", &R, &P);
      if('O'==R) {
	tO += abs(pO-P);
	tO = std::max(tO, tB)+1;
	pO = P;
      } else {
	tB += abs(pB-P);
	tB = std::max(tO, tB)+1;
	pB = P;
      }
    }
    printf("Case #%d: %d\n", cases, std::max(tO, tB));
  }
  return 0;
}
