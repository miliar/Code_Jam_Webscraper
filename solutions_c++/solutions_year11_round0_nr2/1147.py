#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <valarray>
#include <algorithm>
#include <functional>

#define REP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define rep(i,b)   REP(i,0,b)
#define FOR(i,c)   for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c)     (c).begin(), (c).end()

using namespace std;
typedef long long ll;
const double eps = 1e-10;
const int inf = 1<<28;

typedef pair<char,char> P;

int main() {  
//  freopen("dbg.in", "r", stdin);
  int i, j, tc, tcc = 1;
  scanf("%d", &tc);
  
  for (; tc--; ) {

    int C, D, N;
    map<P, char> mp;
    map<char, char> del_pair;
    P p;
    cin >> C;
    rep(i, C) {
      string str; cin >> str;
      p.first = str[0], p.second = str[1]; mp[p] = str[2];
      p.first = str[1], p.second = str[0]; mp[p] = str[2];      
    }
    cin >> D;
    rep(i, D) {
      string str; cin >> str;
      del_pair[str[0]] = str[1];
      del_pair[str[1]] = str[0];
    }
    cin >> N;
    string str; cin >> str;
    p.first = p.second = '~';
    map<char, int> cnt;
    string res;
    rep(i, N) {
      p.first = p.second;
      p.second = str[i];
      if (mp.count(p)) {
        cnt[res[res.size() - 1]]--;
        res[res.size() - 1] = mp[p];
        p.second = mp[p];
        cnt[mp[p]]++;
      } else if (del_pair.count(str[i]) and cnt[del_pair[str[i]]] > 0) {
        p.first = p.second = '~';       
        cnt.clear();
        res.clear();
      } else {
        cnt[str[i]]++;
        res += str[i];
      }
    }
    printf("Case #%d: ", tcc++);
    cout << '[';
    rep(i, res.size()) {
      if (i) cout << ", ";
      cout << res[i];
    }
    puts("]");
  }
  
  return 0;
  
}



