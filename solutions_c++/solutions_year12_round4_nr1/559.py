#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <climits>

using namespace std;

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define SZ size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1000000000;
const double EPS = 1e-10;

int T;
int n, D;
int ds[10000], ls[10000];

int memo[10000];

bool dfs(int cvine, int clen) {
  int maxd = ds[cvine] + clen;
  if(D <= maxd) return true;

  for(int x = cvine+1; x < n && ds[x] <= maxd; x++) {
    int len = min(ls[x], ds[x] - ds[cvine]);

    if(memo[x] > len) {}
    else if(dfs(x, len)) return true;
    else {
      memo[x] = len;
    }
  }

  return false;
}

int main()
{
  cin >> T;
  REP(ncase, T) {
    cin >> n;
    REP(i, n) cin >> ds[i] >> ls[i];
    cin >> D;

    REP(i, n) memo[i] = -1;
    
    int cvine = 0;
    int clen = min(ds[0], ls[0]);
   
    if(dfs(cvine, clen)) printf("Case #%d: YES\n", ncase+1);
    else printf("Case #%d: NO\n", ncase+1);
  }
  
  return 0;
}
