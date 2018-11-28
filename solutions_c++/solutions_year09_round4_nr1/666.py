#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  int q, cases, x, y, a[50], n, y2;
  char c[100];
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    cin >> n;
    for (y = 0; y < n; y++) {
      for (x = 0; x < n; x++) {
	cin >> c[x];
      }
      for (x = n-1; x >= 0; x--) {
	if (c[x] == '1') break;
      }
      a[y] = x;
    }
    int ans = 0;
    for (y = 0; y < n; y++) {
      for (y2 = y; y2 < n; y2++) {
	if (a[y2] <= y) break;
      }
      while (y2 > y) {
	swap(a[y2], a[y2-1]);
	ans++;
	y2--;
      }
    }
    printf("Case #%d: %d\n", q, ans);
  }
  return 0;
}
