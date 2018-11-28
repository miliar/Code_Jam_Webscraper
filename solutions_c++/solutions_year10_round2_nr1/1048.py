#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    int N, M;
    //    cout << "!" << endl;
    cin >> N >> M;
    //    cout << "?" << endl;    
    set<string> dirs;
    dirs.clear();
    for(int i = 0; i < N; ++i) {
      string path;
      cin >> path;
      //      cout << path << endl;
      int j;
      for(j = 1; j < path.size(); ++j) {
	if(path[j] == '/') { dirs.insert(path.substr(0, j)); }
      }
      dirs.insert(path.substr(0, j));
    }
    /*
    set<string>::iterator it = dirs.begin();
    while(it != dirs.end()) {
      cout << *it << endl;
      ++it;
    }
    */
    //    cout << dirs.size() << endl;
    int cnt = 0;
    for(int i = 0; i < M; ++i) {
      string path;
      cin >> path;
      int j;
      for(j = 1; j < path.size(); ++j) {
	if(path[j] == '/') {
	  //cout << path.substr(0, j) << endl;
	  if(dirs.find(path.substr(0, j)) == dirs.end()) {
	    ++cnt;
	    dirs.insert(path.substr(0, j));
	  }
	}
      }
      //cout << path.substr(0, j) << endl;
      if(dirs.find(path.substr(0, j)) == dirs.end()) {
	++cnt;
	dirs.insert(path.substr(0, j));
      }
    }
    printf("Case #%d: %d\n", t, cnt);
  }
}
