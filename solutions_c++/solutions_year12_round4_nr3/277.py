#include <cstdio>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cstdlib>

using namespace std;

int r(int n) {
  return (rand()) % n;
}

const int INF = 1000000001;
const int MAXC = 100000;

int n;
int x[20], h[20];

char s[10];

int check(int i, int j, int k) {
  long long left = (long long)(k - j) * h[i] + (j - i) * h[k];
  long long right = (long long)(k - i) * h[j];
  return (j < k && left > right || j > k && left >= right);
}

int adjust() {
  long long left, right;
  int count = 0;
  while (++count < MAXC) {
    int more = 0;
    for (int i = 0; i+1 < n; ++i) {
      int k = x[i];
      for (int j = i+1; j < n; ++j) if (j != k) {
	left = (long long)(k - j) * h[i] + (j - i) * h[k];
	right = (long long)(k - i) * h[j];
	if (j < k && left <= right) {
	  /*	  printf("i=%d j=%d k=%d\n",i,j,k);
	  for (int q=0;q<n;++q) printf("%d ", h[q]);
	  printf("\n");*/

	  // increase i
	  right -= (j - i) * h[k];
	  h[i] = (right + (k-j-1)) / (k-j);
	  //	  printf("adjust h[%d] to %d\n", i, h[i]);
	  if (h[i] >= INF) return 0;
	  more = 1;
	  break;
	}
	else if (j > k && left < right) {
	  // increase k
	  /*	  printf("%d %d %d\n",i,j,k);
	  for (int q=0;q<n;++q) printf("%d ", h[q]);
	  printf("\n");*/

	  right -= (k - j) * h[i];
	  h[k] = (right + (j-i-1)) / (j-i);
	  //	  printf("adjust h[%d] to %d\n", k, h[k]);
	  if (h[k] >= INF) return 0;
	  more = 1;
	  break;
	}
      }
    }
    if (!more) return 1;
  }
  return 0;
}

int ok() {
  if (adjust()) {
    for (int j = 0; j < n; ++j) printf(" %d", h[j]);
    printf("\n");
    return 1;
  }
  return 0;
}

void solve() {
  for (int j = 0; j < n; ++j) h[j] = 0;
  if (ok()) return;

  for (int i = 1; i <= 100; ++i) {
    for (int j = 0; j < n; ++j) h[j] = r(10000);
    if (ok()) return;
  }
  printf(" Impossible\n");
}

int main() {
  int t;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    printf("Case #%d:", c);
    scanf("%d", &n);
    for (int i = 0; i+1 < n; ++i) { scanf("%d", x + i); x[i]--; }
    solve();
  }
}
