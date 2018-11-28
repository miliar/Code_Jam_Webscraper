#include <cstdio>
#include <map>
#include <string>
#include <set>

using namespace std;

typedef pair<int, int> pii;

int rt() { int h, m; scanf("%d:%d", &h, &m); return 60*h + m; }

void solve(int P) {

  int na, nb, t;
  scanf("%d%d%d", &t, &na, &nb);
  //  printf("got %d %d %d\n", t, na,
  multiset<pii> events;

  for (int i = 0; i < na; ++i) {
    int start = rt(), stop = rt();
    events.insert(pii(start, 1));
    events.insert(pii(stop+t, -1));
  }
  for (int i = 0; i < nb; ++i) {
    int start = rt(), stop = rt();
    events.insert(pii(start, 2));
    events.insert(pii(stop+t, -2));
  }
  int ta = 0, tb = 0;
  int atA = 0, atB = 0;

  while (!events.empty()) {
    switch (events.begin()->second) {
    case 1: 
      if (!atA) ++ta;
      else --atA;
      break;
    case -1:
      ++atB;
      break;
    case 2:
      if (!atB) ++tb;
      else --atB;
      break;
    case -2:
      ++atA;
      break;
    default: assert(0);
    }
    events.erase(events.begin());
  }

  printf("Case #%d: %d %d\n", P, ta, tb);
}

int main(void) {
  int N;
  scanf("%d", &N);
  for (int i = 1; i <= N; ++i) solve(i);
  return 0;
}
