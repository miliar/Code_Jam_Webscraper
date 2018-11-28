#include <cstdio>
#include <cstring>

using namespace std;

int pi[5001];

void next(int& idx, int k) {
  for(idx=(idx+1)%k; pi[idx]; idx=(idx+1)%k);
}

void go() {
  int k, n, d[101];
  scanf("%d%d", &k, &n);
  for(int i=0; i<n; ++i) {
    scanf("%d", &d[i]);
  }
  
  memset(pi, 0, sizeof(pi));
  for(int i=1,idx=0; i<=k; ++i) {
    if (i > 1) {
      next(idx, k);
    }
    for(int j=0; j<i-1; ++j) {
      next(idx, k);
    }
    pi[idx] = i;
  }
  
  for(int i=0; i<n; ++i) {
    printf(" %d", pi[d[i]-1]);
  }
}

int main() {
  int T; scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    printf("Case #%d:", i); go();
    printf("\n");
  }
}
