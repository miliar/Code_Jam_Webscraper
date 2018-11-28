#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 2011;
struct seg {
  int sp;
  double t;
  bool operator<(seg a) const {
    return sp < a.sp;
  }
}s[N];
main() {
  int i, T, C = 1;
  scanf("%d", &T);
  while (T--) {
    int st, ed, ws, rs, ac, n;
    double rt, wt, t, t0;
    scanf("%d %d %d %lf %d", &ed, &ws, &rs, &rt, &n);
    wt =  ed/1.0/ws;
    for (t = i = 0; i < n; ++i) {
      scanf("%d %d %d", &st, &ed, &ac);
      wt -= (ed - st)/1.0/ws;
      s[i].t = (ed - st)/1.0/(ws + ac);
      s[i].sp = ws + ac;
      t += s[i].t;
    }
    t += wt;
    s[n++] = (seg){ws, wt};
    sort(s, s+n);
    for (i = 0; i < n; ++i) {
      if (rt < 0) break;
      ac = s[i].sp - ws + rs;
      if (rt > s[i].sp*s[i].t/ac) {
        rt -= s[i].sp*s[i].t/ac;
        t -= s[i].t;
        t += s[i].sp*s[i].t/ac;
      } else {
        t -= s[i].t;
        t += rt + (s[i].sp*s[i].t - ac*rt)/s[i].sp;
        rt = -1;
      }
    }
    printf("Case #%d: %lf\n", C++, t);
  }
}
