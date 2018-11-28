#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int smartSol(int n, vector<int> c) {
  int sum = 0, m = 1000001, p = 0;
  
  for (int i=0; i<n; i++) {
    sum += c[i];
    m = min(m, c[i]);
    p ^= c[i];
  }
  
  if (p != 0) return -1;
  return sum - m;
}

int bfSol(int n, vector<int> c) {
  int bestSol = -1;
  
  for (int mask=0; mask<(1 << n)-1; mask++) {
    int p = 0, s = 0, sum = 0;
    int mask2 = mask;
    for (int i=0; i<n; i++) {
      if (mask2 & 1) {
        sum += c[i];
	s ^= c[i];
      } else {
        p ^= c[i];
      }
      mask2 >>= 1;
    }
    if (p == s && sum > bestSol) bestSol = sum; 
  }
  
  return bestSol;
}

int main() {
  int nCases;
  
  scanf("%d", &nCases);
  for (int i=1; i<=nCases; i++) {
    int n;
    vector<int> c;
    
    scanf("%d", &n);
    for (int j=1; j<=n; j++) {
      int candy;
      scanf("%d", &candy);
      c.push_back(candy);
    }
    
    int sol = smartSol(n, c);
    if (sol == -1) printf("Case #%d: NO\n", i); else printf("Case #%d: %d\n", i, sol);
  }
  return 0;
}
