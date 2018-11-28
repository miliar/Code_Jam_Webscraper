#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_R = 500;
const int MAX_C = 500;

int R, C, D;
int W[MAX_R][MAX_C];

char buf[512];

inline void
read_input()
{
  scanf("%d %d %d", &R, &C, &D);

  for (int i = 0; i < R; ++i) {
    scanf("%s", buf);

    for (int j = 0; j < C; ++j)
      W[i][j] = buf[j] - '0';
  }
}

inline bool
corner(int i, int j, int K)
{
  if (i == 0 && j == 0)
    return (true);

  if (i == 0 && j == K-1)
    return (true);

  if (i == K-1 && j == 0)
    return (true);

  if (i == K-1 && j == K-1)
    return (true);

  return (false);
}

inline bool
mass_center_ok(int i, int j, int K)
{
  pair<int, int> cs = make_pair(0, 0);

  /*  if (K % 2 == 1) {
    pair<int, int> center = make_pair(i + K/2, j + K/2);

    for (int r = 0; r < K; ++r)
      for (int c = 0; c < K; ++c) 
	if (!corner(r, c, K))
	  cs = make_pair(cs.first + (D + W[i + r][j + c])*(i + r - center.first), cs.second + (D + W[i + r][j + c])*(j + c - center.second));
	  } else {*/
    pair<int, int> center = make_pair(2*i + K, 2*j + K);

    for (int r = 0; r < K; ++r)
      for (int c = 0; c < K; ++c) 
	if (!corner(r, c, K)) {
	  cs = make_pair(cs.first + (D + W[i + r][j + c])*(1 + 2*(i + r) - center.first), cs.second + (D + W[i + r][j + c])*(1 + 2*(j + c) - center.second));
	}
    /*}*/

  return (cs.first == 0 && cs.second == 0);
}

inline bool
feasible(int K)
{
  for (int i = 0; i + K <= R; ++i)
    for (int j = 0; j + K <= C; ++j)
      if (mass_center_ok(i, j, K))
	return (true);

  return (false);
}

inline void
solve()
{
  for (int K = min(R, C); K >= 3; --K)
    if (feasible(K)) {
      printf("%d\n", K);
      return;
    }

  printf("IMPOSSIBLE\n");
}

int
main()
{
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);
    read_input();
    solve();
  }

  return (0);
}
