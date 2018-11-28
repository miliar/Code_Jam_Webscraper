#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

struct dir {
  map<string, dir> subs;

  int process(char* str) {
    int last = 0;
    while (str[last] && str[last] != '/')
      last++;
    bool end = str[last] == 0;
    str[last] = 0;

    int result = 0;
    string d(str);
    if (subs.find(d) == subs.end()) {
      subs[d] = dir();
      result++;
    }

    if (!end)
      result += subs[d].process(str + last + 1);

    return result;
  }
} root;

int main() {
  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cout << "Case #" << _tt << ": ";

    int n, m; cin >> n >> m;
    root.subs.clear();
    char tmp[1024];

    for (int i = 0; i < n; i++) {
      scanf("%s", tmp);
      root.process(tmp + 1);
    }

    int result = 0;
    for (int i = 0; i < m; i++) {
      scanf("%s", tmp);
      result += root.process(tmp + 1);
    }

    cout << result << endl;
  }

  return 0;
}
