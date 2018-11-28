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

bool debug = true;

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
  char comb[200][200], s[1000];
  bool opp[200][200];
  memset(comb, 0, sizeof(comb));
  memset(opp, 0, sizeof(opp));
  int C,D , N;
  assert(scanf("%d", &C));
  for (int i = 0; i < C; ++i) {
    assert(scanf("%s", s) == 1);
    assert(strlen(s) == 3);
    comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
  }
  assert(scanf("%d", &D) == 1);
  for (int i = 0; i < D; ++i) {
    assert(scanf("%s", s) == 1);
    opp[s[0]][s[1]] = opp[s[1]][s[0]] = true;
  }
  assert(scanf("%d", &N) == 1);
  assert(scanf("%s", s) == 1);
  char *p = s;
  for (char *at = s; *at; ++at) {
    *p++ = *at;
    while (p >= s+2 && comb[p[-1]][p[-2]]) {
      p[-2] = comb[p[-1]][p[-2]];
      --p;
    }
    for (char *q = s; q < p; ++q)
      if (opp[*q][p[-1]]) {
	p = s;
	break;
      }
  }
  print("Case #%d: [", P);
  for (char *at = s; at != p; ++at) {
    if (at != s) print(", ");
    print("%c", *at);
  }
  print("]\n");
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
