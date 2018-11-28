#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int B[2000], E[2000], w[2000];

vector<pair<int,int> > intervals;

int X, S, R, t, N;
double running;
double result;

void add(int dist, int bonus) {
  if(dist != 0) intervals.push_back(make_pair(bonus, dist));
}

void handle(int dist, int bonus) {
//  fprintf(stderr, "handle %d %d\n", dist, bonus);
  if(dist == 0) return;
  double runtime = min(running, dist * 1.0 / (R+bonus));
  running -= runtime;
  if(running < 0.00000000001) running = 0;
  double runpos = runtime * (R+bonus);
  double walkpos = dist - runpos;
  double walktime = walkpos * 1.0 / (S+bonus);
  result += runtime + walktime;
//  fprintf(stderr, "runtime=%lf runpos=%lf walkpos=%lf walktime=%lf running=%lf\n", runtime, runpos, walkpos, walktime, running);
}

int main() {
  int Tn;
  scanf("%d", &Tn);
  for(int tid = 1; tid <= Tn; tid++) {
    scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
    for(int i = 0; i < N; i++) {
      scanf("%d%d%d", &B[i], &E[i], &w[i]);
    }
    intervals.clear();
    running = t;
    int pos = 0;
    result = 0;
    for(int i = 0; i < N; i++) {
      add(B[i]-pos, 0);
      add(E[i]-B[i], w[i]);
      pos = E[i];
    }
    add(X-pos, 0);
    sort(intervals.begin(), intervals.end());
    for(int i = 0; i < intervals.size(); i++) {
      handle(intervals[i].second, intervals[i].first);
    }
    printf("Case #%d: %.9lf\n", tid, result);
  }
  return 0;
}


