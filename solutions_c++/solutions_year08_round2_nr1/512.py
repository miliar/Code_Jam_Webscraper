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


bool solve(int P) {
  ll n,A,B,C,D,x,y,M;
  scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&x,&y,&M);
  int v[3][3];
  Rep(i,3) Rep(j,3) v[i][j] = 0;
  v[y%3][x%3]++;
  for (int i = 1; i < n; ++i) {
    x =(A*x+B)%M;
    y = (C*y+D)%M;
    //cout << x << " " << y << endl;
    v[y%3][x%3]++;
  }
  ll res = 0;
  Rep(x1,3) Rep(y1,3) {
    //cout << v[x1][y1] << " ";
    Rep(x2,3) Rep(y2,3) {
      int y3=(6-y1-y2)%3, x3=(6-x1-x2)%3;
      if (x1==x2 && y1==y2 && x1==x3 && y1==y3) {
	int a = v[y1][x1];
	res += a*(a-1)*(a-2);
      }
      else if (x1==x2 && y1==y2) {
	res += v[x1][y1]*(v[x1][y1]-1)*(v[x3][y3]);
      } else if (x1==x3 && y1==y3)
        res +=  v[x1][y1]*(v[x1][y1]-1)*(v[x2][y2]);
      else if (x2==x3 && y2==y3)
        res +=  v[x2][y2]*(v[x2][y2]-1)*(v[x1][y1]);
      else
        res +=  v[x1][y1]*v[x2][y2]*v[x3][y3];
    }
  }
  printf("Case #%d: %lld\n",P+1,res/6);
  return true;
}

int main() {
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%i", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
