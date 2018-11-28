#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>

using namespace std;

typedef long long ll;
double dist (double x1, double y1, double x2, double y2) {
  return sqrt ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main() {
  int num_cases;
  cin >> num_cases;
  cin.ignore();
  
  for (int case_num = 1; case_num <=  num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    int n;
    cin >> n;
    vector<pair<pair<int,int>, int> > plants;
    for (int i = 0; i < n; ++i) {
      int x,y,r;
      cin >> x >> y >> r;
      plants.push_back (make_pair (make_pair (x,y),r));
    }
    if (n==1) {
      cout << plants[0].second << "\n";
    }
    if (n==2) {
      cout << max (plants[0].second, plants[1].second) << "\n";
    }
    if (n==3) {
      double ret = numeric_limits<double>::max();
      ret = min (ret, max (0.5*(dist (plants[0].first.first, plants[0].first.second,
                                 plants[1].first.first, plants[1].first.second) 
                            + plants[0].second + plants[1].second),
                           (double)plants[2].second));
      ret = min (ret, max (0.5 * (dist (plants[0].first.first, plants[0].first.second,
                                 plants[2].first.first, plants[2].first.second) 
                                  + plants[0].second + plants[2].second),
                           (double)plants[1].second));
      ret = min (ret, max (0.5 * (dist (plants[2].first.first, plants[2].first.second,
                                 plants[1].first.first, plants[1].first.second) 
                                  + plants[2].second + plants[1].second),
                           (double)plants[0].second));
      cout << fixed << setprecision (10) << ret << "\n";
    }
    if (n>3) cout << "err\n";
  }
  
}
