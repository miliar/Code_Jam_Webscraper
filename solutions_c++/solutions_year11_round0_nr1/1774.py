#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main() {
  int nCases, n, x;
  int pos[2], time[2];
  char c;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d", &n);
    pos[0] = pos[1] = 1;
    time[0] = time[1] = 0;
    for (int i = 0; i < n; i++) {
      scanf(" %c%d\n", &c, &x);
      int j = (c == 'O');
      time[j] = max(time[j] + abs(pos[j] - x) + 1, time[1 - j] + 1);
      pos[j] = x;
    }
    printf("Case #%i: %i\n", iCase, max(time[0], time[1]));
  }
  return 0;
}
