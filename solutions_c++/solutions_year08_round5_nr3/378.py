#include <cstdio>
#include <cstring>

using namespace std;

const int N = 128;

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int m, n; scanf("%d%d", &m, &n);
    int A[N] = {0};
    for(int i=0; i<m; ++i) {
      char line[N];
      scanf(" %[^\n]", line);
      for(int j=0; j<n; ++j) {
	if (line[j] == 'x') {
	  A[i] |= 1<<j;
	}
      }
    }
    int B[1<<10][2];
    memset(B, -1, sizeof(B));
    B[0][0] = 0;
    int p = 1;
    for(int i=0; i<m; ++i,p^=1) {
      for(int j=0; j<(1<<n); ++j) {
	bool ok = (A[i]&j) == 0;
	for(int k=0; ok && k<n-1; ++k) {
	  if ((j&(1<<k)) && (j&(1<<(k+1)))) {
	    ok = false;
	  }
	}
	if (ok) {
	  int m = ((j<<1) | (j>>1)) & ((1<<n)-1);
	  int cnt = 0;
	  for(int k=j; k; ++cnt, k&=(k-1));
	  for(int k=0; k<(1<<n); ++k) {
	    if ((k&m) == 0 && B[k][p^1] >= 0) {
	      B[j][p] >?= cnt+B[k][p^1];
	    }
	  }
	}
      }
    }
    int ans = 0;
    for(int i=0; i<(1<<n); ++i) {
      if ((A[m-1]&i) == 0) {
	ans >?= B[i][p^1];
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
