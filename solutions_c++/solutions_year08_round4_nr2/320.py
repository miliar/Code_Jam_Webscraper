#include <cstdio>
#include <cstdlib>
#define min(a, b) (a < b ? a : b)
using namespace std;

int main() {
  int C, N, M, A;
  scanf("%d", &C);
  for (int cnum = 1; cnum <= C; cnum++) {
    scanf("%d%d%d", &N, &M, &A);
    bool done = false;
    for (int x1 = 0; x1 <= N && !done; x1++) {
      for (int y2 = -M; y2 <= M && !done; y2++) {
	int target = x1*y2 - A;
	for (int x2 = 0; x2 <= N && !done; x2++) {
	  if ((x2 == 0 && target != 0) || (x2 != 0 && target%x2 != 0)) {
	    continue;
	  }
	  for (int y1 = -M; y1 <= M && !done; y1++) {
	    if (x2*y1 == target && abs(y2-y1) <= M) {
	      int miny = min(min(y1, y2), 0);
	      y1 -= miny;
	      y2 -= miny;
	      printf("Case #%d: ", cnum);
	      printf("%d %d %d %d %d %d\n", 0, -miny, x1, y1, x2, y2);
	      done = true;
	    }
	  }
	}
      }
    }
    if (!done) {
      printf("Case #%d: IMPOSSIBLE\n", cnum);
    }

  }
  return 0;
}
