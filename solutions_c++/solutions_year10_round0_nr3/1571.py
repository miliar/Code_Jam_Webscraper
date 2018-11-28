#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <sstream>
#include <iterator>

//std::cin.ignore();

static std::string encode(const std::deque<int>& d)
{
  std::stringstream ss;
  std::copy(d.begin(), d.end(), std::ostream_iterator<int>(ss, ","));
  return ss.str();
}

int main() {
  int T;
  std::cin >> T;
  for(int tt = 1; tt <= T; ++tt) {
    int R, k, N;
    std::cin >> R >> k >> N;
    std::deque<int> gs;
    std::deque<int> is;
    for(int i = 0; i < N; ++i) {
      int g;
      std::cin >> g;
      gs.push_back(g);
      is.push_back(i);
    }
    std::map<std::string, long long int> cache;
    std::map<std::string, int> rcache;
    long long int score = 0;
    bool flag = true;
    for(int r = 1; r <= R; ++r) {
      std::string key = encode(is);
      if(flag) {
        std::map<std::string, long long int>::const_iterator ci = cache.find(key);
        if(ci != cache.end()) {
          int interval = r-rcache[key];
          int remaining = R-r-1;
          long long int intervalscore = score-(*ci).second;
          score += remaining/interval*intervalscore;
          r += remaining/interval*interval;
          flag = false;
        } else {
          cache[key] = score;
          rcache[key] = r;
        }
      }
      int m = k;
      std::deque<int> gst;
      std::deque<int> ist;
      while(!gs.empty() && m-gs[0] >= 0) {
        gst.push_back(gs[0]);
        ist.push_back(is[0]);
        score += gs[0];
        m -= gs[0];
        gs.pop_front();
        is.pop_front();
      }
      gs.insert(gs.end(), gst.begin(), gst.end());
      is.insert(is.end(), ist.begin(), ist.end());
    }
    std::cout << "Case #" << tt << ": " << score << std::endl;
  }
}

    // std::cout << "Case #" << n << ": " << std::setfill('0')
    //           << std::setw(4) << X << std::endl;
