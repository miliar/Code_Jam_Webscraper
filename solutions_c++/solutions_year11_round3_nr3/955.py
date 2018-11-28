#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <cstdio>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t < T+1; ++t) {
    cout << "Case #" << t << ": ";

    int N, L, H;
    cin >> N >> L >> H;

    vector<int> f(N);
    for (int i = 0; i < N; ++i)
      cin >> f[i];

    int ans = -1;
    for (int i = L; i < H+1; ++i) {
      bool ok = true;
      for (unsigned int j = 0; j < f.size(); ++j) {
	if (i >= f[j]) {
	  if (i%f[j] != 0) {
	    ok = false;
	    break;
	  }
	} else {
	  if (f[j]%i != 0) {
	    ok = false;
	    break;
	  }
	}
      }
      if (ok) {
	ans = i;
	break;
      }
    }

    if (ans == -1)
      cout << "NO" << endl;
    else
      cout << ans << endl;
  }
  return 0;
}
