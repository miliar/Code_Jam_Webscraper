#include <iostream>

using namespace std;

int main()
{
	int T;
	freopen("c.txt", "w", stdout);
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		//get the input
		int r, n;
		long long k;
		scanf("%d %lld %d", &r, &k, &n);
		long long g[n*2];
		long long sum, y;
		
		sum = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%lld\n", &g[i]);
			if (g[i] > k) while (1); //???
			sum += g[i];
		}
		
		//caculate the result
		y = 0;
		if (sum <= k) {
			y = sum * ((long long)r);
		} else {
			// initialize
			for (int i = 0; i < n; ++i) {
				g[i+n] = g[i];
			}
			
			int next[n+1], cur; 
			long long hold[n+1], tot = 0;
			for (int i = 0; i < n; ++i) {
				tot += g[i];
				if (tot > k) {
					cur = i;
					break;
				}
			}
			
			for (int i = 0; i < n; ++i) {
				hold[i] = tot - g[cur];
				next[i] = cur % n;
				
				tot -= g[i];
				while (tot <= k) {
					++cur;
					tot += g[cur];
				}
			}
			
			//round up
		
			int dot[n], cycle;
			long long add_up[n], cycle_up = 0, result = 0;
			memset(dot, 0, sizeof(dot));
			int round = 1, pos = 0;
			
			while (true) {
				dot[pos] = round;
				result += hold[pos];
				add_up[pos] = result;
				if (round == r) {
					y = result;
					cycle = 0;
					break;
				}
				pos = next[pos];
				round++;
				
				if (dot[pos] != 0) {
					cycle = round - dot[pos];
					cycle_up = result + hold[pos] - add_up[pos];
					break;
				}
			}
			
		//	printf("round=%d, cycle=%d, result=%lld, pos=%d, cycle_up=%lld\n", round, cycle, result, pos, cycle_up);
			
			if (cycle != 0) {
				y = result;
				r -= round - 1; //
				y += cycle_up * (r / cycle );
				r %= cycle;
				for (int i = 0; i < r; i++) {
					y += hold[pos];
					pos = next[pos];
				}
			}
		}
		
		printf("Case #%d: %lld\n", ca, y);
	}
	return 0;
}

