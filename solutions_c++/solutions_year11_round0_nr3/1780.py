#include <cstdio>
#include <climits>
#include <algorithm>

using namespace std;

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    int n, x, numSum = 0, numXor = 0, numMin = INT_MAX;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%d", &x);
      numSum += x;
      numXor ^= x;
      numMin = min(numMin, x);
    }
    printf("Case #%i: ", iCase);
    if (numXor)
      printf("NO\n");
    else
      printf("%i\n", numSum - numMin);
  }
  return 0;
}
