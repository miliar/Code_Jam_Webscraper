//Ulf Lundström

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

char number[1000];
int L;

int read(int b, int e) {
  char tmp = number[e];
  number[e] = 0;
  ll res = 0;
  sscanf(number+b,"%lld",&res);
  number[e] = tmp;
  return res%210;
}

ll v[50][50][210];
void V(int b, int e) {
  if (v[b][e][0] == -1) {
    Rep(i,210) v[b][e][i] = 0;
    if (b==e) {
      v[b][e][0]=1;
      return;
    }
    for (int i = b+1; i < e; ++i) {
      int a = read(i,e);
      V(b,i);
      Rep(j,210) {
	v[b][e][(j+a)%210] += v[b][i][j];
	v[b][e][(j-a+210)%210] += v[b][i][j];
      }
    }
    v[b][e][read(b,e)]++;
  }
}

bool solve(int P) {
  scanf("%s",number);
  L = strlen(number);
  Rep(i,L+1) Rep(j,L+1) v[i][j][0] = -1;
  V(0,L);
  ll res = 0;
  Rep(i,210) {
    if (i%2==0 || i%3==0 || i%5==0 || i%7==0) {
      res += v[0][L][i];
    }
  }
  printf("Case #%d: %lld\n",P+1,res);
  return true;
}

int main() {
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%i", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
