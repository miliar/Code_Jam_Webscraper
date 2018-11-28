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
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef long long ll;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-9)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}


int ncases;

char novo[256][256];
bool out[256][256];

int main() {
  cin >> ncases;
  FOR(kk,ncases) {
    printf("Case #%d: ",kk);
    memset(novo,0,sizeof(novo));
    memset(out,0,sizeof(out));
    int c,d;
    string a;
    cin >> c;
    FOR(i,c) {
      cin >> a;
      novo[a[0]][a[1]] = novo[a[1]][a[0]] = a[2];
    }
    cin >> d;
    FOR(i,d) {
      cin >> a;
      out[a[0]][a[1]] = out[a[1]][a[0]] = true;
    }
    vector<char> ans;
    int n;
    cin >> n;
    cin >> a;
    int sz = 0;
    FOR(i,n) {
      ans.pb(a[i]);
      sz++;
      while (sz >= 2 && novo[ans[sz-1]][ans[sz-2]]) {
        ans[sz-2] = novo[ans[sz-1]][ans[sz-2]];
        ans.pop_back();
        sz--;
      }
      FOR(j,sz-1) if (out[ans[j]][ans[sz-1]]) {
        ans.clear();
        sz = 0;
        break;
      }
      // FOR(j,sz) {
      //   cout << ans[j] << ", ";
      // }
      // cout << endl;
    }
    cout << '[';
    if (sz) cout << ans[0];
    for (int i = 1; i < sz; i++) cout << ", " << ans[i];
    cout << ']' << endl;
  }
  return 0;
}
