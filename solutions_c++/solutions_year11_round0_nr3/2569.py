#include <algorithm>
#include <cstdio>
#include <cstring>
#include <numeric>

using namespace std;

const int N = 1048576;

int a[N];

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int sum = 0, parity = 0, n; scanf("%d", &n);
    memset(a, -1, sizeof(a));
    for(int i=0; i<n; ++i) {
      int x; scanf("%d", &x);
      for(int j=0; j<N; ++j) {
	if ((j^x) < j) {
	  int u, v;
	  if (a[j^x] != -1 && a[j] < a[j^x]+x) {
	    u = a[j^x] + x;
	  } else {
	    u = a[j];
	  }
	  if (a[j] != -1 && a[j^x] < a[j]+x) {
	    v = a[j] + x;
	  } else {
	    v = a[j^x];
	  }
	  a[j]   = u;
	  a[j^x] = v;
	}
      }
      if (i) {
	if (a[parity] < sum) {
	  a[parity] = sum;
	}
	if (a[x] < x) {
	  a[x] = x;
	}
      }
      sum += x; parity ^= x;
    }
    printf("Case #%d: ", t);
    if (parity) {
      printf("NO\n");
    } else {
      printf("%d\n", *max_element(a+0, a+N));
    }
  }
}
