#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;

#define MOD 10009

struct state {
  int ct[4], len;
  state() { memset(ct, 0, sizeof(ct)); len = 0; }
  bool operator<(const state& other) const {
    if (len != other.len)
      return len > other.len;
    for (int i = 0; i < 4; i++)
      if (ct[i] != other.ct[i])
        return ct[i] > other.ct[i];
    return false;
  }
};

map<state, int> mem;
int res[8][16];
int n;
vector<string> D;

inline int eval(state& s, string& p) {
  int r = 1;
  for (int i = 0; i < p.size(); i++) {
    r *= s.ct[i];
    r %= MOD;
  }
  return r;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    string p; cin >> p;
    vector<string> pt;
    int prev = 0;
    for (int i = 0; i < p.size(); i++) {
      if (p[i] == '+') {
        pt.push_back(p.substr(prev, i - prev));
        prev = i + 1;
      }
    }
    pt.push_back(p.substr(prev));

    int K; cin >> K;
    cin >> n; D.clear(); D.resize(n);
    for (int i = 0; i < n; i++)
      cin >> D[i];

    memset(res, 0, sizeof(res));
    for (int i = 0; i < pt.size(); i++) {
      state start;
      mem.clear();

      // cout << "calc " << pt[i] << endl;
      priority_queue<state> q;
      q.push(start);
      mem[start] = 1;
      while (!q.empty()) {
        state cur = q.top(); q.pop();
        int w = mem[cur] % MOD;
        res[i][cur.len] += w * eval(cur, pt[i]);
        res[i][cur.len] %= MOD;
        if (cur.len == K) continue;

        for (int j = 0; j < n; j++) {
          state next = cur;
          next.len++;
          for (int m = 0; m < D[j].size(); m++)
            for (int k = 0; k < pt[i].size(); k++)
              next.ct[k] += (D[j][m] == pt[i][k]);
          if (mem.find(next) == mem.end()) q.push(next);
          mem[next] += w;
        }
      }
    }

    int r;
    cout << "Case #" << c << ": ";
    for (int i = 1; i <= K; i++) {
      r = 0;
      for (int j = 0; j <= pt.size(); j++) {
        r += res[j][i];
        r %= MOD;
      }
      cout << r << " ";
    }
    cout << endl;
  }
}
