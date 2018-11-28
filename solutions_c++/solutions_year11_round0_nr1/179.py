#define _ABS(x) (((x)>0)?(x):(-(x)))

#include <stdio.h>

int T;
int N;

int main() {

  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%d", &N);
    int pb = 1, po = 1;
    int tb = 0, to = 0;
    int t = 0;
    int pos = 0;
    char p = 0;
    for (int i=0;i<N;++i) {
      scanf(" %c %d",&p,&pos);
      if (p == 'B') {
	if (t - tb < _ABS(pos-pb)) {
	  t += _ABS(pos-pb)-(t-tb);
	}
	tb = t + 1;
	pb = pos;
      } else if (p == 'O') {
	if (t - to < _ABS(pos-po)) {
	  t += _ABS(pos-po)-(t-to);
	}
	to = t + 1;
	po = pos;
      }
      ++t;
    }
    printf("Case #%d: %d\n", TT, t);
  }
  return 0;
}
