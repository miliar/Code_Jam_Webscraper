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
#include <queue>

using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
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
  vi C;
  int N;
  scanf("%d", &N);
  C.resize(N);
  for (int i = 0; i < N; ++i)
    scanf("%d", &C[i]);
  sort(C.begin(), C.end());
  int worst = 1<<20;
  if (!N) worst = 0;
  multiset<pii> has;
  for (int i = 0; i < N; ++i) {
    bool used = false;
    //    printf("process %d\n", C[i]);
    while (!has.empty()) {
      int e = has.begin()->first, l = has.begin()->second;
      if (e < C[i]-1) {
	//	printf("discard %d %d\n", e, l);
	worst = min(worst, l);
	has.erase(has.begin());
      } else if (e == C[i]-1) {
	//	printf("add to %d %d\n", e, l);
	has.erase(has.begin());
	has.insert(pii(C[i], l+1));
	used = true;
	break;
      } else {
	//	printf("next is %d %d, postpone\n", e, l);
	break;
      }
    }
    if (!used) {
      has.insert(pii(C[i], 1));
    }
  }
  for (set<pii>::iterator it = has.begin(); it != has.end(); ++it)
    worst = min(worst, it->second);
  print("Case #%d: %d\n", P, worst);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
