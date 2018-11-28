#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

const int off = 1500000;

int a[2*off];

int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    int n;
    cin >> n;
    CLEAR(a);
    queue<int> q;
    for (int i = 0; i < n; i++) {
      int p, v;
      cin >> p >> v;
      p += off;
      a[p] += v;
      if (a[p] > 1)
	q.push(p);
    }

    int res = 0;
    while (!q.empty()) {
      int p = q.front(); q.pop();
      while (a[p] > 1) {
	a[p] -= 2;
	if (++a[p-1] > 1)
	  q.push(p-1);
	if (++a[p+1] > 1)
	  q.push(p+1);
	res++;
      }
    }
    cout << "Case #" << C << ": " << res << endl;
  }
}
