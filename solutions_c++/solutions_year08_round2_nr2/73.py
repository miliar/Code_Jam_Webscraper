#include<iostream>
using namespace std;

typedef long long LL;
int a[1000005];

void stdize(int x) {
  if (a[x] != a[a[x]]) {
    stdize(a[x]);
    a[x] = a[a[x]];
  }
}
void join(int x, int y) {
  stdize(x); stdize(y);
  a[a[x]] = a[y];
}

int main() {
  bool np[1000005];
  int i, j, nlp = 0, lp[80000];
  
  memset(np, 0, sizeof(np));
  for (i = 2; i <= 1000; i++) {
    if (! np[i]) {
      lp[nlp++] = i;
      for (j = i*i; j <= 1000000; j+=i) np[j] = true;
    }
  }
  for (i = 1001; i <= 1000000; i++) {
    if (! np[i]) {
      lp[nlp++] = i;
    }
  }
  //--------------
  int cases, q, n, ans;
  LL A, B, P, x, y;
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    printf("Case #%d: ", q);
    cin >> A >> B >> P;
    n = B-A+1;
    for (i = 0; i < n; i++) a[i] = i;
    
    for (i = 0; i < nlp; i++) {
      if (lp[i] < P) continue;
      if (lp[i] > n) break;
      x = A;
      if (x % lp[i] != 0) {
	x = x - (x%lp[i]) + lp[i];
      }
      y = x+lp[i];
      while (y <= B) {
	join(x-A, y-A);
	x = y;
	y += lp[i];
      }
    }
    for (i = 0; i < n; i++) stdize(i);
    ans = 0;
    for (i = 0; i < n; i++) {
      if (a[i] == i) {
	ans++;
      }
    }
    cout << ans << endl;
  }
  return 0;
}
