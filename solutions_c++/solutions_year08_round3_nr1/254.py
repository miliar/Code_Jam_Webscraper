//Ulf LundstrÅˆm

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
const enum {SIMPLE, FOR, WHILE} mode = FOR;

#define For(i,a,b) for (int i(a),_b(b); i < _b; ++i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define ever (;;)
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

bool solve(int P0) {
  int P,K,L;
  scanf("%d%d%d",&P,&K,&L);
  vi f(L);
  Rep(i,L)
    scanf("%d",&f[i]);
  sort(f.begin(),f.end());
  ll res = 0;
  Rep(i,L) {
    res += f[L-i-1]*(1+i/K);
    //cout << f[L-i-1]*(1+i/K) << endl;
  }
  printf("Case #%d: %lld\n",P0+1,res);

  return true;
}

int main() {
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%i", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
