#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAXN 100
#define MAXK 5000
int indices[MAXN], K;
int main() {
  int no_cases;
  cin >> no_cases;
  for (int rr = 1; rr <= no_cases; ++rr) {
    int vals[MAXK], taken[MAXK], at = 0, c = 0, need = 1, n;
    cin >> K >> n;
    for (int i = 0; i < n; ++i)
      cin >> indices[i];
    memset(taken, 0, sizeof(taken));
    while(need <= K) {
      if (!taken[at]) {
	++c;
	if (c == need)
	  c = 0, vals[at] = need++, taken[at] = 1;
      }
      at = (at + 1) % K;
    }
    printf("Case #%d:", rr);
    for (int i = 0; i < n; ++i)
      printf(" %d", vals[indices[i]-1]);
    printf("\n");
  }
  return 0;
}
