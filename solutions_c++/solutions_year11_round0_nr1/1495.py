#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int solve() {
  char c;
  int B, b, pb = 1, po = 1, tb = 0, to = 0, tt = 0;
  cin >> B;
  while (B--) {
    cin >> c >> b;
    if (c == 'O') {
      int dis = abs(po - b);
      if (dis > to) {
        tt += abs(dis - to);
        tb += abs(dis - to);
        to = 0;
        po = b;
      } else {
        to -= dis;
        po = b;
      }
      tt++; tb++; to = 0;
    } else {
      int dis = abs(pb - b);
      if (dis > tb) {
        tt += abs(dis - tb);
        to += abs(dis - tb);
        tb = 0;
        pb = b;
      } else {
        tb -= dis;
        pb = b;
      }
      tt++; to++; tb = 0;
    }
  }
  return tt;
}
int main() {
  int T, i = 0;
  cin >> T;
  while (i++ < T) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}

