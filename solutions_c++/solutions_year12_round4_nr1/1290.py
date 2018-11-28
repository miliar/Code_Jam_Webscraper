#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
using namespace std;
typedef long long lli;

const int MAX_N = 10001;
int N;
int D[MAX_N];
int L[MAX_N];
int W;

int lim[MAX_N];

bool solve() {
  fill(lim,lim+N,-1);
  lim[0] = D[0]*2;
  if(lim[0] >= W) return true;
  for(int i = 0; i < N; ++i) {
    for(int j = i+1; j < N && D[j] <= lim[i]; ++j) {
      int l = min(D[j]-D[i], L[j]);
      lim[j] = max(lim[j], D[j] + l);
      if(lim[j] >= W) return true;
    }
  }
  return false;
}

int main() {
  int Tc;
  cin >> Tc;
  for(int tc = 1; tc <= Tc; ++tc) {
    cin >> N;
    for(int i = 0; i < N; ++i) {
      cin >> D[i] >> L[i];
    }
    cin >> W;
    cout << "Case #" << tc << ": ";
    if(solve()) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
