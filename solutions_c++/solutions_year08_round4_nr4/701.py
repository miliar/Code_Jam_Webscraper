#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;

int main() {
  int q, cases, i, j, p[20], ans, ans2, le, k;
  char last, a[50005];
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    printf("Case #%d: ", q);
    cin >> k;
    cin >> a;
    le = strlen(a);
    for (i = 0; i < k; i++) p[i] = i;
    ans = le;
    do {
      ans2 = 0;
      last = '1';
      for (i = 0; i < le; i+=k) {
	for (j = 0; j < k; j++) {
	  if (last != a[i+p[j]]) ans2++;
	  last = a[i+p[j]];
	}
      }
      ans <?= ans2;
    } while (next_permutation(p, p+k));
    cout << ans << endl;
  }
  return 0;
}
