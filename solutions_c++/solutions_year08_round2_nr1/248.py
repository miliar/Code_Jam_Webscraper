#include <algorithm>
#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

typedef unsigned long long ULL;

int go() {
  int n; scanf("%d", &n);
  ULL A, B, C, D, x, y, M; scanf("%llu%llu%llu%llu%llu%llu%llu",
				 &A, &B, &C, &D, &x, &y, &M);
  vector<pair<int, int> > P;
  do {
    P.push_back(make_pair(x, y));
    x = (A*x+B)%M;
    y = (C*y+D)%M;
  } while(--n);

  sort(P.begin(), P.end());
  P.erase(unique(P.begin(), P.end()), P.end());

  n = (int)P.size();
  int cnt = 0;
  for(int i=0; i<n; ++i) {
    for(int j=i+1; j<n; ++j) {
      for(int k=j+1; k<n; ++k) {
	if ((P[i].first+P[j].first+P[k].first)%3 == 0 &&
	    (P[i].second+P[j].second+P[k].second)%3 == 0) {
	  ++cnt;
	}
      }
    }
  }

  return cnt;
}

int main() {
  int T; scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    printf("Case #%d: %d\n", i, go());
  }
}
