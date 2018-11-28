#include <cstdio>
#include <algorithm>
using namespace std;

const int P = 100, Q = 1000;
int W[P + 1][Q + 1];

void makeW()
{
  for (int i = 1; i <= P; ++i)
    for (int j = 1; j <= Q; ++j)
      W[i][j] = 0;

  for (int i = 1; i <= P; ++i) {
    for (int j = i + 1; j < Q; ++j) {
      int A = i, B = j;
      for (int k = 1; B - k * A >= 0; ++k) {
	int AA = A;
	int BB = B - k * A;
	if (AA > BB) swap(AA, BB);
	if (!W[AA][BB]) {
	  W[A][B] = 1;
	  break;
	}
	if (W[A][B]) break;
      }
    }
  }
}

bool g(int A, int B)
{
  if (A > B) swap(A, B);
  if (A <= P && B <= Q) return W[A][B];

  // printf("%d %d\n", A, B);
  int K = B / A;
  if (!(B - K * A)) --K;
  for (int k = K; k > 0; --k)
    if (!g(A, B - k * A))
      return true;
  return false;
}

int f(int A1, int A2, int B1, int B2)
{
  int cnt = 0;

  for (int i = A1; i <= A2; ++i)
    for (int j = B1; j <= B2; ++j)
      if (g(i, j)) ++cnt;

  return cnt;
}

int main()
{
  makeW();

  int T;
  scanf(" %d", &T);
  for (int i = 1; i <= T; ++i) {
    int A1, A2, B1, B2;
    scanf(" %d %d %d %d", &A1, &A2, &B1, &B2);
    printf("Case #%d: %d\n", i, f(A1, A2, B1, B2));
  }

  return 0;
}
