
/**
 *
 *  Time-stamp:<2010/05/23 02:12:05>
 **/

#include <functional>
#include <algorithm>
#include <iostream>
#include <complex>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <queue>
#include <cmath>
#include <set>
#include <map>
using namespace std;

#define For(i, s, n) for(int i = (int)(s); i < (int)(n); ++i)
#define rep(i, n) For(i, 0, n)
#define iter(c) __typeof((c).begin())
#define each(c, i) for(iter(c) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long LL;
typedef complex<double> point;

vector<string> get_dir(const string &path)
{
  vector<string> ret;
  string tmp = "";
  for(int i = 1; i < (int)path.size(); ++i)
  {
    if(path[i] == '/') { ret.pb(tmp); tmp = ""; }
    else tmp += path[i];
  }
  ret.pb(tmp);
  return ret;
}

set<string> mlm;

int main()
{
  int T, n, m, cnt = 0;
  string str;

  cin >> T;
  while(T--) {
    mlm.clear();

    cin >> n >> m;
    while(n--) {
      cin >> str;
      vector<string> tmp = get_dir(str);
      string path = "";
      each(tmp, it) {
        path += *it + "/";
        mlm.insert(path);
      }
    }
    int ans = 0;
    while(m--) {
      cin >> str;
      vector<string> tmp = get_dir(str);
      string path = "";
      each(tmp, it) {
        path += *it + "/";
        if(mlm.find(path) == mlm.end()) {
          mlm.insert(path);
          ans += 1;
        }
      }
    }
    cout << "Case #" << ++cnt << ": " << ans << endl;
  }
  return 0;
}


