#include <limits.h>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
#include <map>
#include <stack>
struct Node {
  int B, E, W;
  bool operator<(const Node& rhs) const
  {
    return W < rhs.W;
  }
};
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int X, S, R, t, N;
    std::cin >> X >> S >> R >> t >> N;
    std::vector<Node> nv(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> nv[i].B >> nv[i].E >> nv[i].W;
    }
    std::sort(nv.begin(), nv.end());
    std::vector<std::pair<int, int> > v(N);
    int evt = 0;
    for(int i = 0; i < N; ++i) {
      v[i].first = nv[i].W;
      v[i].second = nv[i].E-nv[i].B;
      evt += v[i].second;
    }
    double now = 0;
    int len = 0;
    double next = (double)(X-evt)/R;
    if(next > t) {
      double l = t*R;
      now += t;
      now += (double)(X-evt-l)/S;
    } else {
      now = next;
    }
    for(int i = 0; i < N; ++i) {
      double next = now+(double)v[i].second/(v[i].first+R);
      if(next > t) {
        if(t > now) {
          double r = t-now;
          double l = r*(v[i].first+R);
          now += r;
          now += (v[i].second-l)/(v[i].first+S);
        } else {
          now += (double)v[i].second/(v[i].first+S);
        }
        len += v[i].second;
        for(int j = i+1; j < N; ++j) {
          now += (double)v[j].second/(v[j].first+S);
          len += v[j].second;
        }
        break;
      } else {
        now = next;
        len += v[i].second;
      }
    }
    std::cout << "Case #" << test << ": " << std::fixed << std::setprecision(9) << now << std::endl;
  }
}
