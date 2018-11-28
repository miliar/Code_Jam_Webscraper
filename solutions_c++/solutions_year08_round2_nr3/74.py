#include<iostream>
using namespace std;

int next[1000005], prev[1000005], ans[1000005];

int main() {
  int cases, q, k, left, x, y, n, i, d, j;
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    printf("Case #%d:", q);
    cin >> k;
    for (i = 0; i < k; i++) {
      next[i] = (i+1)%k;
      prev[next[i]] = i;
    }

    left = k;
    x = 0;
    for (i = 0; i < k; i++) {
      d = i%left;
      for (j = 0; j < d; j++) x = next[x];
      ans[x] = i+1;
      x = next[x];
      y = prev[prev[x]];
      next[y] = x;
      prev[x] = y;
      left--;
    }
    
    cin >> n;
    for (i = 0; i < n; i++) {
      cin >> x;
      printf(" %d", ans[x-1]);
    }
    cout << endl;
  }
  return 0;
}
