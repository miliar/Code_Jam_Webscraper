#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <sstream>
#include <cmath>
using namespace std;

#define mp make_pair
#define pb push_back

const int inf = 1000 * 1000 * 1000;

typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> vll;
typedef set<int> si;

template<typename T>
void readvector(int N, vector<T> &v, istringstream& iss = cin) {
  v.clear();
  v.resize(N);
  for (int i = 0 ; i < N ; i++)
    iss >> v[i];
}

int N;
struct plant {
  int x,y,r;
};
vector<plant> pl;

double dd(plant a, plant b) {
  double res = 0;
  res += pow(double(a.x - b.x), 2);
  res += pow(double(a.y - b.y), 2);
  return sqrt(res);
}

double go() {
  if (N == 1) {
    return pl[0].r;
  }
  if (N == 2) {
    return max(pl[0].r, pl[1].r);
  }
  
  double best = inf;
  for (int x = 0 ; x < 8 ; x++) {
    double R;
    if (__builtin_popcount(x) != 2) continue;
    plant a,b;
    bool first = true;
    for (int i = 0 ; i < 3 ; i++) {
      if ((x>>i)&1) {
	if (first) {
	  first = false;
	  a = pl[i];
	} else
	  b = pl[i];
      } else R = pl[i].r;
    }
    R = max(R, (dd(a,b) + a.r + b.r) / 2);
    if (R < best) best = R;
  }
  return best;
}

int main() {
  int T; cin>>T; cin.ignore();
  for (int test = 1 ; test <= T ; test++) {
    pl.clear();
    cin >> N;
    for (int i = 0 ; i < N ; i++) {
      plant p;
      cin >> p.x >> p.y >> p.r;
      pl.pb(p);
    }
    double res = go();    
    cout << "Case #" << test << ": " << res << endl;
  }
}
