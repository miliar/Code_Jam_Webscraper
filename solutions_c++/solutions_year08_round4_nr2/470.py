#include <iostream>

using namespace std;

void foo(int idx) {
  long long n, m, A;
  cin >> n >> m >> A;
  
  for(long long x1 = 0; x1 <=n; ++x1) {
    for(long long y1 = 0; y1 <= m; ++y1) {
      for(long long x2 = x1; x2 <= n; ++x2) {
        for(long long y2 = 0; y2 <= m; ++y2) {
          long long t1 = x2 * y1 - x1 * y2;
          long long t2 = y2 - y1;
          long long t4 = x1 - x2;
          for(long long x3 = x2; x3 <= n; ++x3) {
            long long t3 = t1 + x3 * t2;
            if(t4 == 0 and (A== t3) or (A==-t3)) {
              long long y3 = 0;
              if(y3 >= 0 and y3 <= m) {
                cout << "Case #" << idx << ": " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << '\n';
                return;
              }
            }

            if(t4 == 0) continue;

            if((A-t3) % t4 == 0) {
              long long y3 = (A-t3)/t4;
              if(y3 >= 0 and y3 <= m) {
                cout << "Case #" << idx << ": " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << '\n';
                return;
              }

            }

            if((-A-t3)%t4 == 0) {
              long long y3 = (-A-t3)/t4;
              if(y3 >= 0 and y3 <= m) {
                cout << "Case #" << idx << ": " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << '\n';
                return;
              }

            }
          }
        }
      }
    }
  }
    cout << "Case #" << idx << ": IMPOSSIBLE\n";
  
}


int main() {
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    foo(i+1);
  }
}
