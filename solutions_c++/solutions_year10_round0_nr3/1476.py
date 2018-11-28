#include <cstdio>

typedef long long ll;
const int MAXN = 1000+5;

ll R, k, N;
ll g[MAXN];

int nexti[MAXN];
ll value[MAXN];

inline ll solve() {
	scanf("%lld %lld %lld", &R, &k, &N);
	for(int i = 0; i < N; i++) {		
		scanf("%lld", &g[i]);
		value[i] = 0;
	}

	int cycleLength = 0;
	ll cycleValue = 0;

	int i = 0;	
	ll res = 0;

	while(R > 0) {
		if(cycleLength > 0 && value[i] > 0) {		
			int j = 0;
			while(i != j) {
				cycleLength--;
				cycleValue-=value[j];
				j = nexti[j];
			} 

			res += (R/cycleLength)*cycleValue;
			R -= cycleLength*(R/cycleLength);
			cycleLength = -1;

		} else {
			if(value[i] == 0) {
				ll c = 0;
				int j = i;

				do {			
					c+=g[j];
					j = (j+1)%N;
				} while(i != j && c+g[j] <= k);

				value[i] = c;
				nexti[i] = j;

				cycleValue+=c;
				cycleLength++;
			}

			res += value[i];
			i = nexti[i];
			R--;
		}		
	}
	return res;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) printf("Case #%d: %lld\n", i, solve()); 

}