#include <cstdio>
using namespace std;

int A[31];

void initA()
{
  A[0] = 0;
  for (int i = 0; i < 30; ++i)
    A[i + 1] = 2 * A[i] + 1;
}

bool f(int N, int K)
{
  return !((K + 1) % (A[N] + 1));
}

int main()
{
  initA();

  int T;
  scanf(" %d", &T);
  for (int i = 1; i <= T; ++i) {
    int N, K;
    scanf(" %d %d", &N, &K);
    printf("Case #%d: %s\n", i, f(N, K) ? "ON" : "OFF");
  }

  return 0;
}
