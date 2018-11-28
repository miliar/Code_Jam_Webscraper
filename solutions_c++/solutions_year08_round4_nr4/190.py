#include <algorithm>
#include <cstdio>

using namespace std;

char str[1001], a[1001];

int go() {
  int k; scanf("%d%s", &k, str);
  int pi[5] = {0, 1, 2, 3, 4};
  int m = 0x3fffffff, n = strlen(str);
  do {
    for(int i=0; i<n; i+=k) {
      for(int j=0; j<k; ++j) {
	a[i+j] = str[i+pi[j]];
      }
    }
    int score = 0;
    for(int i=0; i<n; ++score) {
      int j = i+1;
      for(; j<n && a[j] == a[i]; ++j);
      i = j;
    }
    m <?= score;
  } while(next_permutation(pi,pi+k));
  return m;
}

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    printf("Case #%d: %d\n", t, go());
  }
}
