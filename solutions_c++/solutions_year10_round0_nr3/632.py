#include <cstdio>
#include <vector>

using namespace std;

int T;

int main() {
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		int R, k, N;
		scanf("%d%d%d", &R, &k, &N);
		vector<int> g(N);
		long long int tg = 0;
		
		for(int j=0; j<N; j++) {
			scanf("%d", &g[j]);
			tg += g[j];
		}
		
		vector<int> gp(N, -1);
		vector<long long int> gm(N, 0);

		
		long long int m = 0;
		int p = 0;
		int c = 0;
		
		while(p < R) {		
			if (gp[c] >= 0) {	
				int z = R - p;			
				int dp = p - gp[c];				
				if (dp <= z) {
					long long int v = m - gm[c];				
					gp[c] = p;
					gm[c] = m;
					int e = z / dp;
					
					m += e * v;
					p += e * dp;					
				}
			}
			
			if (p >= R)
				break;
			
			
			gp[c] = p;
			gm[c] = m;
			long long int v = 0;
			while(1) {
				long long int nv = v + g[c];
				if ((nv > tg) || (nv > k))
					break;
				v = nv;
				c = (c+1) % N;
			}
			m += v;	
			p++;					
		}
		
			
		printf("Case #%d: %lld\n", (i+1), m);
	}
	return 0;
}
