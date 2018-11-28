#include <cstdio>
#include <cstdlib>
#include <stack>
#include <map>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool interset(int a1, int b1, int a2, int b2)
{
  int upper = a1- a2;
  int lower = b2-a2-b1+a1;

  if (lower == 0) {
    return false;
  }
  double x = (double)upper/(double)lower;
  return ((x>=0) && (x<=1));
}

int main(int argc, const char *argv[])
{
  int T; //Number of cases

  scanf("%d\n", &T);

  for (int t = 0; t < T; t++) {
    int result = 0;
    int N = 0;  // the number of wires you see.

    scanf("%d\n", &N);

    int A[N]; //the height of the window on the left building
    int B[N]; //the height of the window on the right building

    for (int n = 0; n < N; n++) {
      scanf("%d %d\n", &A[n], &B[n]);
    }

    for (int n = 0; n < N; n++) {
      for (int n2 = 0; n2 < n; n2++) {
        if (n == n2) {
          continue;
        }

        if (interset(A[n], B[n], A[n2], B[n2])) {
          result++;
        }
      }
    }


    printf("Case #%d: %d\n", t+1, result);
  }

  return 0;
}
