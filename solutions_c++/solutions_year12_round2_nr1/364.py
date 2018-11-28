#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define f first
#define s second

const double eps = 1e-10;
const int IT = 80;

int X,n;
pair <int,int> J[222];
double ans[222], res[222];
double ss[222];

int comp(double a, double b) {
  if (abs(a-b) < eps)
    return 0;
  if (a-b < eps)
    return -1;
  return +1;
}

bool cool(double m) {
  double s = J[0].f + m*X;
  double sum = X*(1.0-m);
  int count = 0;
  for (int i=1; i<n; ++i)
    if (comp(J[i].f,s) <= 0) {
      sum += J[i].f;
      ++count;
    }
  if (count == 0)
    return false;
  return comp(sum,count*s) <= 0;
}

double calc(int i) {
  swap(J[i],J[0]);
  double l=0.0, r=1.0;
  for (int it=0; it<IT; ++it) {
    double m=(l+r)/2;
    if (cool(m)) r=m; else l=m;
  }
  swap(J[i],J[0]);
  return l;
}

void solve(int testcase) {
  printf("Case #%d: ", testcase);
  eprintf("Case #%d: ", testcase);
  scanf("%d",&n);
  for (int i=0; i<n; ++i)
    scanf("%d", &J[i].f);
  X = 0;
  for (int i=0; i<n; ++i)
    X += J[i].f;
  for (int i=0; i<n; ++i)
    ans[i] = calc(i)*100;
  for (int i=0; i<n; ++i)
    printf("%.6lf%c", ans[i], " \n"[i+1==n]);
  for (int i=0; i<n; ++i)
    eprintf("%.6lf%c", ans[i], " \n"[i+1==n]);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
    solve(i);
  return 0;
}
