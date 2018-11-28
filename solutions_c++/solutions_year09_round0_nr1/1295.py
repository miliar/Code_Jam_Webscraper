#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int nl, nd, n;

  cin >> nl >> nd >> n;
  vector<string> d;
  string w;
  while (nd-- && cin >> w)
    d.push_back(w);

  for (int C = 1; C <= n && cin >> w; ++C) {
    vector<int> mask;
    int i = 0;
    while (i < w.size()) {
      if (w[i] == '(') {
	int m = 0;
	++i;
	while (w[i] != ')')
	  m |= (1<<(w[i++]-'a'));
	++i;
	mask.push_back(m);
      } else
	mask.push_back(1<<(w[i++]-'a'));
    }

    int ans = 0;
    for (int i = 0; i < d.size(); ++i) {
      bool f = true;
      for (int j = 0; j < d[i].size(); ++j)
	if (!((mask[j]>>(d[i][j]-'a'))&1)) {
	  f = false;
	  break;
	}

      if (f)
	++ans;
    }

    cout << "Case #" << C << ": " << ans << endl;
  }
}
