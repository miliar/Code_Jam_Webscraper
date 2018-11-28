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

bool isPrime[2000];

void calcPrime() {
  for (int i = 0; i < 1001; i+=1) 
    isPrime[i] = true;
  for (int i = 2; i < 1001; i+=1) {
    for (int j = 2; j*i < 1001; ++j) {
      isPrime[i*j] = false;
    }
  }
  //Rep(i,20) if (isPrime[i]) cout << i << " ";
}

int A,B,P;
vi factors[1001];

bool con[1001][1001];

bool found[1001];

void search(int n) {
  if (found[n])
    return;
  found[n] = true;
  for (int i = A; i <=B; ++i) {
    if (con[n][i])
      search(i);
  }
}

bool solve(int P0) {
  scanf("%d%d%d",&A,&B,&P);
  for (int i = A; i <= B; ++i) {
    for (int j =P; j <= i; ++j)
      if (isPrime[j] && i%j == 0)
	factors[j].push_back(i);
  }
  for (int i = A; i <= B; ++i) {
    for (int j = A; j <= B; ++j) {
      con[i][j] = false;
    }
  }
  for (int i = P; i <= B; ++i) {
    Rep(j,factors[i].size()) Rep(k,factors[i].size()) {
      con[factors[i][j]][factors[i][k]] = true;
      //cout << j << "," << k << endl;
    }
  }
  /*for (int i = A; i <= B; ++i) {
    for (int j = A; j <= B; ++j) {
      cout << con[i][j];
    }
    cout << endl;
  }*/
  Rep(i,1001) found[i] = false;
  int res = 0;
  for (int i = A; i <= B; ++i) {
    if (!found[i])
      ++res;
    search(i);
  }
  printf("Case #%d: %d\n",P0+1,res);
  return true;
}

int main() {
  calcPrime();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%i", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
