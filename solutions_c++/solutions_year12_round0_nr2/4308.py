#include <cstdio>
#include <iostream>

using namespace std;

int a[100];
int b[100];
int c[100];

int main() {
  int T; scanf("%d\n", &T);
  for (int tt = 1; tt <= T; ++tt) {
  	int n, s, p;
  	scanf("%d %d %d", &n, &s, &p);
  	int k = 0;
  	for (int i = 0; i < n; ++i) {
  		scanf("%d", &a[i]);
  		bool f1 = false, f2 = false;
  		for (int x = 0; x <= 2; ++x) {
  			for (int y = 0; y + x <= 2; ++y) {
  				if (a[i] - (2 * x + y) >= 0 && (a[i] - (2 * x + y)) % 3 == 0) {
  					int z = (a[i] - (2 * x + y)) / 3 + x + y;
  					if (z >= p) {
//  						cout << a[i] << " " << x << " " << y << " " << z << endl;
  						if (x + y < 2) f1 = true;
  						else f2 = true;
  					}
  				}
  			}
  		}
  		if (f1) ++k;
  		else
  		if (f2 && s) {
  			++k;
  			--s;
  		}
  	}
    printf("Case #%d: %d\n", tt, k);
  }
  return 0;
}

