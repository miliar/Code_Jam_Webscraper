#include <cstdio>
#include <cmath>

using namespace std;

long long iabs(long long a) {
  return a<0?-a:a;
}

void go() {
  long long a, n, m; scanf("%lld%lld%lld", &n, &m, &a);
  for(long long i=0; i<=n; ++i) {
    for(long long j=i; j<=n; ++j) {
      for(long long ii=0; ii<=m; ++ii) {
	for(long long jj=0; jj<=m; ++jj) {
	  if (iabs(j*ii - i*jj) == a) {
	    printf("0 0 %lld %lld %lld %lld", i, ii, j, jj);
	    goto out;
	  }
	}
      }
    }
  }
  printf("IMPOSSIBLE");
 out:;
}

int main() {
  int T; scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    printf("Case #%d: ", i);
    go();
    printf("\n");
  }
}
