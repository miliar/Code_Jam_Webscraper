#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <queue>
#include <cstring>
using namespace std;

#define loop(i,n) for (int i = 0; i < (int)(n); ++i)
#define Bounded(x,a,b) ((a) <= (x) && (x) <= (b))
#define db(x) #x << " = " << x
#define pdb(x) printf("#x = %d\n",x);
#define All(x) x.begin(),x.end()
#define sz(x) x.size()
typedef vector<int> Vi;
typedef pair<int,int> Pii;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;

void solve(int casenum) {
  cout << "Case #" << casenum << ":" << endl;
  int n; cin >> n;
  vector<string> a(n);
  loop(i,n) cin >> a[i];

  typedef vector<double> Vd;

  Vi wins(n,0), ops(n,0);
  loop(i,n) loop(j,n)
    wins[i] += a[i][j]=='1', ops[i] += a[i][j] != '.';

  Vd owp(n);
  loop(i,n) {
    loop(j,n)
      if (a[i][j] != '.')
        owp[i] += (wins[j] - (a[i][j]=='0')) / (double)(ops[j]-1);
    owp[i] /= ops[i];
  }

  Vd oowp(n);
  loop(i,n) {
    loop(j,n) if (a[i][j] != '.') oowp[i] += owp[j];
    oowp[i] /= ops[i];
  }

  vector<double> rpi(n);
  loop(i,n)
    rpi[i] = 0.25 * (wins[i]/(double)ops[i]) + 0.5 * owp[i] + 0.25 * oowp[i];

  loop(i,n)
    printf("%.10f\n", rpi[i]);
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}

