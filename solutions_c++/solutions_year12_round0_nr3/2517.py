#include <string>
#include <map>
#include <iostream>
#include <set>

using namespace std;

int main() {
  freopen("C-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t = 0; 
  cin >> t;
  for(int i = 0; i < t; ++i) {
    int a, b;
    int ans = 0;
    cin >> a >> b;
    for(int n = a; n < b; ++n) {
      int st = 1;
      int sti = 0;
      while(st <= n) {
        st *= 10;
        ++sti;
      }
      sti--;
      st/=10;
      int ns = 10;
      set<int> used;
      for(int q = 0; q < sti; ++q) {
        int e = ns;
        int t = st/ns;
        int m = (n % e)* t * 10 + n / e;
        if(m >= sti && m > n && m <= b && used.find(m) == used.end()) {
          ++ans;
          used.insert(m);
        }
        ns*= 10;
      }
    }

    cout << "Case #" << i+1 << ": " << ans << endl;
  }

  return 0;
}
