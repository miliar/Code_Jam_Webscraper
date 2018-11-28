#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

const int maxn = 20000010;

int g[maxn];
long long s[maxn];

int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    int r, k, n;
    cin >> r >> k >> n; 
    for (int i = 0; i < n; i++) {
      cin >> g[i];
      g[i+n] = g[i];
    }
    s[0] = 0;
    for (int i = 0; i < 2*n; i++)
      s[i+1] = s[i]+g[i];

    long long res = 0;
    if (s[n] <= k) 
      res = s[n]*r;
    else {
      int i = 0;
      for (; r; r--) {
	int d = i;
	int h = i+n;
	while (h-d > 1) {
	  int m = (d+h)/2;
	  if (s[m]-s[i] <= k)
	    d = m;
	  else
	    h = m;
	}
	res += s[d]-s[i];
	i = d % n;
      }
    }
    cout << "Case #" << C << ": " << res << endl;
  }
}
