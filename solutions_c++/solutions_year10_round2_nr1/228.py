#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

#define filename "A-large"

int add (set <string>& dirs, string& dir) {
	int ret = 0;
	for (int i = 1; i <= dir.size(); ++i)
		if (i == dir.size() || dir[i] == '/') {
			string parent = dir.substr(0, i);
			if (dirs.find(parent) == dirs.end()) {
				ret++;
				dirs.insert(parent);
			}
		}
	return ret;
}

int main()
{
  freopen (filename ".in", "rt", stdin);
  freopen (filename ".out", "wt", stdout);
  
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
	  int n, m, ans = 0;
	  cin >> n >> m;
	  set <string> dirs;
	  string dir;
	  for (int i = 0; i < n; ++i) {
		  cin >> dir;
		  add (dirs, dir);
	  }
	  for (int i = 0; i < m; ++i) {
		  cin >> dir;
		  ans += add (dirs, dir);
	  }
	  cout << "Case #" << test << ": " << ans << endl;
  }

  return 0;
}