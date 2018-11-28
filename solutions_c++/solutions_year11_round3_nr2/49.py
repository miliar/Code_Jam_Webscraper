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
#include <assert.h>

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

int c;
vi a;
int n;
ll t;
int l;

vector<ll> eco;

int main() {
  int ncases;
  scanf("%d",&ncases);
  FOR(ccases,ncases) {
    a.clear();
    eco.clear();
    printf("Case #%d: ",ccases+1);
    cin >> l >> t >> n >> c;
    FOR(i,c) {
      int v;
      cin >> v;
      a.pb(v);
    }
    FOR(i,n-c) a.pb(a[i%c]);
    //FOR(i,n) cout << a[i] << endl;
    ll cost = 0;
    int first = -1;
    ll acc = 0;
    FOR(i,n) {
      if (cost + 2*a[i] > t) {
        first = i;
        break;
      }
      cost += 2*a[i];
    }
    FOR(i,n) acc += 2*a[i];
    //cerr << acc << endl;
    if (first == -1) cout << acc << endl;
    else {
      for (int i = first ; i < n; i++) {
        ll mid = max(0LL,t-cost);
        eco.pb(2*a[i] - (mid + a[i]-mid/2));
        cost += 2*a[i];
      }
      sort(ALL(eco),greater<ll>());
      FOR(i,min(l,SZ(eco))) acc -= eco[i];
      cout << acc << endl;
    }
  }
  return 0;
}
