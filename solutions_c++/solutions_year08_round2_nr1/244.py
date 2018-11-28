#include <iostream>
#include <complex>
#include <set>
#include <vector>
using namespace std;

typedef long long ll;

struct point {
  ll x, y;

  point(ll x, ll y) : x(x), y(y) {}

  bool operator<(const point &o) const {
    if (x == o.x) {
      return y < o.y;
    } else {
      return x < o.x;
    }
  }
};

int main() {
  int N;
  cin >> N;
  for (int casenum=1; casenum<=N; casenum++) {
    int n, A, B, C, D, x0, y0, M;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

    set<point> trees;
    vector<point> treev;

    ll X = x0;
    ll Y = y0;
    trees.insert(point(X, Y));
    treev.push_back(point(X, Y));

    for (int i=1; i<n; i++) {
      X = (A*X + B) % M;
      Y = (C*Y + D) % M;
      trees.insert(point(X, Y));
      treev.push_back(point(X, Y));
    }

    //for (int i=0; i<n; i++) {
    //  cout << treev[i].x << " " << treev[i].y << endl;
    //}

    int ans = 0;

    for (int i=0; i<n; i++) {
      for (int j=i+1; j<n; j++) {
	for (int k=j+1; k<n; k++) {

	  point a = treev[i];
	  point b = treev[j];
	  point c = treev[k];

	  ll x = a.x + b.x + c.x;
	  ll y = a.y + b.y + c.y;

	  if ((x % 3 == 0) && (y % 3 == 0)) {
	    ans++;
	  }
	}
      }
    }

    cout << "Case #" << casenum << ": " << ans << endl;
  }

  return 0;
}
