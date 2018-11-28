#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;

int ab(int x) { return x < 0 ? -x : x; }


int main()
{
  int t;
  scanf("%d", &t);
  
  char op[5];
  int pos, p1, p2, t1, t2;
  for (int l = 1; l <= t; ++l) {
    printf("Case #%d: ", l);
    p1 = p2 = 1;
    t1 = t2 = 0;
    
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%s%d", op, &pos);
      if (op[0] == 'O') {
	t1 += ab(p1-pos);
	t1 = max(t1, t2)+1;
	p1 = pos;
      } else {
	t2 += ab(p2-pos);
	t2 = max(t1, t2)+1;
	p2 = pos;
      }
    }

    printf("%d\n", max(t1, t2));
  }
  return 0;
}
