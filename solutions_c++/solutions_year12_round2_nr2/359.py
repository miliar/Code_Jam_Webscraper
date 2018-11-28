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

const double eps=1e-10;
const double inf=1e9;

int H, n,m;
int c[111][111],f[111][111];
double d[111][111][2];

int comp(double a, double b) {
  if (abs(a-b) < eps)
    return 0;
  if (a-b < eps)
    return -1;
  return +1;
}

void solve(int testcase) {
  printf("Case #%d: ", testcase);
  eprintf("Case #%d: ", testcase);
  scanf("%d%d%d", &H, &n, &m);
  for (int i=0; i<n; ++i)
    for (int j=0; j<m; ++j)
      scanf("%d", &c[i][j]);
  for (int i=0; i<n; ++i)
    for (int j=0; j<m; ++j)
      scanf("%d", &f[i][j]);

  for (int i=0; i<n; ++i)
    for (int j=0; j<m; ++j)
      for (int k=0; k<2; ++k)
        d[i][j][k]=inf;
  priority_queue < pair < pair < double, int > , pair <int,int> > > q;
  q.push(mp(mp(0.0,0),mp(0,0)));
  d[0][0][0]=0.0;

  while (!q.empty()) {
    int i = q.top().s.f;
    int j = q.top().s.s;
    int k = q.top().f.s;
    double t = q.top().f.f;
    q.pop();

    if (-d[i][j][k] != t)
      continue;
    t=-t;

    if (k == 0) {
      if (comp(d[i][j][1],0.0)>0) {
        d[i][j][1] = 0;
        q.push(mp(mp(-d[i][j][1], 1), mp(i,j)));
      }
    }

    for (int di=-1; di<=1; ++di)
      for (int dj=-1; dj<=1; ++dj) {
        if (di==0 && dj==0) continue;
        if (di!=0 && dj!=0) continue;
        int ii=di+i;
        int jj=dj+j;
        if (ii<0 || ii>=n || jj<0 || jj>=m) continue;

        if (c[ii][jj]-f[ii][jj]<50 || c[ii][jj]-f[i][j]<50 || c[i][j]-f[ii][jj]<50)
          continue;

        if (k == 1) {
          double w=max(0.0,H-10*t);

          if (comp(c[ii][jj]-w,50.0)>=0) {
            double cost=0;
            if (w-f[i][j] >= 20) cost=1; else cost=10;

            if (comp(d[ii][jj][k],t+cost)>0) {
              d[ii][jj][k] = t+cost;
              q.push(mp(mp(-d[ii][jj][k], k), mp(ii,jj)));
            }
          } else {
            double tt=(50.0-(c[ii][jj]-w))/10.0;
            double ww=w-10*tt;
            double cost = tt;
            if (comp(ww-f[i][j],20)>=0) cost+=1; else cost+=10;

            if (comp(d[ii][jj][k],t+cost)>0) {
              d[ii][jj][k] = t+cost;
              q.push(mp(mp(-d[ii][jj][k], k), mp(ii,jj)));
            }
          }

        } else {
          if (comp(c[ii][jj]-H,50.0)>=0) {
            if (comp(d[ii][jj][0],0.0)>0) {
              d[ii][jj][0] = 0.0;
              q.push(mp(mp(-d[ii][jj][0], 0), mp(ii,jj)));
            }
          }
        }

      }
  }
  printf("%.7lf\n", min(d[n-1][m-1][0],d[n-1][m-1][1]));
  eprintf("%.7lf\n", min(d[n-1][m-1][0],d[n-1][m-1][1]));
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
    solve(i);
  return 0;
}
