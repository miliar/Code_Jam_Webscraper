#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

int P[1000];
int V[1000];
int C, D;

bool valid(long long t) {
	long long d = 4 * (P[0] - D) - t;
	int sofar = 0;
	
	for(int i = 0; i < C; i++) {
		for(int j = 0; j < V[i]; j++) {
			//printf("\t\t%d: %lld\n", sofar++, d + D*2);
			
			long long oldd = d;
			if(d + D*4 < P[i]*4) {
				d = max(d + D*4, P[i]*4 - t);
			} else {
				d = min(d + D*4, P[i]*4 + t);
			}
			
			if(llabs(oldd - d) < 4*D) return false;
		}
	}
	
	return true;
}

int main() {
	int T;
	
	scanf("%d\n", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d %d\n", &C, &D);
		
		for(int i = 0; i < C; i++) {
			scanf("%d %d\n", &P[i], &V[i]);
		}
		
		long long a = 0, b = 2000000000000LL, c;
		
		while(a < b) {
			c = (a + b) / 2;
			
			if(valid(c)) {
				//printf("\t%lld high\n", c);
				b = c;
			} else {
				//printf("\t%lld low\n", c);
				a = c + 1;
			}
		}
		
		printf("Case #%d: %f\n", nCase, b/4.0);
	}
}
