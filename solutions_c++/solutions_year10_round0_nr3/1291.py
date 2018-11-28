
#include <cstdio>

int main(){
	
	long long testcase;
	long long r, k, n;
	long long s[1000];
	long long t[1000];
	long long c[1000];
	long long p[1000];
	long long e[1000];

	scanf("%lld", &testcase);

	for(long long i=1; i<=testcase; ++i){
		scanf("%lld%lld%lld", &r, &k, &n);
		long long sum = 0;
		for(long long j=0; j<n; ++j){
			scanf("%lld", &s[j]);
			sum += s[j];
		}
		if(sum <= k){
			for(long long j=0; j<n; ++j){
				t[j] = j;
				c[j] = sum;
			}
		}else{
			for(long long j=0; j<n; ++j){
				c[j] = 0;
				t[j] = j;
				for(long long u=j; u<n+j; ++u){
					if(c[j]+s[u%n] <= k){
						c[j] += s[u%n];
						t[j] = (u+1)%n;
					}else{
						break;
					}
				}
			}
		}
		for(long long j=0; j<n; ++j){
			p[j] = -1;
			e[j] = 0;
		}
		long long last = 0, crnt = 0;
		long long a, b, ea, eb, newstart;
		for(long long j=0; j<=n; ++j){
			if(p[last] == -1){
				p[last] = j;
				e[last] = crnt;
				crnt += c[last];
				last = t[last];
			}else{
				a = p[last];
				ea = e[last];
				b = j;
				eb = crnt - e[last];
				newstart = last;
				break;
			}
		}
		long long make = 0;
		
		if(r < a){
			last = 0;
			for(long long j=0; j<r; ++j){
				make += c[last];
				last = t[last];
			}
		}else{
			
			make += ea + eb*((r-a)/(b-a));
			
			//printf("%lld %lld %lld %lld\n", ea, eb, a, b);

			last = newstart;

			for(long long j=0; j<(r-a)%(b-a); ++j){
				make += c[last];
				last = t[last];
			}
		}

		printf("Case #%lld: %lld\n", i, make);
	}
	return 0;
}
