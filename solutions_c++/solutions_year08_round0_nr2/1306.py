#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>

using namespace std;

#define MAXT 212

int na, nb, n, turn;

typedef struct {int arr, dep, from;} trip_t;
trip_t trips[MAXT];

int nposs;
vector< pair<int, int> > conf;

bool cmp(const trip_t &a, const trip_t &b) {
  if (a.dep < b.dep)
    return true;
  if (a.dep > b.dep)
    return false;
  if (a.arr < b.arr)
    return true;
  return false;
}

bool conf_cmp(const pair<int, int> &a, const pair<int, int> &b) {
  if (a.first+a.second < b.first+b.second)
    return true;
  if (a.first+a.second > b.first+b.second)
    return false;
  return a < b;
}

bool poss(int a, int b) {
  int i, time;
  priority_queue<int> A, B;

  for (i = 0; i < a; i++) A.push(0);
  for (i = 0; i < b; i++) B.push(0);

  for (i = 0; i < n; i++)
    if (!trips[i].from) {
      if (A.empty())
	return false;
      time = -A.top(); A.pop();
      if (time > trips[i].dep)
	return false;
      B.push(-(trips[i].arr+turn));
    } else {
      if (B.empty())
	return false;
      time = -B.top(); B.pop();
      if (time > trips[i].dep)
	return false;
      A.push(-(trips[i].arr+turn));
    }

  return true;
}

int main() {
  int t, cases = 1;
  int i, a, b;

  for (a = 0; a <= 100; a++)
    for (b = 0; b <= 100; b++) {
      conf.push_back(make_pair(a,b));
    }

  nposs = conf.size();

  sort(conf.begin(), conf.end(), conf_cmp);

  scanf("%d", &t);
  while (t--) {
    scanf("%d", &turn);
    scanf("%d%d", &na, &nb);

    for (i = 0; i < na; i++) {
      int ah, am, dh, dm;
      scanf("%d:%d %d:%d", &dh, &dm, &ah, &am);
      trips[i].dep = dh*60+dm;
      trips[i].arr = ah*60+am;
      trips[i].from = 0;
    }
    
    n = na+nb;
    for (i = na; i < n; i++) {
      int ah, am, dh, dm;
      scanf("%d:%d %d:%d", &dh, &dm, &ah, &am);
      trips[i].dep = dh*60+dm;
      trips[i].arr = ah*60+am;
      trips[i].from = 1;
    }
    
    sort(trips, trips+n, cmp);

    printf("Case #%d: ", cases++);
    for (i = 0; i < nposs; i++) {
      if (poss(conf[i].first, conf[i].second)) {
	printf("%d %d\n", conf[i].first, conf[i].second);
	break;
      }
    }
  }

  return 0;
}
