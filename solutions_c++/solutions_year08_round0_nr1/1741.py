#include<iostream>
#include<map>
#include<cassert>
using namespace std;

int main() {
  int cases, q, n, k, i, x, ans;
  map<string, int> m;
  bool a[105];
  string s;
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    cin >> n; getline(cin, s);
    m.clear();
    for (i = 0; i < n; i++) {
      getline(cin, s);
      m[s] = i;
    }
    memset(a, 0, sizeof(a));
    ans = 0; x = 0;
    cin >> k; getline(cin, s);
    for (i = 0; i < k; i++) {
      getline(cin, s);
      assert(m.find(s) != m.end());
      if (! a[m[s]]) {
	if (x == n-1) {
	  x = 0;
	  ans++;
	  memset(a, 0, sizeof(a));
	}
	x++;
	a[m[s]] = true;
      }
    }
    printf("Case #%d: %d\n", q, ans);
  }
  return 0;
}
