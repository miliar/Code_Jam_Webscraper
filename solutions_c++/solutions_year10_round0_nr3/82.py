#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <numeric>
#include <limits.h>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-8)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}

typedef long long ll;

typedef pair<ll,int> pli;

set<pli> s[1100];
set<pli>::iterator it, it2;

ll v[1100];

ll memo[1100];
int next[1100];

int main() {
  int ntest;
  cin >> ntest;
  int kk = 1;
  while (ntest--) {
    memset(memo,-1,sizeof(memo));
    cerr << ntest << endl;
    cout << "Case #" << kk++ << ": ";
    ll r,k,n;
    cin >> r >> k >> n;
    FOR(i,n) cin >> v[i]; 
    FOR(i,n) {
      s[i].clear();
      ll sum = 0;
      FOR(j,n) {
        int id = (i+j)%n;
        sum += v[id];
        s[i].insert(pli(sum,id));
      }
    }
    ll res = 0;
    int id = 0;
    FOR(i,r) {
      // if (memo[id] != -1) {
      //   res += memo[id];
      //   id = next[id];
      //   continue;
      // }
      it = s[id].upper_bound(pli(k,2000));
      if (it == s[id].begin()) break;
      it2 = it;
      it2--;
      //cout << "A" << endl;
      //cout << it2->first << endl;
      //cout << it->second << endl;
      //cout << "B" << endl;
      memo[id] = it2->first;
      next[id] = it->second;
      res += it2->first;
      id = it->second;
    }
    cout << res << endl;
  }
  return 0;
}
