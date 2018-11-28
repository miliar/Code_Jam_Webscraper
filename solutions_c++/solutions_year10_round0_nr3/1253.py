#include <iostream>

using namespace std;

unsigned gs[1000];
unsigned ss[1000];
unsigned ts[1000];

int main ()
{
  unsigned T = 0;
  cin >> T;
  for (unsigned t = 1; t <= T; ++t) {
    memset(gs, 0, sizeof(gs));
    memset(ss, 0, sizeof(ss));
    memset(ts, 0, sizeof(ts));

    unsigned R = 0, k = 0, N = 0;
    cin >> R >> k >> N;
    for (unsigned i = 0; i < N; i++) cin >> gs[i];
    
    unsigned s = 0;
    unsigned X = 0;
    for (unsigned r = 1; r <= R; r++) {
      if (ss[s] > 0 && r-ss[s] <= R-r) {
        unsigned reps = (R-r)/(r-ss[s]);
        unsigned pr = r, pX = X;
        r += reps * (r - ss[s]);
        X += reps * (X - ts[s]);
        ss[s] = pr;
        ts[s] = pX;
      }
      ss[s] = r;
      ts[s] = X;
      unsigned t = 0;
      unsigned p = s;
      while (p < N && t + gs[p] <= k) t += gs[p++];
      if (p == N) p = 0;
      while (p != s && t + gs[p] <= k) t += gs[p++];
      if (t == 0) break;
      s = p;
      X += t;
    }
    
    cout << "Case #" << t << ": " << X << "\n";
  }
  
  return 0;
}