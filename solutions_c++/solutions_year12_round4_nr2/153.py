#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)

int hoge(double r) {

  return (int)(2.0 * r) + 1;

}

int main()
{
  int T;
  cin >> T;
  FOR(t,1,T+1) {
    int N, W, L;
    cin >> N >> W >> L;
    vector<double> r(N);
    REP(i,N) cin >> r[i];

    vector<pair<double,int> > v(N);
    REP(i,N) v[i] = make_pair(hoge(r[i]), i);
    sort(v.rbegin(), v.rend());

    vector<pair<double,double> > ans(N);
    int x = W+1;
    int y = 0;
    int ny = 0;
    REP(i,N) {
      if (x > W) {
        x = 0;
        y = ny;
        ny += v[i].first;
      }
      ans[v[i].second] = make_pair(x, y);
      x += v[i].first;
    }
    cout << "Case #" << t << ':';
    REP(i,N) {
      printf(" %.1f %.1f", ans[i].first, ans[i].second);
    }
    cout << endl;
  }

  return 0;
}
