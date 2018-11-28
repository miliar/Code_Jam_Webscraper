#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>

const int maxn = 200;

bool sp[maxn][maxn], rem[maxn][maxn];
char sps[maxn][maxn];
std::string s;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  
  int t, n;
  
  std::cin >> t;
  for (int tnum = 0; tnum < t; ++tnum) {
    int c, d;
    std::string cs = "", ds = "", ns = "";
    std::cin >> c;
    std::memset(rem, false, sizeof(rem));
    std::memset(sp, false, sizeof(sp));
    for (int i = 0; i < c; ++i) {
      std::cin >> cs;
      sp[cs[0]][cs[1]] = true;
      sps[cs[0]][cs[1]] = cs[2];
      sp[cs[1]][cs[0]] = true;
      sps[cs[1]][cs[0]] = cs[2];
    }
    std::cin >> d;
    for (int i = 0; i < d; ++i) {
      std::cin >> ds;
      rem[ds[0]][ds[1]] = true;
      rem[ds[1]][ds[0]] = true;
    }
    std::cin >> n;
    if (n > 0) {
      std::cin >> ns;
    }
    s = "";
    for (int i = 0; i < n; ++i) {
      s = s + ns[i];
      int len = s.length()-1;
      if (len > 0 && sp[s[len-1]][s[len]]) {
        char cc = sps[s[len-1]][s[len]];
        s.erase(s.end()-2, s.end());
        s = s + cc;
      }
      for (int i = 0; i < len; ++i) {
        if (rem[s[i]][s[len]]) {
          s = "";
          break;
        }
      }
    }
    std::cout << "Case #" << tnum+1 << ": [";
    for (int i = 0; i < int(s.length())-1; ++i) {
      std::cout << s[i] << ", ";
    }
    if (s.length() > 0) {
      std::cout << s[s.length()-1];
    }
    std::cout << "]" << std::endl;
  }
  return 0;
}