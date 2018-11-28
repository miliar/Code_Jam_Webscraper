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

int nc[20000][2];
int v[20000];
int c[20000];
bool solve(int P) {
  int M,V;
  scanf("%d%d",&M,&V);
  for (int i = 0; i < (M-1)/2; ++i) {
    scanf("%d%d",v+i,c+i);
  }
  for (int i = 0; i < (M+1)/2; ++i) {
    int a;
    scanf("%d",&a);
    nc[i+(M-1)/2][0] = (100000)*(a);
    nc[i+(M-1)/2][1] = (100000)*(!a);
    //cout << "i=" << i+(M-1)/2 << ":" << nc[i+(M-1)/2 ][1] << endl;
    //cout << a << endl;
  }
  for (int i = (M-1)/2-1; i >= 0; --i) {
    if (c[i]) {
      nc[i][1] = min(nc[2*i+1][1]+nc[2*i+1+1][1]+!v[i],min(nc[2*i+1][1],nc[2*i+1+1][1])+v[i]);
      nc[i][0] = min(min(nc[2*i+1][0],nc[2*i+1+1][0])+!v[i],nc[2*i+1][0]+nc[2*i+1+1][0]+v[i]);
    } else {
      if (v[i]) {
	nc[i][1] = nc[2*i+1][1]+nc[2*i+1+1][1];
	nc[i][0] = min(nc[2*i+1][0],nc[2*i+1+1][0]);
      } else {
	nc[i][1] = min(nc[2*i+1][1],nc[2*i+1+1][1]);
	nc[i][0] = nc[2*i+1][0]+nc[2*i+1+1][0];
      }
    }
    //cout << "i=" << i << ":" << nc[i][1] << endl;
  }
  printf("Case #%d: ",P+1);
  if (nc[0][V] >= 100000)
    puts("IMPOSSIBLE");
  else {
    printf("%d\n",nc[0][V]);
  }

  return true;
}

int main() {
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%i", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
