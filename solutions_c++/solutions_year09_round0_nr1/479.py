#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define ALL(x) (x).begin(), (x).end()
#define MP make_pair

using namespace std;

char word[5000][15];
bool ok[5000][15];

vector<vector<char> > Explode(const string& s) {
  vector<vector<char> > ret;
  int p = 0;
  while (p < (int)s.size()) {
    ret.push_back(vector<char>());
    if (s[p] == '(') {
      ++p;
      while (s[p] != ')') ret.back().push_back(s[p++]);
      ++p;
    } else {
      ret.back().push_back(s[p++]);
    }
  }
  return ret;
}

int main() {
  int L, D, N;
  cin >> L >> D >> N;
  REP(i, D) REP(j, L) cin >> word[i][j];
  REP(n, N) {
    string s;
    cin >> s;

    memset(ok, 0, sizeof(ok));
    vector<vector<char > > v = Explode(s);
    REP(i, L) REP(j, D) {
      bool pre = (i == 0 ? true : ok[j][i - 1]);
      if (!pre) continue;
      REP(k, v[i].size()) if (word[j][i] == v[i][k]) {
        ok[j][i] = true;
        break;
      }
    }

    int cnt = 0;
    REP(i, D) if (ok[i][L - 1]) ++cnt;

    cout << "Case #" << (n + 1) << ": " << cnt << endl;
  }
  return 0;
}
