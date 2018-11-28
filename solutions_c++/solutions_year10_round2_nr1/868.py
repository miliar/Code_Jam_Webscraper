#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <string>

using namespace std;

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

#define ASCII 128
#if 0
struct directory {
  string name;
  struct directory* subdirs[ASCII];

  directory(string& path) {
    REP(i, ASCII) subdirs[i] = NULL;
    int last = 1;
    while (last < path.length() && path[last] != '/') last++;
    if (last == path.length()) {
      name = path.substr(1);
    } else {
      name = path.substr(1, last);
      string subpath = path.substr(last);
      subdirs[path[1]] = new directory(subpath);
    }
  }

  ~directory() {
    REP(i, ASCII) {
      if (subdirs[i])
        delete subdirs[i];
    }
  }

  struct directory* mkdir(string& path) {
    
  }
};
#endif

int addpath(set<string>& dirs, string& path)
{ 
  int length = 1;
  int count = 0;
  string subpath;
  while (length < path.length()) {
    while (length < path.length() && path[length] != '/')
      length++;
    subpath = path.substr(0, length);
    //cout << subpath << endl;
    if (dirs.find(subpath) == dirs.end()) {
      dirs.insert(subpath);
      count++;
    }
    length++;
  }
  return count;
}

int main()
{
  int T, N, M;
  cin >> T;
  REP(cs, T) {
    cin >> N >> M;
    
    string path;
    set<string> dirs;
    dirs.insert("/");
    
    REP(i, N) {
      cin >> path;
      addpath(dirs, path);
    }

    int ans = 0;
    REP(i, M) {
      cin >> path;
      ans += addpath(dirs, path);
    }
    cout << "Case #" << cs+1 << ": " << ans << endl;
  }
  return 0;
}


