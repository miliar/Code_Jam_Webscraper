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
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 1000;

int M, W; // numbers of men and women

char visited[MAXN];
int husband[MAXN];
char like[MAXN][MAXN];

bool find_wife(int m)
{
  if (visited[m]) return false;
  visited[m] = true;
  for (int w = 0; w < W; w++)
    if (like[m][w])
      if (husband[w] == -1 || find_wife(husband[w]))
	{
	  husband[w] = m;
	  return true;
	}
  return false;
}

int maxmatch(void)
{
  memset(husband, -1, sizeof(husband));
  int ans = 0;
  for (int m = 0; m < M; m++)
    {
      memset(visited, 0, sizeof(visited));
      if (find_wife(m))
	ans++;
      else
	return 0;
    }
  return ans;
}

int main(void) {
  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    vector <int> freqs(10002);
    int N; cin >> N;
    int ans;
    if (N == 0) ans = 0;
    else {
      for (int i = 0; i < N; i++) {
	int x; cin >> x;
	freqs[x]++;
      }
      vector <int> plus, minus;
      for (int x = 0; x <= 10000; x++) {
	for (int d = 0; d < freqs[x+1]-freqs[x]; d++)
	  plus.push_back(x);
	for (int d = 0; d < freqs[x]-freqs[x+1]; d++)
	  minus.push_back(x);
      }
      M = W = plus.size();
      int lo = 1, hi = 1001, mid = (lo+hi)/2;
      while (hi-lo > 1) {
	memset(like, 0, sizeof(like));
	for (int m = 0; m < M; m++)
	  for (int w = 0; w < W; w++)
	    if (minus[w]-plus[m] >= mid)
	      like[m][w] = 1;
	if (maxmatch() == M)
	  lo = mid;
	else
	  hi = mid;
	mid = (lo+hi)/2;
      }
      ans = mid;
    }
    printf("Case #%d: %d\n", test, ans);
  }
}
