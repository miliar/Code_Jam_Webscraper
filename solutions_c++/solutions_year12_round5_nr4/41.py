#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>

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

const int MAXL = 5010;
char s[MAXL + 1];
vvb was;

char getC(int x) { if (x < 26) return 'a' + x; return '0' + x - 26; }

int ne[26][2];

void solve() {
  int k;
  scanf("%d%s", &k, s);

  was = vvb(36, vb(36, false));
  for (int i = 0; s[i + 1]; i++) {
    int c1 = s[i] - 'a', c2 = s[i + 1] - 'a';
    for (int t1 = 0; t1 < 2; t1++)
    for (int t2 = 0; t2 < 2; t2++) {
      assert(getC(ne[c1][t1]) != '2');
      assert(getC(ne[c2][t2]) != '2');
      assert(ne[c1][t1] != 26 + 2);
      assert(ne[c2][t2] != 26 + 2);
      was[ne[c1][t1]][ne[c2][t2]] = true;
    }
  }

  int cnt = 0;
  int addIn = 0, addOut = 0;
  for (int a = 0; a < 36; a++) {
    int ind = 0, outd = 0;
    for (int b = 0; b < 36; b++) {
      if (was[a][b]) { outd++; cnt++; }
      if (was[b][a]) ind++;
    }

    int d = abs(ind - outd);
    if (ind < outd) addIn += d;
    else addOut += d;
  }
  eprintf("cnt=%d\n", cnt);
  printf("%d\n", 1 + cnt + max(0, max(addIn, addOut) - 1));
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

  for (int i = 0; i < 26; i++) {
    ne[i][0] = ne[i][1] = i;
  }
  {
    const char *as = "o0i1e3a4s5t7b8g9";
    for (int pos = 0; as[pos];) {
      char a = as[pos++];
      char b = as[pos++];
      ne[a - 'a'][1] = 26 + b - '0';
    }
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  char buf[100];
  fgets(buf, sizeof buf, stdin);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d: ", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}
