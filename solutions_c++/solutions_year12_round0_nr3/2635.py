#include <cstdio>
#include <iostream>

using namespace std;

int getl(int a) {
  int cnt = 0;
  while (a > 0) {
    cnt++;
    a /= 10;
  }
  return cnt;
}

int was[2100000];
int save[100];

int main() {
  int t;
  cin >> t;
  
  for (int tl = 0; tl < t; tl++) {
    int l, r;
    cin >> l >> r;
    int ans = 0;
    for (int i = l + 1; i <= r; i++) {
      int sv = 0; int td = 1;
      for (int t = 1; t < getl(i); t++) {
        td *= 10;
        int b = i % td;
        if (getl(b) != t) continue;
        int a = i / td;
        for (int j = 0; j < getl(a); j++) b *= 10;
        b += a;
        if (b >= l && b < i && !was[b]) {
          save[sv] = b;
          sv++;
          was[b] = 1;
          ans++;
        }
      }
      for (int t = 0; t < sv; t++) was[save[t]] = 0;
    }
    cout << "Case #" << tl + 1 << ": " << ans << endl;
  }
  
  return 0;
}