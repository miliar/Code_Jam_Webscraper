#include <cstdio>
#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

#define maxn (1<<14)
string words[16][maxn];
int rank[16][maxn];
int wordc[16];

string ans;
int score, brank;

map<string, bool> tb[32];

char st[128];

void update(const string & w) {
  int len = w.size();
  int cnt = len;
  char word[16];
  char wordo[16];
  for (int i = 0; i < len; ++i) word[i] = '_'; word[len] = 0;
  wordo[len] = 0;
  for (int i = 0; i < 26; ++i) {
    int oc = cnt;
    for (int j = 0; j < len; ++j) {
      wordo[j] = word[j];
      if (w[j] == st[i]) {
	word[j] = st[i];
	--cnt;
      }
    }
    if (oc != cnt) tb[i][wordo] = true;
    
    if (cnt == 0) break;
  }
}

int calcans(const string & w) {
  int len = w.size();
  int cnt = len;
  char word[16];
  char wordo[16];
  int ans = 0;
  for (int i = 0; i < len; ++i) word[i] = '_'; word[len] = 0;
  wordo[len] = 0;
  for (int i = 0; i < 26; ++i) {
    int och = cnt;
    for (int j = 0; j < len; ++j) {
      wordo[j] = word[j]; 
      if (w[j] == st[i]) {
	word[j] = st[i];
	--cnt;
      }
    }
    if (cnt == 0) break;
    if (och == cnt) {
      if (tb[i][wordo])++ans;
    }
  }
  return ans;
}

void doit(int n, string * word, int * rank) {
  for (int i = 0; i < n; ++i) {
    update(word[i]);
  }
  for (int i = 0; i < n; ++i) {
    int res = calcans(word[i]);
    if (res > score || res == score && rank[i] < brank) {
      ans = word[i];
      score = res;
      brank = rank[i];
    }
  }
}

void calc(const string & s) {
  for (size_t i = 0; i < s.size(); ++i)
    st[i] = s[i];
  for (int i = 0; i <= 10; ++i)
    if (wordc[i] > 0) {
      for (int j = 0; j < 32; ++j)
	tb[j].clear();
      doit(wordc[i], words[i], rank[i]);
    }
}

void solve() {
  string ts;
  int n, m;
  cin >> n >> m;
  memset(wordc, 0, sizeof(wordc));
  for(int i = 0; i < n; ++i) {
    cin >> ts;
    int id = ts.size();
    words[id][wordc[id]] = ts;
    rank[id][wordc[id]] = i;
    ++wordc[id];
  }
  for (int i = 0; i < m; ++i) {
    cin >> ts;
    ans = "~error";
    score = -1;
    calc(ts);
    printf(" %s", ans.c_str(), score);
  }
}

int main() {
  freopen("B-large.in", "r", stdin);
  int T, t = 0;
  cin >> T;
  while (T--) {
    printf("Case #%d:", ++t);
    solve();
    putchar('\n');
  }
  return 0;
}
