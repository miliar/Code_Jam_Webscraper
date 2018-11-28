#include<cstdio>
#include<algorithm>
using namespace std;
  double p[1048576];
  double q[1048576];
int main() {
  int e = 0, T;
  double ans;
  scanf("%d",&T);
  while(T--) {
    int A, B;
    scanf("%d%d",&A,&B);
    for(int i = 0; i < A; ++i)
    {
      scanf("%lf",&p[i]);
      if(i == 0) q[i] = p[i];
      else
        q[i] = q[i-1] * p[i];
    }
    // if i press enter now:
    ans = 2. + B;
    double add = B + 1.0;
    for(int i = 0; i <= A; ++i) {
      double alpha = (B-A) + 1.0 + 2*i;
      double good;
      if( i == A ) 
        good = 1.0;
      else
        good = q[A-1-i];
      double v = alpha * good + (alpha + B + 1.) * (1 - good);
      ans = min(ans, v);
    }
    printf("Case #%d: %.10lf\n", ++e, ans);
  }
  return 0;
}
