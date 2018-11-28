#include <cstdio>
using namespace std;

int A[1000], B[1000];

long long f()
{
  int R, k, N, G[1000];
  scanf(" %d %d %d", &R, &k, &N);
  for (int i = 0; i < N; ++i)
    scanf(" %d", &G[i]);

  for (int i = 0; i < N; ++i) {
    A[i] = B[i] = 0;
    for (int j = i; j < N + i; ++j) {
      if (A[i] + G[j % N] <= k) {
	A[i] += G[j % N];
	B[i]++;
      } else {
	break;
      }
    }
  }

  int p = 0;
  long long amt = 0;
  while (R--) {
    amt += A[p];
    p = (p + B[p]) % N;
  }

  return amt;
}

int main()
{
  int T;
  scanf(" %d", &T);
  for (int i = 1; i <= T; ++i)
    printf("Case #%d: %lld\n", i, f());

  return 0;
}
