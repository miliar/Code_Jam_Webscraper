#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;

const int DBG = 0, INF = int(1e9);

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

bool quick(int x, int v, int B, int T) {
  return B - x <= v * T;
}

int solve(vector<PII> &V, int K, int B, int T) {
  if (K == 0)
    return 0;

  if (V.size() < K)
    return -INF;
  if (V.size() == 0)
    return 0;

  int a = V.back().ST, b = V.back().ND;

  V.pop_back();

  if (quick(a,b,B,T)) 
    return solve(V,K - 1,B,T);
  else
    return solve(V,K,B,T) + K;
}

int main() {
  ios_base::sync_with_stdio(0);

  int C;

  scanf("%d", &C);

  REP(q,C) {

    int N, K, B, T;

    scanf("%d %d %d %d", &N, &K, &B, &T);

    vector<PII> V(N);

    REP(i,N) 
      scanf("%d", &V[i].ST);

    REP(i,N)
      scanf("%d", &V[i].ND);

    int res = solve(V, K, B, T);

    if (res < 0)
      printf("Case #%d: IMPOSSIBLE\n", q + 1);
    else
      printf("Case #%d: %d\n", q + 1, res);

  }

  return 0;
}
