#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int cases;
  scanf("%d", &cases);
  char S[123456];
  for (int C = 1; C <= cases; C++) {
    int k;
    scanf("%d %s", &k, S);
    int tab[11];
    int res = 123456;
    for (int i = 0; i < k; i++) tab[i] = i;
    do {
      char S2[123456];
      for (int i = 0; S[i] != '\0'; i++) {
        int a = i / k;
        int b = i % k;
        S2[i] = S[a*k + tab[b]];
      }
      int cur = 0;
      char last = '?';
      for (int i = 0; S[i] != '\0'; i++) {
        if (S2[i] == last) continue;
        cur++;
        last = S2[i];
      }
      res = min(res, cur);
    } while (next_permutation(tab, tab+k));
    printf("Case #%d: %d\n", C, res);
  }
}
