
#include <cstdio>
#include <cstdlib>
#include <ctime>

typedef long long ull;

ull Q(ull a){ return a*a; }

int main(){
	
	int testcase; scanf("%d", &testcase);
	ull r[1000];
	ull x[1000];
	ull y[1000];

	srand(time(NULL));

	for(int t=1; t<=testcase; ++t){
		ull n, a, b;
		scanf("%lld %lld %lld", &n, &a, &b);
		for(int i=0; i<n; ++i){
			scanf("%lld", &r[i]);
		}
		for(int i=0; i<n; ++i){
			x[i] = rand()%(a+1);
			y[i] = rand()%(b+1);
			bool flag = true;
			for(int j=0; j<i; ++j){
				if(Q(x[j]-x[i])+Q(y[j]-y[i]) < Q(r[i]+r[j])){
					flag = false; break;
				}
			}
			if(!flag){
				--i;
			}
		}

		printf("Case #%d:", t);

		for(int i=0; i<n; ++i){
			printf(" %lld %lld", x[i], y[i]);
		}
		printf("\n");
	}
	return 0;
}
