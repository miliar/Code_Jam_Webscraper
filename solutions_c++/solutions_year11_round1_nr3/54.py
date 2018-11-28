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

struct card {
  int c, s, t;
};

card all[1000];

void solve(int P) {
  int N, M;
  assert(scanf("%d", &N) == 1);
  for (int i = 0; i < N; ++i) {
    assert(scanf("%d%d%d", &all[i].c, &all[i].s, &all[i].t) == 3);
  }
  assert(scanf("%d", &M) == 1);
  for (int i = 0; i < M; ++i) {
    assert(scanf("%d%d%d", &all[N+i].c, &all[N+i].s, &all[N+i].t) == 3);
  }

  int res = 0;
  for (int reach = N; reach <= N+M+1; ++reach) {
    int turns = 1, score = 0, last = N;
    int at = 0;
    vector<card> hand;
    while (turns > 0) {
      while (at < last && at < N+M) {
	if (all[at].t > 0) {
	  turns += all[at].t-1;
	  score += all[at].s;
	  last += all[at].c;
	} else {
	  hand.push_back(all[at]);
	}
	++at;
      }
      if (!turns || hand.empty()) break;
      int play = 0;
      for (int i = 0; i < hand.size(); ++i) {
	if (at < reach) {
	  if (hand[i].c > hand[play].c || (hand[i].c == hand[play].c && hand[i].s > hand[play].s))
	    play = i;
	} else if (hand[i].s > hand[play].s)
	  play = i;
      }
      --turns;
      score += hand[play].s;
      last += hand[play].c;
      hand.erase(hand.begin() + play);
    }
    
    if (score > res) res = score;
  }

  print("Case #%d: %d\n", P, res);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
