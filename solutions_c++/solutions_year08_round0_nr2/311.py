#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <utility>
#include <functional>
using namespace std;

typedef pair<int, int> PII;
typedef pair<int, PII> PIP;

#define DEPART first
#define ARRIVE second.first
#define STATION second.second

int getTime(char *bf);

int main() {
  int i, t, T, nA, nB, R;
  int aS[2];
  char b1[12], b2[12];
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    priority_queue< int, vector<int>, greater<int> > ps[2];
    priority_queue< PIP, vector<PIP>, greater<PIP> > pq;
    scanf("%d", &R);
    scanf("%d %d", &nA, &nB);
    for (i=0; i<nA; i++) {
      scanf("%s %s", b1, b2);
      pq.push(PIP(getTime(b1), PII(getTime(b2), 0)));
    }
    for (i=0; i<nB; i++) {
      scanf("%s %s", b1, b2);
      pq.push(PIP(getTime(b1), PII(getTime(b2), 1)));
    }
    aS[0]=aS[1]=0;
    while (!pq.empty()) {
      PIP r=pq.top();
      pq.pop();
      if (ps[r.STATION].empty() || ps[r.STATION].top()>r.DEPART)
	aS[r.STATION]++;
      else
	ps[r.STATION].pop();
      ps[1-r.STATION].push(r.ARRIVE+R);
    }
    printf("Case #%d: %d %d\n", t, aS[0], aS[1]);
  }
  return 0;
}

int getTime(char *bf) {
  int h, m;
  sscanf(bf, "%d:%d", &h, &m);
  return h*60+m;
}
