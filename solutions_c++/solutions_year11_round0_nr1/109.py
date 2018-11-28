#include <cstdio>

inline int abs2(int x) {
	if (x < 0) {
		return -x;
	}
	return x;
}

inline int min2(int a, int b) {
	if (a < b) {
		return a;
	}
	return b;
}

int main() {
	int O[100], B[100], turn[100];
	int t, n;
	
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		scanf("%d", &n);
		
		int o = 0, b = 0;
		char robot;
		int pos;
		
		for (int i = 0; i < n; i++) {
			scanf(" %c %d", &robot, &pos);
			
			if (robot == 'O') {
				turn[i] = 0;
				O[o++] = pos;
			} else {
				turn[i] = 1;
				B[b++] = pos;
			}
		}
		
		int opos = 1, bpos = 1;
		int oi = 0, bi = 0;

		int acc = 0;

		for (int i = 0; i < n; i++) {
			if (turn[i] == 0) {
				acc += abs2(O[oi] - opos) + 1;
				
				if (bi < b) {				
					int db = min2(abs2(O[oi] - opos) + 1, abs2(B[bi] - bpos));
					
					if (db > 0) {
						bpos += ( (B[bi] - bpos) / abs2(B[bi] - bpos) ) * db;
					}
				}
				
				opos = O[oi++];
			} else {
				acc += abs2(B[bi] - bpos) + 1;
				
				if (oi < o) {				
					int db = min2(abs2(O[oi] - opos), abs2(B[bi] - bpos) + 1);
					
					if (db > 0) {
						opos += ( (O[oi] - opos) / abs2(O[oi] - opos) ) * db;
					}
				}
				
				bpos = B[bi++];			
			}
		}		
		
		printf("Case #%d: %d\n", test, acc);
	}
	
	return 0;
}

