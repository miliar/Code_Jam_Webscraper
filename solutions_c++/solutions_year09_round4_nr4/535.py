#include<algorithm>
#include<cmath>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<utility>
#include<sstream>
#include<vector>
using namespace std;

template<class A, class B> void conv_(A& x, B& y) { stringstream s; s << x; s >> y; }

typedef unsigned int uint;
typedef unsigned long long int ullong;
#define for_(i, a, b) for(int i=(a);i<(b);++i)
#define set_(a, n) memset(a, n, sizeof a)

int main(void) {
  int t;
  cin >> t;

  for_(k, 1, t+1) {
    int n;
    cin >> n;

    int pl[n][3], mr = -1;
    for_(i, 0, n) { // x y r
      cin >> pl[i][0] >> pl[i][1] >> pl[i][2];
      mr = max(mr, pl[i][2]);
    }

    cout << "Case #" << k << ": ";

    if (n <= 2) {
      cout << mr << endl;
      continue;
    }

    int ch[3][3] = {{0, 1, 2}, {0, 2, 1}, {1, 2, 0}};
    double min_r = INT_MAX;

    for_(c, 0, 3) {
      int a = ch[c][0], b = ch[c][1], f = ch[c][2];
      //cout << "a = " << a << ' ';
      //cout << "B = " << b << endl;
      int dx = pl[a][0]-pl[b][0];
      int dy = pl[a][1]-pl[b][1];
      //cout << "Dx = " << dx << " dy = " << dy << endl;
      double calc = (sqrt(double(dx*dx + dy*dy))+pl[a][2]+pl[b][2])/2;

      min_r = min(min_r, max(double(pl[f][2]), calc));
      //cout << "Min_r = " << min_r << endl;
    }

    cout << min_r << endl;
  }

  return 0;
}
