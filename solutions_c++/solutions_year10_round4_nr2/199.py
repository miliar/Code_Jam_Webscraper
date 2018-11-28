#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

#define filename "B-large"

long long cost[16][2048];
long long ticket[2048];
int M[2048];
int games;

long long inf = 0x3f3f3f3f3f3f3f3fLL;

long long Cost(int skipped, int game)
{
	if (game > games)
		return skipped > M[game - games - 1] ? inf : 0;

	long long &ret = cost[skipped][game];
	if (ret != -1LL)
		return ret;
	ret = inf;

	ret = min (ret, ticket[game] + Cost(skipped, game << 1) + Cost(skipped, (game << 1) + 1));
	ret = min (ret, Cost(skipped + 1, game << 1) + Cost(skipped + 1, (game << 1) + 1));

	return ret;
}

int main()
{
  freopen (filename ".in", "rt", stdin);
  freopen (filename ".out", "wt", stdout);
  
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
	  memset (cost, 0xff, sizeof (cost));
	  int p;
	  cin >> p;
	  games = (1 << p) - 1;
	  for (int i = 0; i <= games; ++i)
		  cin >> M[i];
	  for (int i = 1 << p-1; i > 0; i >>= 1) {
		  for (int j = 0; j < i; ++j)
			  cin >> ticket[i + j];
	  }
	  cout << "Case #" << test << ": " << Cost(0, 1) << endl;
  }

  return 0;
}