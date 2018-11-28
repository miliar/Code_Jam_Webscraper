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
typedef long long ll;

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


#define MAX 10100

vi primes;
int v[11];
int d,k;

set<int> sol;

#define MOD(a,b) (((a)%(b) + (b))%(b))

void tenta(int a, int b, int p) {
  for (int i = 0; i < k-2; i++) {
    if (MOD(a*v[i+1]+b,p) != v[i+2]) return;
  }
  sol.insert(MOD(a*v[k-1]+b,p));
  //printf("SOL: %d %d %d: %d\n",a,b,p,MOD(a*v[k-1]+b,p));
}

void go(int p) {
  //cout << "tentando " << p << endl;
  if (k == 1) {
    FOR(a,p) {
      FOR(b,p) {
        if (sol.size() > 1) break;
        sol.insert(MOD(a*v[0] + b,p));
      }
    }
    return;
  }
  FOR(a,p) {
    tenta(a,MOD(v[1]-a*v[0],p),p);
    if (sol.size() > 1) return;
  }
}

int main() {
  primes.pb(2);
  for (int i = 3; i < MAX; i+=2) {
    bool ok = true;
    for (int j = 0; j < primes.size() && primes[j]*primes[j] <= i; j++) {
      if (i%primes[j] == 0) {
        ok = false;
        break;
      }
    }
    if (ok) primes.pb(i);
  }
  //FOR(i,primes.size()) cout << primes[i] << endl;
  int ncases;
  scanf("%d",&ncases);
  FOR(kk,ncases) {
    printf("Case #%d: ",kk+1);
    scanf("%d %d",&d,&k);
    FOR(i,k) scanf("%d",&v[i]);
    int minv = *max_element(v,v+k);
    int maxv = 1;
    FOR(i,d) maxv *= 10;
    sol.clear();
    for (int i = 0; i < primes.size() && primes[i] <= maxv; i++) {
      if (primes[i] > minv) go(primes[i]);
      if (sol.size() > 1) break;
    }
    if (sol.size() == 0 || sol.size() > 1) {
      cout << "I don't know." << endl;
    }
    else cout << *sol.begin() << endl;
  }  
  return 0;
}
