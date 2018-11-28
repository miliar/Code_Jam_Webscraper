#include <cstdio>
#include <iostream>


using namespace std;

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

int d[100000];
int l[100000];
int p[100000];

int main() {
  int T; scanf("%d\n", &T);
  for (int tt = 1; tt <= T; ++tt) {
  	int n; scanf("%d", &n);
  	for (int i = 0; i < n; ++i) {
  		scanf("%d %d", &d[i], &l[i]);
  		p[i] = 0;
  	}
  	p[0] = d[0];
  	int w; scanf("%d", &w);
  	bool result = false;
  	for (int i = 0; i < n; ++i) {
  		if (d[i] + p[i] >= w) {
  			result = true;
  			break;
		}
  		for (int j = i + 1; j < n; ++j) {
  			if (d[i] + p[i] >= d[j]) {
				int t = min(d[j] - d[i], l[j]);
				p[j] = max(p[j], t);
  			} else break;
  		}
  	}
    printf("Case #%d: ", tt);
    if (result) printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}

