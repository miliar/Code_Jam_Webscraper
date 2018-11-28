#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

#define filename "B-large"

pair <int, int> chick[64];

int main()
{
  freopen (filename ".in", "rt", stdin);
  freopen (filename ".out", "wt", stdout);

  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
	  cout << "Case #" << test << ": ";

	  int n, k, b, t;
	  cin >> n >> k >> b >> t;
	  for (int i = 0; i < n; ++i)
		  cin >> chick[i].first;
	  for (int i = 0; i < n; ++i)
		  cin >> chick[i].second;
	  sort (chick, chick + n);

	  int swaps = 0;
	  int finished = 0;
	  for (int i = n - 1; i >= 0 && finished < k; --i) {
		  if (t * chick[i].second + chick[i].first >= b) {
			  finished++;
		  } else {
			  swaps += k - finished;
		  }
	  }
	  if (finished < k) {
		  cout << "IMPOSSIBLE" << endl;
	  } else {
		cout << swaps << endl;
	  }
  }

  return 0;
}