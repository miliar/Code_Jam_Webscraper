#include <cstdio>
#include <iostream>

using namespace std;

int m[1000];
int vl[1000];

int main() {
  int t;
  cin >> t;
  
  for (int tl = 0; tl < t; tl++) {
    int n, s, p;
    cin >> n >> s >> p;
    for (int i = 0; i < n; i++) cin >> m[i];
    for (int i = 0; i < n; i++)
      if (m[i] > 1 && s > 0) {
        if (m[i] % 3 == 0 && m[i] / 3 == p - 1) {
          s--;
          vl[i] = m[i] / 3 + 1;
        } else 
        if (m[i] % 3 == 2 && m[i] / 3 == p - 2) {
          s--;
          vl[i] = m[i] / 3 + 2;
        }
        else if (m[i] % 3 == 0) vl[i] = m[i] / 3; else vl[i] = m[i] / 3 + 1;
      } else
     if (m[i] <= 1) vl[i] = m[i]; else {
       if (m[i] % 3 == 0) vl[i] = m[i] / 3; else vl[i] = m[i] / 3 + 1;
     }
    int ans = 0;
    for (int i = 0; i < n; i++)
      if (vl[i] >= p) ans++;
    //for (int i = 0; i < n; i++) cout << vl[i] << " ";
    cout << "Case #" << tl + 1 << ": " << ans << endl;
  }
  
  return 0;
}