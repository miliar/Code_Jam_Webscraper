#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define eps 1e-9

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

double UX[200];
double UY[200];
double LX[200];
double LY[200];

int UN, LN;

double findY(double x, double * XX, double * YY, int N, int& pos) {
  int e = N-2;
  for (int i = 1; i < N; ++i)
    if (x <= XX[i]) {
      e = i-1;
      break;
    }
  double ey = YY[e];
  if (fabs(XX[e+1]-XX[e]) > eps) {
    ey += (YY[e+1]-YY[e]) * (x - XX[e]) / (XX[e+1]-XX[e]);
  }
  pos = e+1;
  return ey;
}

double area(double x) {
  //  printf("area %.2lf\n", x);
  int pu, pl;
  double yu, yl;
  yu = findY(x, UX, UY, UN, pu);
  yl = findY(x, LX, LY, LN, pl);

  //  printf("yu = %.2lf; yl = %.2lf\n", yu, yl);

  double sum = 0;
  double px = LX[0], py = LY[0];
  for (int i = 0; i < pu; ++i) {
    sum += UX[i] * py - px * UY[i];
    px = UX[i];
    py = UY[i];
  }
  sum += x * py - px * yu;
  px = x;
  py = yu;
  sum += x * py - px * yl;
  px = x;
  py = yl;
  for (int i = pl-1; i >= 0; --i) {
    sum += LX[i] * py - px * LY[i];
    px = LX[i];
    py = LY[i];
  }

  //  printf("area = %.2lf\n", fabs(sum) * 0.5);

  return fabs(sum) * 0.5;
}

double findCut(int N) {
  double ub, lb, cb;
  ub = UX[UN-1];
  lb = UX[0];
  int maxi = 500;

  double full = area(ub);

  for (int i = 0; i < maxi; ++i) {
    cb = (ub + lb) * 0.5;
    double cr = area(cb);
    if (cr * N < full * (N-1))
      lb = cb;
    else
      ub = cb;
  }
  double x = ub;

  int pu, pl;
  double yu, yl;
  yu = findY(x, UX, UY, UN, pu);
  yl = findY(x, LX, LY, LN, pl);

  UX[pu] = x;
  UY[pu] = yu;
  UN = pu+1;

  LX[pl] = x;
  LY[pl] = yl;
  LN = pl+1;

  return x;
}


int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    double w;
    int K;
    scanf("%lf%d%d%d", &w, &LN, &UN, &K);
    for (int i = 0; i < LN; ++i) {
      scanf("%lf%lf", &LX[i], &LY[i]);
    }
    for (int i = 0; i < UN; ++i) {
      scanf("%lf%lf", &UX[i], &UY[i]);
    }

    printf("Case #%d:\n", t+1);

    vector<double> res;
    for (int i = K; i >= 2; --i) {
      double x = findCut(i);
      res.PB(x);
    }
    reverse(ALL(res));
    for (int i = 0; i < res.size(); ++i)
      printf("%.10lf\n", res[i]);

    fprintf(stderr, "%d/%d\n", t+1, T);
  }

  return 0;
};
