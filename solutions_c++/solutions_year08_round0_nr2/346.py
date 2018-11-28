#include "assert.h"
#include "ctype.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
using namespace std;

#ifndef ONLINE_JUDGE
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4996)  // deprecations
#endif

typedef long long i64;
#define all(x) (x).begin(), (x).end()

//////////////////////////////////////////////////////////////////////////////////////////

enum {ARRIVAL = 0, DEPARTURE = 1};
struct event_t {
  event_t(int time_, int type_, int station_)
    : time(time_), type(type_), station(station_) {}
  bool operator <(const event_t& e) const {
    if (time != e.time) return time < e.time;
    else if (type != e.type) return type < e.type;
    else return station < e.station;
  }
  int time, type, station;
};

pair<int, int> ReadTrip(int fit) {
  int sh, sm, eh, em;
  scanf("%d:%d %d:%d", &sh, &sm, &eh, &em);
  const int start = sh * 60 + sm;
  const int end = eh * 60 + em;
  return make_pair(start, end + fit);
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
#endif
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    int fit, nA, nB; scanf("%d %d %d", &fit, &nA, &nB);
    vector<pair<int, int> > AtoB, BtoA;
    for (int i = 0; i < nA; ++i) AtoB.push_back(ReadTrip(fit));
    for (int i = 0; i < nB; ++i) BtoA.push_back(ReadTrip(fit));
    vector<event_t> events;
    for (int i = 0; i < nA; ++i) {
      events.push_back(event_t(AtoB[i].first, DEPARTURE, 0));
      events.push_back(event_t(AtoB[i].second, ARRIVAL, 1));
    }
    for (int i = 0; i < nB; ++i) {
      events.push_back(event_t(BtoA[i].first, DEPARTURE, 1));
      events.push_back(event_t(BtoA[i].second, ARRIVAL, 0));
    }
    sort(all(events));
    int start[2] = {0, 0}, ready[2] = {0, 0};
    for (int i = 0; i < (int)events.size(); ++i) {
      if (events[i].type == ARRIVAL) ++ready[events[i].station];
      else if (ready[events[i].station] <= 0)
        ++start[events[i].station];
      else --ready[events[i].station];
    }
    printf("Case #%d: %d %d\n", Ti, start[0], start[1]);
  }
  return 0;
}
