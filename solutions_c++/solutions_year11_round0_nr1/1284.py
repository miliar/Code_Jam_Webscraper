#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
  assert(scanf("%d", &CASES) == 1);
}

int print(const char *err, ...) {
  va_list pvar;
  va_start(pvar, err);
  vfprintf(stderr, err, pvar);
  return vfprintf(stdout, err, pvar);
}

int dprint(const char *err, ...) { 
  if (debug) {
    va_list pvar;
    va_start(pvar, err);
    return vfprintf(stderr, err, pvar);
  }
  return 0;
}


void solve(int P) {
  int N;
  assert(scanf("%d", &N) == 1);
  int pos[200];
  char rob[200][5];
  for (int i = 0; i < N; ++i) assert(scanf("%s%d", rob[i], pos+i) == 2);
  int at[2];
  at[0] = at[1] = 1;
  int T = 0;
  for (int i = 0; i < N; ++i) {
    int x = -1, y = -1;
    for (int j = i; j < N; ++j) if (*rob[j] == 'O') { x = j; break; }
    for (int j = i; j < N; ++j) if (*rob[j] == 'B') { y = j; break; }
    assert((x == i) ^ (y == i));
    int t = 0;
    if (x == i) {
      t = abs(at[0]-pos[i])+1;
      at[0] = pos[i];
      if (y != -1) at[1] += max(min(pos[y]-at[1], t), -t);
    }
    else {
      t = abs(at[1]-pos[i])+1;
      at[1] = pos[i];
      if (x != -1) at[0] += max(min(pos[x]-at[0], t), -t);
    }
    T += t;
  }
  print("Case #%d: %d\n", P, T);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
