#include <iostream>
#include <cstdio>

using namespace std;

int ev[3];

int main() {
	int C, N, T, ref;
	bool p;
	
	scanf("%d", &C);
	for (int c = 0; c < C; c++) {
		scanf("%d", &N);
		
		T = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", ev + i);
			T = max(T, ev[i]);
		}
		
		for (; T > 0; T--) {
			p = 1;
			ref = ev[0] % T;
			for (int i = 1; i < N; i++)
				if (ev[i] % T != ref) {
					p = 0;
					break;
				}
			if (p) break;
		}
		
		printf("Case #%d: %d\n", c + 1, (T - ev[0] % T) % T);
	}
}

