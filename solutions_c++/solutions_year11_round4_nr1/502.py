#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
const double eps = 1e-9, INF = 2 * 1000 * 1000 * 1000;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int s, r, n, x, t; 
    cin >> x >> s >> r >> t >> n;
    vector<int> b, e, w;
    int last = 0;
    for (int i = 0; i < n; ++i) {
      int B, E, W;
      cin >> B >> E >> W;
      if (last != B) {
        b.push_back(last);
        e.push_back(B);
        w.push_back(0);
      }        
      last = E;
      b.push_back(B);
      e.push_back(E);
      w.push_back(W);
    }
    b.push_back(last);
    e.push_back(x);
    w.push_back(0);

    vector< pair<double, int> > tt;
    for (int i = 0; i < b.size(); ++i) {
      tt.push_back( make_pair( w[i], i ) );
    }
    sort(tt.begin(), tt.end());
    double dist = 0, time = 0;
   /* int ind = 0;
    for (ind = 0; ind < b.size(); ++ind) {
      double carry = ((double)e[ind] - b[ind]) / (r + w[ind]);
      if (time + carry - eps > t) {        
        dist += (t - time) * (r + w[ind]);
        time = t;
        break;
      }
      time += carry;
      dist = e[ind];
    }
    if (ind != b.size()) {
      for (int index = ind; index < b.size(); ++index) {
        time += (e[index] - dist) / (w[index] + s);
        dist = e[index];
      }
    }    */
    for (int i = 0; i < tt.size(); ++i) {
      if (time < t) {
        double carry = ((double)e[tt[i].second] - b[tt[i].second]) / (r + w[tt[i].second]);
        if (time + carry - eps > t) {          
          dist = b[tt[i].second] + (t - time) * (r + w[tt[i].second]);
          time = t + (e[tt[i].second] - dist) / (s + w[tt[i].second]);
          dist = e[tt[i].second];
        }
        else
        {
          time += carry;
          dist = e[tt[i].second];
        }
      }
      else
        time += ((double)e[tt[i].second] - b[tt[i].second]) / (s + w[tt[i].second]);
    }
    cout << fixed << setprecision(9) << "Case #" << test_index + 1 << ": " << time << endl;
  }
  return 0;
}
