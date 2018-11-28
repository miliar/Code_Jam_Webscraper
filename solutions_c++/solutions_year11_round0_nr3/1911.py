#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N = 1000;
const int MAX_C = 1000000;
const int INFINITY = 1000000000;

int N;
int C[MAX_N];
int dist[MAX_C + 1];

inline void
solve()
{
  int total = 0, xor_total = 0;
  int min_c = INFINITY;

  for (int i = 0; i < N; ++i) {
	 xor_total ^= C[i];
	 total += C[i];
	 min_c = min(min_c, C[i]);
  }

  if (xor_total != 0) {
	 printf("NO\n");
	 return;
  }

  printf("%d\n", total - min_c);
}

int
main()
{
  int T;
  
  scanf("%d", &T);

  for (int t = 0; t < T; ++t) {
	 scanf("%d", &N);

	 for (int i = 0; i < N; ++i)
		scanf("%d", &C[i]);

	 printf("Case #%d: ", t + 1);
	 solve();
  }

  return (0);
}
