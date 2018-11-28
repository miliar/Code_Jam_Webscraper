/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Sat 25 Jun 2011 12:02:59 AM CST

 @Created By: Zhai Yan

 @Purpose :
        template for gcj

*******************************************************************************/


#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;

static int x;
static int s;
static int r;
static int t;
static int n;

struct Seg {
  public:
  int start;
  int stop;
  int w;
  Seg() {}
  bool operator < (const Seg& other) const {
    return w < other.w;
  }
} wst[1000000];



static void solve(int t)
{
  int no_w = 0;
  scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
  //fprintf(stderr, "%d %d %d %d %d\n", x, s, r, t, n);
  for (int i = 0; i < n; i++) {
    scanf("%d%d%d", &wst[i].start, &wst[i].stop, &wst[i].w);
  //  fprintf(stderr, "%d %d %d\n", wst[i].start, wst[i].stop, wst[i].w);
    no_w += wst[i].stop - wst[i].start;
  }
  no_w = x - no_w;
  sort(wst, wst+n);
  double used_run = min((double) t, (double) no_w / r);
  double left_run = t - used_run;
  fprintf(stderr, " t = %lf now = %lf left %lf used_run %lf\n", (double) t, (double) no_w, left_run, used_run);

  no_w -= used_run * r;
  double total_time = (double) no_w /s + used_run;

  for (int i = 0; i < n ; i++) {
    double l      = wst[i].stop - wst[i].start;
    double leftw  = l - left_run * (wst[i].w + r);
    //fprintf(stderr, "leftw %lf %lf %lf before\n", left_run, leftw, total_time);
    total_time   += left_run;
    if (leftw < 0) {
      fprintf(stderr, "nohit!\n");
      left_run    = -leftw / (wst[i].w + r);
      total_time -= left_run; 
    } else {
      total_time += leftw / (wst[i].w + s);
      left_run = 0;
    }
    fprintf(stderr, "%lf w=%d\n", total_time, wst[i].w);
  }
  printf("%.6lf", total_time);
}


int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}





