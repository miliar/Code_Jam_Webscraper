#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define pb push_back
#define mp make_pair
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

char buf[1024];
char ops[256][256];
bool dels[256][256];

void solve() {
  memset(ops, 0, sizeof ops);
  memset(dels, 0, sizeof dels);
  for (int step = 0; step < 2; step++) {
    int cnt;
    scanf("%d", &cnt);
    for (int i = 0; i < cnt; i++) {
      char a, b; string res = "";
      scanf(" %c%c", &a, &b);
      if (!step) {
        char c;
        scanf("%c", &c);
        res = c;
        ops[a][b] = ops[b][a] = c;
      } else {
        dels[a][b] = dels[b][a] = true;
      }
    }
  }

  int n;
  scanf("%d%s", &n, buf);
  string cur = "";
  for (int i = 0; i < n; i++) {
    cur += buf[i];
    bool wasop = false;
    while (cur.length() >= 2) {
      char a = cur[cur.length() - 2], b = cur[cur.length() - 1];
      if (ops[a][b]) {
        cur = string(cur, 0, cur.length() - 2);
        cur += ops[a][b];
        wasop = true;
      } else
        break;
    }
    if (!wasop) {
      for (int i2 = 0; i2 < cur.length(); i2++)
        if (dels[buf[i]][cur[i2]]) {
          if (dels[buf[i]][cur[i2]]) {
            cur = "";
            break;
          }
        }
    }
  }
  printf("[");
  for (int i = 0; i < cur.length(); i++) {
    printf("%c", cur[i]);
    if (i + 1  < cur.length())
      printf(", ");
  }
  printf("]\n");
}

int main(int argc, char* argv[]) {
  {
    string fname = "std";
    if (argc >= 2) {
      fname = argv[1];
      if (fname.length() >= 3 && string(fname, fname.length() - 3) == ".in")
        fname = string(fname, 0, fname.length() - 3);
    }
    freopen((fname + ".in").c_str(), "r", stdin);
    freopen((fname + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d: ", TN);
    solve();
  }
  return 0;
}
