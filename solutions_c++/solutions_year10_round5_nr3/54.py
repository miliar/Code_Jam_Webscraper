#include <iostream>
#include <map>
using namespace std;

long long steps(int n) {
  n /= 2;

  long long res = 1;
  res *= n;
  res *= n+1;
  res *= 2*n+1;
  res /= 6;
  return res;
}

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    int n; cin >> n;
    map<int, int> p;
    for(int i = 0; i < n; i++) {
      int x, y;
      cin >> x >> y;
      p[x] = y;
    }

    long long res = 0;
    while(true) {
      bool done = true;
      for(map<int, int>::iterator it = p.begin(); it != p.end(); ++it) {
        if(it->second >= 2) {
          res += steps(it->second);
          for(int i = 1; 2*i <= it->second; i++) {
            p[it->first-i]++;
            p[it->first+i]++;
          }

          if(it->second % 2 == 0)
            p.erase(it->first);
          else
            p[it->first] = 1;

          done = false;
          break;
        }
      }
      if(done) break;
    }

    printf("Case #%d: %lld\n", c, res);
  }

  return 0;
}
