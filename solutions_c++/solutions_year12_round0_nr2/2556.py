#include <cstdio>
#include <algorithm>

int main()
{
  int T;
  scanf("%d", &T);
  for(int cs=1; cs<=T; ++cs) {
    int N, S, p;
    scanf("%d%d%d", &N, &S, &p);
    int x1=std::max(0, p-1)*2+p;
    int x2=std::max(0, p-2)*2+p;
    int score = 0;
    for(int i=0; i<N; ++i) {
      int y;
      scanf("%d", &y);
      if(x1 <= y)
	++score;
      else if(S && x2 <= y) {
	--S;
	++score;
      }
    }
    printf("Case #%d: %d\n", cs, score);
  }
  return 0;
}
