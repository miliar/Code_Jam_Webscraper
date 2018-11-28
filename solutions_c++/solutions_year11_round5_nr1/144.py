#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>

using namespace std;

int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

void solve_case();

int main() {
  int T; scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    printf("Case #%d:", t);
    solve_case();
  }
}

void solve_case() {
  int W, N, M, G; cin >> W >> N >> M >> G;
  vector<pair<double, double> > LO, HI;
  for(int i = 0; i < N; i++) {
    int x, y; cin >> x >> y;
    LO.push_back(make_pair(x, y));
  }
  for(int i = 0; i < M; i++) {
    int x, y; cin >> x >> y;
    HI.push_back(make_pair(x, y));
  }
  printf("\n");
  double total = 0;
  for(int i = 0; i < G; i++) {
    pair<double, double> lp = LO[0];
    pair<double, double> hp = HI[0];
    int j = 1;
    int k = 1;
    double pos = 0;
    double target = total * i / G;
    while(j < LO.size() && k < HI.size()) {
      pair<double, double> nlp, nhp;
      if(j < LO.size() && (k == HI.size() || LO[j] < HI[k])) {
        nlp = LO[j++];
        nhp = make_pair(nlp.first, hp.second +
                        (HI[k].second - hp.second) / (HI[k].first - hp.first) *
                        (nlp.first - hp.first));
      } else {
        nhp = HI[k++];
        nlp = make_pair(nhp.first, lp.second +
                        (LO[j].second - lp.second) / (LO[j].first - lp.first) *
                        (nhp.first - lp.first));
      }
      double A = (hp.second - lp.second + nhp.second - nlp.second) *
                 (nlp.first - lp.first) / 2.0;
      if(i) {
        if(A > target) {
          double a = (nhp.second - nlp.second - (hp.second - lp.second)) /
                     (nlp.first - lp.first) / 2;
          double b = hp.second - lp.second;
          double c = -target;
          double x;
          if(fabs(a) < 1e-9) {
            x = target / b;
          } else {
            x = (-b + sqrt(b * b - 4 * a * c)) / (2 * a);
          }
          printf("%.9f\n", lp.first + x);
          break;
        } else {
          target -= A;
        }
      } else {
        total += A;
      }
      lp = nlp;
      hp = nhp;
    }
  }
}
