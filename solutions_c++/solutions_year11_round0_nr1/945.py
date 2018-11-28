#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <algorithm>



int main() {


  int kases;
  scanf("%d", &kases);

  for (int i = 0; i < kases; ++i) {
    int n;
    scanf("%d", &n);
    int pb = 1, tb = 0;
    int po = 1, to = 0;
    for (int j = 0; j < n; ++j) {
      char buf[1024];
      int pos;
      scanf("%s", buf);
      scanf("%d", &pos);
      switch (buf[0]) {
      case 'O':
	to = 1 + std::max(tb, to + abs(pos - po));
	po = pos;
	break;
      case 'B':
	tb = 1 + std::max(to, tb + abs(pos - pb));
	pb = pos;
	break;
      default:
	assert(false);
      };
    }
    printf("Case #%d: %d\n", 1+i, std::max(to, tb));
  }


  return(0);
}
