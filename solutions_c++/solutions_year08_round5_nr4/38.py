#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

const int p = 10007;
int inv[p];

int binom(int n, int k)
{
  if (k == 0) return 1;
  if (n < k) return 0;
  int ans = 1;
  for (int i = 1; i <= k; i++)
    ans = ((ans * (n+1-i)) % p * inv[i]) % p;
  //cerr << n << " " << k << " " << ans << endl;
  return ans;
}

int calc(int x, int y)
{
  if (x < 0 || y < 0) return 0;
  if ((x+y) % 3 != 0) return 0;
  int m = (x+y) / 3;
  x -= m; y -= m;
  if (x < 0 || y < 0) return 0;
  return binom((x+y)/p, y/p) * binom((x+y)%p, y%p) % p;
}

int main(void)
{
  for (int i = 0; i < p; i++)
    for (int j = 0; j < p; j++)
      if (i*j%p == 1)
	inv[i] = j;
  int NUM_CASES;
  cin >> NUM_CASES;
  for (int c = 1; c <= NUM_CASES; c++) {
    int H, W, R;
    cin >> H >> W >> R;
    vector < pair <int, int> > rocks;
    for (int i = 0; i < R; i++) {
      int r, c;
      cin >> r >> c;
      rocks.push_back(make_pair(r, c));
    }
    if (rocks.size() > 0)
      sort(rocks.begin(), rocks.end());
    int R2 = 1<<R;
    vector < vector <int> > ways(R+2, vector <int> (R+2));
    rocks.insert(rocks.begin(), make_pair(1, 1));
    rocks.push_back(make_pair(H, W));
    for (int i = 0; i < R+2; i++)
      for (int j = 0; j < R+2; j++)
	ways[i][j] = calc(rocks[j].first - rocks[i].first,
			  rocks[j].second - rocks[i].second);
    int ans = 0;
    for (int mask = 0; mask < R2; mask++) {
      vector <int> vi(1, 0);
      for (int i = 0; i < R; i++)
	if ((mask>>i)&1)
	  vi.push_back(i+1);
      vi.push_back(R+1);
      int tans = 1;
      for (int i = 0; i+1 < vi.size(); i++)
	tans = (tans * ways[vi[i]][vi[i+1]]) % p;
      ans += tans * (vi.size() % 2 == 0 ? 1 : -1);
    }
    ans = (ans + p*p) % p;
    cerr << c << " " << ans << endl;
    printf("Case #%d: %d\n", c, ans);
  }
}
