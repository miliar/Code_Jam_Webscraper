#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int a[100];
int b[100];

int main() {
  int T; scanf("%d\n", &T);
  for (int tt = 1; tt <= T; ++tt) {
  	int n; scanf("%d", &n);
  	for (int i = 0; i < n - 1; ++i) {
  		scanf("%d", &a[i]);
  		--a[i];
  	}
  	for (int i = 0; i < n; ++i) {
  		b[i] = 1;
  	}
	int f = 0;
	int p = 0;
  	while (!f && p < 1000000) {
  		++p;
  		f = 1;
  		for (int i = 0; i < n - 1; ++i) {
  			int dy = b[a[i]] - b[i];
  			int dx = a[i] - i;
  			double y1 = dy;
  			double y2 = dy;
  			for (int j = i + 1; j < a[i]; ++j) {
  				if (dy * (j - i) <= (b[j] - b[i]) * dx) {
  					y1 = max(y1, (b[j] - b[i]) * dx / (double) (j - i));
  					f = 0;
  				}
  			}
			for (int j = a[i] + 1; j < n; ++j) {
				if (dy * (j - i) < (b[j] - b[i]) * dx) {
  					y2 = max(y2, (b[j] - b[i]) * dx / (double) (j - i));
  					f = 0;
				}
			}
			if (!f) {
				dy = (int)max(y1, y2);
				while ((dy <= y1) || (dy < y2)) ++dy;
				b[a[i]] = b[i] + dy;
				if (b[a[i]] > 1000000000) {
					f = -1;
					break;
				}
				break;
			}
  		}
  	}
  	/*
  	bool f = false;
  	do {
		f = true;
  		for (int i = 0; i < n - 1; ++i) {
  			int dy = b[a[i]] - b[i];
  			int dx = a[i] - i;
  			for (int j = i + 1; j < a[i]; ++j) {
  				if (dy * (j - i) <= (b[j] - b[i]) * dx) {
  					f = false;
  					break;
  				}
  			}
  			if (f) {
				for (int j = a[i] + 1; j < n; ++j) {
					if (dy * (j - i) < (b[j] - b[i]) * dx) {
						f = false;
						break;
					}
				}
  			}
  			if (!f) break;
  		}
  		if (f) {
  			break;
  		}
  	} while (next_permutation(b, b + n));*/
    printf("Case #%d:", tt);
    if (f == 1) {
    	for (int i = 0; i < n; ++i) {
    		printf(" %d", b[i]);
    	}
    } else {
    	printf(" Impossible");
    }
    putchar('\n');
  }
  return 0;
}

