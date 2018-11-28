#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int skupine[1000];

int part_r[1000];
long long rezultat[1000];

int main() {
	int T, r, k, N;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d %d", &r, &k, &N);
		for (int i = 0; i < N; i++)
			scanf("%d", skupine + i);
		
		memset(rezultat, 0, sizeof rezultat);
		
		int kapaciteta = k, pos = 0, start = -1;
		long long res = 0;
		bool check = true;
		
		while (1) {
			if (start != pos && kapaciteta - skupine[pos] >= 0) {
				if (start == -1) start = pos;
			
				kapaciteta -= skupine[pos];
				res += skupine[pos];
				pos = (pos + 1) % N;
			} else {
				if (!(--r)) break;
				
				kapaciteta = k;
				start = -1;
				
				if (check) {
					if (rezultat[pos]) {
					
						int cas = part_r[pos] - r;
						long long times = r / cas;
						
						fprintf(stderr, "%d %lld %lld\n", cas, times, times * (res - rezultat[pos]));
						
						res += times * (res - rezultat[pos]);
						
						r %= cas;
						
						check = false;
						
						if (!r) break;
						
					} else {
						rezultat[pos] = res;
						part_r[pos] = r;
					}
				}
			}
		}
		
		printf("Case #%d: %lld\n", t + 1, res);
	}
}

