#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int Tn = 1; Tn <= T; Tn++) {
    int N, S, P;
    scanf("%d%d%d", &N, &S, &P);
    int how[40];
    for (int i = 0; i < 40; i++) how[i] = 0;
    for (int a = 0; a <= 10; a++) {
      for (int b = 0; b <= 10; b++) {
        for (int c = 0; c <= 10; c++) {
          int abcmin = min(a, min(b, c));
          int abcmax = max(a, max(b, c));
          if (abcmax-abcmin > 2) continue;
          if (abcmax < P) continue;
          if (abcmax-abcmin == 2) how[a+b+c] = max(how[a+b+c], 1);
          if (abcmax-abcmin < 2)  how[a+b+c] = max(how[a+b+c], 2);
        }
      }
    }
    //for (int i = 0; i <= 30; i++) printf("how[%d] = %d\t", i, how[i]);
    int over = 0;
    int surp = 0;
    for (int i = 0; i < N; i++) {
      int g;
      scanf("%d", &g);
      if (how[g] == 2) over++;
      if (how[g] == 1) surp++;
    }
    printf("Case #%d: %d\n", Tn, over + min(surp, S));
  }
  return 0;
}
