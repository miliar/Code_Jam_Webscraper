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

int N, S, M, V[200];
int maxim[50][2];
int dp[200][200];

int main() {
  for (int n = 0; n < 50; ++n) {
    maxim[n][0] = maxim[n][1] = -1;
    for (int i = 0; i <= n; ++i)
      for (int j = i; i + j <= n; ++j) {
        int k = n - i - j;
        if (j <= k and k - i <= 2) {
          int t = (k - i == 2 ? 1 : 0);
          maxim[n][t] = max(maxim[n][t], k);
        }
      }
  }
  
//   for (int n = 0; n < 50; ++n) cerr << maxim[n][0] << " " << maxim[n][1] << endl;
  
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> N >> S >> M;
    for (int i = 0; i < N; ++i) cin >> V[i];
    
    for (int s = 0; s < S; ++s) dp[N][s] = -INF;
    dp[N][S] = 0;
    
    for (int n = N - 1; n >= 0; --n)
      for (int s = 0; s <= S; ++s) {
        dp[n][s] = dp[n + 1][s] + (M <= maxim[V[n]][0] ? 1 : 0);
        if (s < S and maxim[V[n]][1] != -1)
          dp[n][s] = max(dp[n][s], dp[n + 1][s + 1] + (M <= maxim[V[n]][1] ? 1 : 0));
      }
    
    cout << "Case #" << cas << ": " << dp[0][0] << endl;
  }
}
