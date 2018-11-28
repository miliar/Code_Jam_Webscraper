#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define X first
#define Y second
#define PB push_back
#define FOR(x,y) for (int x = 0; x < int(y); ++x)
#define debug(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef vector<Vp> Mp;
typedef vector<string> Vs;
typedef vector<Vs> Ms;

typedef queue<int> Q;
typedef priority_queue<int> PQ;
typedef stack<int> STACK;
typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

template <class Ta, class Tb> inline Tb cast(Ta a) { SS ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const int INF = 1000000000;
const int MOD = 1000000007;
const int diri[8] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dirj[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cerr << "RUNNING CASE " << cas << endl;
    int n;
    cin >> n;
    
    Vp v(n);
    for (int i = 0; i < n; ++i)
      cin >> v[i].X >> v[i].Y;
    
    int d;
    cin >> d;
    
    bool res = false;
    
    Vi dist(n, -1);
    dist[0] = v[0].X;
    
    for (int i = 0; i < n; ++i) {
      if (dist[i] == -1) break;
      if (v[i].X + dist[i] >= d) {
        res = true;
        break;
      }
      
      for (int j = i + 1; j < n; ++j) {
        if (v[i].X + dist[i] < v[j].X) break;
        dist[j] = max(dist[j], min(v[j].Y, v[j].X - v[i].X));
      }
    }
    
    cout << "Case #" << cas << ": ";
    if (res) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
}
