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

const char *ord = "yhesocvxduiglbkrztnwjpfmaq";
//const char *ord = "yhesocvxduiglbkr`tnwjpfma`";

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

char buf[1024];
void solve() {
  fgets(buf, sizeof buf, stdin);
  for (int i = 0; buf[i]; i++)
    if (isalpha(buf[i])) {
      assert('a' <= buf[i] && buf[i] <= 'z');
      buf[i] = ord[buf[i] - 'a'];
    }
  printf("%s", buf);
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
  char buf[100];
  fgets(buf, sizeof buf, stdin);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d: ", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}
