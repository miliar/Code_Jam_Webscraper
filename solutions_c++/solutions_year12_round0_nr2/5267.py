#include <cstdio>

#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

int T;

int main(void) {
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		int N, S, p;
		int surprising = 0, nonsurprising = 0;

		scanf("%d%d%d", &N, &S, &p);
		for(int i = 0; i < N; i++) {
			int ti;
			scanf("%d", &ti);
			if(ti >= p + 2 * max(p - 2, 0)) surprising++;
			if(ti >= p + 2 * max(p - 1, 0)) nonsurprising++;
		}

		printf("Case #%d: %d\n", t, min(nonsurprising + min(surprising - nonsurprising, S), N));
	}
	return 0;
}
