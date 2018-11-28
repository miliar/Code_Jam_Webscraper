#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstdio>
using namespace std;

int myabs(int x) {
  if (x > 0) return x;
  return -1 * x;
}

#define abs myabs

int main() {
  int cases;
  cin >> cases;
  int a[105];
  int b[105][256];
  
  for (int q = 1; q <= cases; q++) {
    int D, I, M, N;
    cin >> D >> I >> M >> N;
    for (int i = 0; i < N; i++) {
      cin >> a[i];
    }
    
    // base case
    for (int i = 0; i < 256; i++) {
      b[0][i] = min(D, abs(i - a[0]));
    }

    for (int i = 1; i < N; i++) {
      for (int j = 0; j < 256; j++) {
	b[i][j] = b[i-1][j] + D;
	for (int k = 0; k < 256; k++) {
	  int diff = abs(k-j);
	  int tmp;
	  if (M == 0) {
	    if (diff == 0) tmp = 0;
	    else continue;
	  }
	  else if (diff % M == 0) {
	    tmp = max(diff / M - 1, 0);
	  }
	  else {
	    tmp = diff / M;
	  }
	  b[i][j] = min(b[i][j], b[i-1][k] + abs(a[i] - j) + I * tmp);
	}
      }
    }
    int ans = b[N-1][0];
    for (int i = 1; i < 256; i++) {
      ans = min(ans, b[N-1][i]);
    }
    printf("Case #%d: %d\n", q, ans);
  }
  return 0;
}
