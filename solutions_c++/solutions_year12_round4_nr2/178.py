#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <cmath>
#include <complex>
#include <ctime>
#include <cstdlib>

using namespace std;

typedef long long int LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VP;

typedef pair<double, double> point;

const double EPS = 1E-2;

double dist(const point &p, const point &q) {
  double dx = p.first - q.first;
  double dy = p.second - q.second;
  return sqrt(dx*dx + dy*dy);
  }

double randV(double r) {
  double x = rand();
  x *= double(RAND_MAX)+1; x += rand();
  x /= double(RAND_MAX)+1;
  x /= double(RAND_MAX)+1;

  double v = r*x;
  if (v < 0) v = 0;
  if (v > r) v = r;
  
  return v;
  }

bool randomPlace(int n, int w, int l, const VI &radii, vector<point> &pos, int cur = 1) {
  if (cur == n)
    return true;
  pos[cur].first = randV(w);
  pos[cur].second = randV(l);

  for (int i = 0; i < cur; ++i)
    if (dist(pos[i], pos[cur]) <= (radii[i] + radii[cur] + EPS))
      return false;

  for (int i = 0; i < 10; ++i)
    if (randomPlace(n, w, l, radii, pos, cur+1))
      return true;
  return false;
  }

vector<point> placeDiscs(int n, int w, int l, VI &radii) {
  vector<point> pos(n); pos[0] = point(0, 0);

  while (!randomPlace(n, w, l, radii, pos));

  return pos;
  }

int main() {
  srand(time(0));
  cout << fixed << setprecision(3);
  int nc; cin >> nc;
  for (int cur = 1; cur <= nc; ++cur) {
    int n, w, l; cin >> n >> w >> l;

    VI radii(n);
    for (int i = 0; i < n; ++i)
      cin >> radii[i];

    vector<point> pos = placeDiscs(n, w, l, radii);
    cout << "Case #" << cur << ":";
    for (int i = 0; i < n; ++i)
      cout << ' ' << pos[i].first << ' ' << pos[i].second;
    cout << '\n';
    }
  }

