#include <cstdio>
#include <iostream>

using namespace std;

#define sz(x) ((int)(x).size())

const int maxn = 5 * 10000 * 1000 + 5;
int used[maxn];
int shft = 0;

int main()
{
  freopen("C.in", "r", stdin);
  
  int t; cin >> t;
  
  for (int i = 0; i < t; ++i) {
    int a, b; cin >> a >> b;
    int res = 0;
    for (int j = a; j <= b; ++j) {
      ++shft;
      string s = "";
      int x = j;
      while (x) {
        s += x % 10;
        x /= 10;
      }
      
      for (int q = 0; q < sz(s) - 1; ++q) {
        s = s.substr(1, sz(s) - 1) + s[0];
        int x = 0;
        for (int l = sz(s) - 1; l >= 0; --l) {
          x *= 10;
          x += s[l];
        }
        
        if (used[x] != shft && x < j && a <= x && x <= b) {
          used[x] = shft;
          ++res;
        }
      }
    }
    
    cout << "Case #" << i + 1 << ": " << res << '\n';
  }
  
  
  
  return 0;
}