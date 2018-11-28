#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
using namespace std;

#define X first
#define Y second
#define PB push_back

typedef long long ll;
typedef long long ent;
typedef pair<int, int> P;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef vector<Vp> Mp;

typedef queue<int> Q;
typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

const int INF = 1000000000;

ll gcd(ll a, ll b) {
  if (b == 0) return a;
  return gcd(b, a%b);
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    ll N, Pd, Pg;
    cin >> N >> Pd >> Pg;
    cout << "Case #" << cas << ": ";
    if (Pg == 100 and Pd != 100) {
      cout << "Broken" << endl;
      continue;
    }
    if (Pg == 0 and Pd != 0) {
      cout << "Broken" << endl;
      continue;
    }
    if (100/gcd(100, Pd) <= N) cout << "Possible" << endl;
    else cout << "Broken" << endl;
  }
}
