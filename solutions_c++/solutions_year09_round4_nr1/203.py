#undef DEBUG

#ifdef DEBUG
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...) do ; while(0)
#define NDEBUG
#endif

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

int main ()
{
  int N;

  scanf("%d\n", &N);
  for (int test=1; test<=N; test++) {
    // input
    int n;
    scanf("%d\n", &n);
    char row[n][n];
    char min[n];
    for (int i=0; i<n; i++)
      scanf("%s\n", row[i]);
    // calculate
    for (int i=0; i<n; i++) {
      min[i]=0;
      for (int j=n-1; j>=0; j--)
        if (row[i][j] == '1') {
          min[i]=j;
          break;
        }
      debug("min[%d]=%d\n", i, min[i]);
    }
    int answer=0;
    for (int i=0; i<n; i++) {
      int j;
      for (j=i; j<n; j++)
        if (min[j]<=i)
          break;
      assert(j<n);
      debug("put %d in %d: +%d\n", j, i, j-i);
      answer+=j-i;
      for (int k=j-1; k>=i; k--)
        min[k+1]=min[k];
    }
    // answer
    printf("Case #%d: %d\n", test, answer);
  }
  return 0;
}
