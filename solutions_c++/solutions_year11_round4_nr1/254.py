#include <stdio.h>

#include <algorithm>
#include <vector>

using namespace std;

int T;
int S,R;
int X;
int _t;
double t;
int N;
vector<pair<pair<int,int>, int> > inter;
vector<pair<int, int> > V;

int main() {
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%d %d %d %lf %d", &X, &S, &R, &t, &N);
    inter.clear();
    V.clear();
    for (int i=0;i<N;++i) {
      int b,e,w;
      scanf("%d %d %d", &b, &e, &w);
      V.push_back(make_pair(w, e-b));
      inter.push_back(make_pair(make_pair(b,e),w));
    }
    //    sort(inter.begin(),inter.end());
    sort(V.begin(), V.end());
    int sum = 0;
    for (int i=0;i<N;++i)
      sum += V[i].second;
    sum = X-sum;
    double opt = 0;
    //    t = _t;
    if (t*R < sum) {
      opt = t + (sum-t*R)*1.0/S;
      for (int i=0;i<N;++i)
	opt += V[i].second*1.0/(S+V[i].first);
    } else {
      opt = sum*1.0/R;
      t -= opt;
      int cur = 0;
      //      printf("%d %d\n", S, R);
      while (cur < N) {
	//	printf("%d %lf %lf %d %d\n", cur, opt, t, V[cur].first, V[cur].second);
	if (t*(R+V[cur].first) >= V[cur].second) {
	  double curt = V[cur].second*1.0/(R+V[cur].first);
	  opt += curt;
	  t -= curt;
	} else {
	  opt += t + (V[cur].second - t*(R+V[cur].first))*1.0/(S+V[cur].first);
	  t = 0;
	}
	++cur;
      }
    }
    printf("Case #%d: %.8lf\n", TT, opt);
  }
  return 0;
}
