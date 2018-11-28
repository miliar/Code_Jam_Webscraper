#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
#define ALL(a)  (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
const double EPS = 1e-10;
const double PI  = acos(-1.0);
#define dump(x) cerr << "  (L" << __LINE__ << ") " << #x << " = " << (x) << endl;
#define dumpv(x) cerr << "  (L" << __LINE__ << ") " << #x << " = "; REP(q,(x).size()) cerr << (x)[q] << " "; cerr << endl;
template<typename T1, typename T2>
ostream& operator<<(ostream& s, const pair<T1, T2>& d) {return s << "(" << d.first << "," << d.second << ")";}

bool solve(int N, vector<int>& d, vector<int>& l, int D) {
  vector<int> reach(N, 0);
  reach[0] = d[0];
  REP(i, N) {
    for (int j = i+1; j < N; j++) {
      if (d[j] <= d[i] + reach[i]) {
        reach[j] = max(reach[j], min(l[j], d[j]-d[i]));
      } else {
        break;
      }
    }
    if (d[i] + reach[i] >= D) return true;
  }
  return false;
}

int main() {
  int T; cin >> T;
  REP(t, T) {
    int N; cin >> N;
    vector<int> d(N), l(N);
    REP(i, N) cin >> d[i] >> l[i];
    int D; cin >> D;

    bool ans = solve(N, d, l, D);
    cout << "Case #" << (t+1) << ": " << (ans ? "YES" : "NO") << endl;
  }
}

