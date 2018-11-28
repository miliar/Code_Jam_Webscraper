#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

#define MOD 10009

string s;

int n, k;
int dat[20][30];
int cnt[21];
int ans[10];

int calc() {
  int _ans = 0, cur = 1;

  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '+') {
      _ans += cur;
      cur = 1;

    } else {
      int v = s[i] - 'a';
      int sum = 0;
      for (int j = 0; j < n; j++) sum += cnt[j] * dat[j][v];
      sum %= MOD;
      cur = (cur * sum) % MOD;
    }
  }

  return (_ans + cur) % MOD;
}

void dfs(int s) {
  if (s > k) return;

  ans[s] = (calc() + ans[s]) % MOD;

  for (int i = 0; i < n; i++) {
    cnt[i]++;
    dfs(s + 1);
    cnt[i]--;
  }
}



int main() {
  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cin >> s;
    cin >> k;
    memset(dat, 0, sizeof dat);
    cin >> n;

    for (int i = 0; i < n; i++) {
      string str; cin >> str;
      for (int j = 0; j < str.size(); j++)
        dat[i][str[j] - 'a']++;
    }

    cout << "Case #" << _tt << ":";
    memset(cnt, 0, sizeof cnt);
    memset(ans, 0, sizeof ans);

    dfs(0);

    for (int i = 1; i <= k; i++) cout << " " << ans[i];
    cout << endl;
  }

  return 0;
}
