#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

bool used[1100011];

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  string str;
  int X, S, R, N;
  double t;
  FOR (test, tests){
    cin >> X >> S >> R >> t >> N;
    vector<pair<int, pair<int, int> > > intervals;
    intervals.clear();
    int a, b, w;
    SET(used, 0);
    FOR (i, N){
      cin >> a >> b >> w;
      ffor (j, a, b)
        used[j] = true;
      intervals.pb(mp(w + S, mp(a, b)));
    }
    FOR (i, X)
      if (!used[i])
        intervals.pb(mp(S, mp(i, i + 1)));
    sort(all(intervals));
    double ret = 0.0;
    FOR (i, intervals.sz){
      double cs = intervals[i].first;
      double a = intervals[i].second.first;
      double b = intervals[i].second.second;
      double ll = (b - a) / (cs - S + R);
      ll = min(ll, t);
      t -= ll;
      ret += ll + (b - a - ll * (cs - S + R)) / cs;
    }
//    cout << t << endl;

    cout << "Case #" << (test + 1) << ": ";
    printf("%.11lf", ret);
    cout << "\n";
  }
  return 0;
}
