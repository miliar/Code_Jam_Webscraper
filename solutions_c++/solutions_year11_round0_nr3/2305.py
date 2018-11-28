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

int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
	  int x = 0;
	  int s = 0;
	  int m = 999999999;
	  int n, i;
	  for (cin >> n; n; n--) {
		  cin >> i;
		  x ^= i;
		  s += i;
		  m = min(m, i);
	  }

    cout << "Case #" << C << ": ";
	  if (x == 0)
		  cout  << s-m << endl;
	  else
		  cout << "NO" << endl;
  }
}
