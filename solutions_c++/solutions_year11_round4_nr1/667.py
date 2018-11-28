#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int N_MAX = 1000;

int main() {
  int T;
  
  scanf("%d", &T);
  for (int caseNum=1; caseNum<=T; caseNum++) {
    int X, S, R, t_int, N;
    int B[N_MAX], E[N_MAX], w[N_MAX];   
    vector<pair<int, int> > odsek;

    scanf("%d %d %d %d %d", &X, &S, &R, &t_int, &N);
    for (int i=0; i<N; i++) {
      scanf("%d %d %d", &B[i], &E[i], &w[i]);
      odsek.push_back(make_pair(S + w[i], E[i] - B[i]));
      X -= E[i] - B[i];
    }
    if (X > 0) odsek.push_back(make_pair(S, X));
    sort(odsek.begin(), odsek.end());
    int delta = R - S;
    
    long double t = 1.0L * t_int;
    long double cas = 0.0L;
    for (int i=0; i<odsek.size(); i++) {
      int len = odsek[i].second;
      int speed = odsek[i].first;
      
      long double tt = 1.0L * len / (speed + delta);
      if (t == 0) {
        cas += 1.0L * len / speed;
      } else if (tt < t) {
        cas += tt;
        t -= tt;
      } else {
        cas += t;
        cas += (len - t * (speed + delta)) / speed;
        t = 0.0L;
      }
      
    }
    
    printf("Case #%d: %.20Lg\n", caseNum, cas);
  }
  
  return 0;
}
