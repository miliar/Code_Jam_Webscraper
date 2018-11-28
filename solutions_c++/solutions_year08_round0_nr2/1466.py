#include <cstdio>
#include <map>

using namespace std;

int read_time() {
  int h, m; scanf("%d:%d", &h, &m);
  return h*60+m;
}

void process(map<int, int>& a, map<int, int>& b, 
	     int& ca, int& cb, int& pa, int& pb) {
  int d = a.begin()->second;
  a.erase(a.begin());
  if (d < 0) {
    /* trains arrive at a */
    pa -= d;
  } else if (d > 0) {
    /* trains leave a to b */
    if (d > pa) {
      d  -= pa;
      ca += d;
      pa = 0;
    } else {
      pa -= d;
    }
  }
}

void go(int& ca, int& cb) {
  int t, na, nb; scanf("%d%d%d", &t, &na, &nb);
  map<int, int> a, b;
  while(na--) {
    int s = read_time(), f = read_time();
    a[s]   += 1;
    b[f+t] -= 1;
  }
  while(nb--) {
    int s = read_time(), f = read_time();
    b[s]   += 1;
    a[f+t] -= 1;
  }
  ca = cb = 0;
  int pa = 0, pb = 0;
  while(!a.empty() && !b.empty()) {
    if (a.begin()->first <= b.begin()->first) {
      process(a, b, ca, cb, pa, pb);
    } else {
      process(b, a, cb, ca, pb, pa);
    }
  }
  while(!a.empty()) {
    process(a, b, ca, cb, pa, pb);
  }
  while(!b.empty()) {
    process(b, a, cb, ca, pb, pa);
  }
}

int main() {
  int T; scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    int ca, cb; go(ca, cb);
    printf("Case #%d: %d %d\n", i, ca, cb);
  }
}
