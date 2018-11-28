#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
using namespace std;
#include<cstring>
#include<cassert>

typedef long long ll;

#define PB push_back
#define MP make_pair

#define A first
#define B second

double solve()
{
  int le, v_walk, v_run, n;
  double max_run_time;
  scanf("%d%d%d%lf%d", &le, &v_walk, &v_run, &max_run_time, &n);
  vector<pair<int, pair<int,int> > > ways;
  for (int i = 0; i < n; i++)
  {
    int bi, ei, wi;
    scanf("%d%d%d", &bi, &ei, &wi);
    if (i > 0)
    {
      int el = ways[ways.size() - 1].B.B;
      if (el != bi)
      {
        ways.PB(MP(0, MP(el, bi)));
      }
    }
    ways.PB(MP(wi, MP(bi, ei)));
  }
  
  if (ways[0].B.A > 0)
  {
    ways.insert(ways.begin(), MP(0, MP(0, ways[0].B.A)));
  }
  if (ways[ways.size() - 1].B.B < le)
  {
    ways.PB(MP(0, MP(ways[ways.size() - 1].B.B, le)));
  }
  
  sort(ways.begin(), ways.end());
  int sz = ways.size();
  double ans = 0;
  for (int i = 0; i < sz; i++)
  {
    int w = ways[i].A;
    int fst = ways[i].B.A;
    int snd = ways[i].B.B;
    
    int d_tot = snd - fst;
    int vri = v_run + w;
    int vwi = v_walk + w;
    
    double t_run = (double)d_tot / (double)vri;
    t_run = min((double) max_run_time, t_run);
    max_run_time -= t_run;
    
    double d_run = vri * t_run;
    double d_wlk = d_tot - d_run;
    double t_wlk = d_wlk / vwi;
    ans += t_run;
    ans += t_wlk;
  }
  
  return ans;
}

int main()
{
  int t; cin >> t;
  for (int i = 1; i <= t; i++)
  {
    double ans = solve();
    printf("Case #%d: %.9f\n", i, ans);
  }
}
