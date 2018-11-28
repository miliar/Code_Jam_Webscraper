#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
typedef pair<int, int> PII;

int N, T, NA, NB, a, b, ta, tb;
priority_queue<PII, vector<PII>, greater<PII> > q;

int main() {
  scanf ("%d\n", &N);
  REP(tc,N) {
    scanf ("%d\n", &T);
    scanf ("%d %d\n", &NA, &NB);
    REP(i,NA) {
      int h1, h2, m1, m2;
      scanf ("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
      q.push (make_pair (h2*60+m2+T, 1));
      q.push (make_pair (h1*60+m1, 3));
    }
    REP(i,NB) {
      int h1, h2, m1, m2;
      scanf ("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
      q.push (make_pair (h2*60+m2+T, 2));
      q.push (make_pair (h1*60+m1, 4));
    }
    a=b=ta=tb=0;
    while (!q.empty()) {
      int c = q.top().second;
      q.pop();
      switch (c) {
        case 1: ++tb; break;
        case 2: ++ta; break;
        case 3: if (!ta) ++a; else --ta; break;
        case 4: if (!tb) ++b; else --tb; break;
      }
    }
    cout << "Case #" << tc+1 << ": " << a << " " << b << endl;
  }
  return 0;
}
