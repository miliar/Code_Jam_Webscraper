#include<iostream>
using namespace std;

typedef long long LL;

LL choose(LL n, LL m) {
  LL ret = 1;
  for (int i = 1; i <= m; i++) {
    ret *= (n-i+1);
    ret /= i;
  }
  return ret;
}

bool ok(int i, int j, int k) {
  int x0, y0, x1, y1, x2, y2;
  x0 = i/3;
  y0 = i%3;
  x1 = j/3;
  y1 = j % 3;
  x2 = k/3;
  y2 = k % 3;
  return ((x0+x1+x2) % 3 == 0) && ((y0+y1+y2) % 3 == 0);
}

void ins(LL a[9], LL x0, LL y0) {
  x0 %= 3;
  y0 %= 3;
  a[x0*3+y0]++;
}

int main() {
  int cases, q;
  LL x0, y0, A, B, C, D, M, n;
  int i, j, k;
  LL a[9], ans;
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    printf("Case #%d: ", q);
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    memset(a, 0, sizeof(a));
    ans = 0;
    ins(a, x0, y0);
    n--;
    for (i = 0; i < n; i++) {
      x0 = (A*x0+B) % M;
      y0 = (C*y0+D) % M;
      ins(a, x0, y0);
    }
    
    for (i = 0; i < 9; i++) {
      for (j = i+1; j < 9; j++) {
	for (k = j+1; k < 9; k++) {
	  if (ok(i, j, k)) {
	    ans += a[i] * a[j] * a[k];
	  }
	}
      }
    }

    for (i = 0; i < 9; i++) {
      ans += choose(a[i], 3);
    }

    for (i = 0; i < 9; i++) {
      for (j = 0; j < 9; j++) {
	if (j == i) continue;
	if (ok(i, i, j)) {
	  ans += (a[i]*(a[i]-1))/2 * a[j];
	}
      }
    }
    cout << ans << endl;
  }
}
