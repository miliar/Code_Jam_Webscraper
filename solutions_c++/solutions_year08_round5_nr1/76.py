#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
bool between(double x, int a, int b) {
  return (a <= x && x <= b) || (b <= x && x <= a);
}
int main() {
  int cases;
  cin >> cases;
  for (int caseno=1; caseno<=cases; caseno++) {
    int L;
    cin >> L;

    vector<pair<int, pair<int, int> > > horiz, vert;

    int dx[] = {0, 1, 0, -1}, dy[] = {-1, 0, 1, 0};
    int dir = 0;
    int x = 0, y = 0, px = 0, py = 0;
    for (int i=0; i<L; i++) {
      string S;
      int T;
      cin >> S >> T;
      for (int t=0; t<T; t++) {
        for (int j=0; j<S.length(); j++) {
          if (S[j] == 'F') {
            x = x + dx[dir];
            y = y + dy[dir];
          } else if (S[j] == 'R' || S[j] == 'L') {
            if (x != px) {
              assert (y == py);
              horiz.push_back(make_pair(y, make_pair(x, px)));
            } else {
              assert (x == px);
              vert.push_back(make_pair(x, make_pair(y, py)));
            }
            px = x; py = y;
            if (S[j] == 'R') {
              dir = (dir + 1) % 4;
            } else {
              dir = (dir + 3) % 4;
            }
          }
        }
      }
    }
    if (x != px) {
      assert (y == py);
      horiz.push_back(make_pair(y, make_pair(x, px)));
    } else {
      assert (x == px);
      vert.push_back(make_pair(x, make_pair(y, py)));
    }
    if (x != 0 || y != 0) cout << "ERR" << " " << x << " " << y << endl;

    sort(vert.begin(), vert.end());
    sort(horiz.begin(), horiz.end());

    int tot = 0;
    for (int y=-103; y<=103; y++) {
      for (int x=-103; x<=103; x++) {
        double xx = x + 0.5, yy = y + 0.5;
        int vcnt0 = 0, vcnt1 = 0;
        for (int i=0; i<vert.size(); i++) {
          if (vert[i].first < xx && between(yy, vert[i].second.first, vert[i].second.second)) vcnt0++;
          if (vert[i].first > xx && between(yy, vert[i].second.first, vert[i].second.second)) vcnt1++;
        }
        int hcnt0 = 0, hcnt1 = 0;
        for (int i=0; i<horiz.size(); i++) {
          if (horiz[i].first < yy && between(xx, horiz[i].second.first, horiz[i].second.second)) hcnt0++;
          if (horiz[i].first > yy && between(xx, horiz[i].second.first, horiz[i].second.second)) hcnt1++;
        }
        if (
          (vcnt0 > 0 && vcnt0 % 2 == 0 && vcnt1 > 0 && vcnt1 % 2 == 0) 
          ||
          (hcnt0 > 0 && hcnt0 % 2 == 0 && hcnt1 > 0 && hcnt1 % 2 == 0)
          )
        {
          tot++;
        }
      }
    }

    int res = tot;
    cout << "Case #" << caseno << ": " << res << endl;
  }
}
