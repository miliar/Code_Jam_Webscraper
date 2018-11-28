#include <set>
#include <cstdio>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int main(){
  int C = getInt();
  REP(cc, C){
    int a = getInt();
    int b = getInt();

    vector<double> p(a);
    REP(i,a) scanf("%lf", &p[i]);

    // enter
    double ret = b + 2;

    // keep typing
    double all = 1.0;
    REP(i,a) all *= p[i];
    const double allp = all * (b - a + 1) + (1.0 - all) * (b - a + 1 + b + 1);

    ret = min(ret, allp);
    // printf("allp: %.2f\n", allp);

    // backspace
    vector<double> correctp(a);
    correctp[0] = p[0];
    REP(i,a){
      if(i) correctp[i] = correctp[i - 1] * p[i];

      int t = (a - i - 1) + (b - i - 1) + 1;
      double prob = t * correctp[i] + (t + b + 1) * (1 - correctp[i]);
      // printf("prob[%d]: %.2f\n", i, prob);

      ret = min(ret, prob);
    }

    printf("Case #%d: %.8f\n", cc + 1, ret);
  }
  return 0;
}
