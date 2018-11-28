#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
using namespace std;

#define X first
#define Y second
#define PB push_back

typedef long long ll;
typedef long long ent;
typedef pair<int, int> P;
typedef vector<int> Vi;
typedef vector<string> Vs;
typedef vector<Vi> Mi;
typedef vector<Vs> Ms;
typedef vector<P> Vp;
typedef vector<Vp> Mp;

typedef queue<int> Q;
typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef map<string, int> MAPS;
typedef MAP::iterator Mit;
typedef stringstream SS;

const int INF = 1000000000;

int N, M;
Ms dict;
Mi mask;
int maxi;
string solution;
string list;

MAPS position;

string clean(string s) {
  int n = s.size();
  string r;
  for (int i = 0; i < n; ++i)
    if (s[i] != '_')
      r += s[i];
  return r;
}

void fun(int n, int e, int d, int act, string st) {
//   cerr << n << " " << e << " " << d << endl;
  if (n == 26) {
    st = clean(st);
    if (act > maxi) {
      maxi = act;
      solution = st;
    }
    else if (act == maxi) {
      if (position[st] < position[solution]) solution = st;
    }
    return;
  }
  
  MAP m;
  for (int i = e; i <= d; ++i) ++m[mask[i][n]];
  
  int q = 0;
  for (Mit it = m.begin(); it != m.end(); ++it) {
    int nex = act;
    if (it->X == 0 and m.size() > 1) ++nex;
    
    string s = st;
    for (int i = 0; i < 10; ++i) {
      if (it->X&(1<<i)) {
        s[i] = list[n];
      }
    }
    
    fun(n + 1, e + q, e + q + it->Y - 1, nex, s);
    q += it->Y;
  }
}

void solve(Vs dic) {
  int n = dic.size();
  if (n == 0) {
    maxi = -INF;
    return;
  }
  mask = Mi(n, Vi(26, 0));
  for (int j = 0; j < n; ++j) {
    for (int k = 0; k < 26; ++k) {
      for (int h = 0; h < int(dic[j].size()); ++h) {
        if (dic[j][h] == list[k]) {
          mask[j][k] |= 1<<h;
        }
      }
    }
  }
  sort(mask.begin(), mask.end());
  maxi = -INF;
  fun(0, 0, n - 1, 0, "__________");
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> N >> M;
    dict = Ms(11);
    position.clear();
    for (int i = 0; i < N; ++i) {
      string s;
      cin >> s;
      dict[s.size()].PB(s);
      position[s] = i;
    }
    
    
    Vs res;
    for (int i = 0; i < M; ++i) {
//       string list;
      cin >> list;
      
      int best = -INF;
      string act;
      for (int sz = 1; sz <= 10; ++sz) {
        solve(dict[sz]);
        if (maxi > best) {
          best = maxi;
          act = solution;
        }
      }
      res.PB(act);
//       cout << maxi << " " << solution << endl;
    }
    cout << "Case #" << cas << ":";
    for (int i = 0; i < M; ++i) cout << " " << res[i];
    cout << endl;
  }
}
