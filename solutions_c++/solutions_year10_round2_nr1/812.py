#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

void getPath(vector<string> *path) {
  char line[1024];
  fgets(line, sizeof(line), stdin);
  char *pch = strtok(line, "/\n");
  while (pch) {
    path->push_back(string(pch));
    pch = strtok(NULL, "/\n");
  }
}

int main() {
  int cases;
  scanf("%d\n", &cases);
  for (int i = 1; i <= cases; ++i) {
    int n, m;
    scanf("%d%d\n", &n, &m);
    set<string> dirs;
    for (int j = 0; j < n; ++j) {
      vector<string> path;
      getPath(&path);
      ostringstream oss;
      for (int k = 0; k < path.size(); ++k) {
        oss << '/' << path[k];
        dirs.insert(oss.str());
      }
    }
    int x = dirs.size();
    for (int j = 0; j < m; ++j) {
      vector<string> path;
      getPath(&path);
      ostringstream oss;
      for (int k = 0; k < path.size(); ++k) {
        oss << '/' << path[k];
        dirs.insert(oss.str());
      }
    }
    int y = dirs.size();
    int answer = y - x;
    printf("Case #%d: %d\n", i, answer);
  }
  return 0;
}
