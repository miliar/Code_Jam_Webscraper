#include <cstdio>
#include <cstring>

long long R, k, N;
long long x;
long long sum[2100];
long long pd[2100];
long long val[2100];
long long next[2100];
long long mark[2100];

void read() {
	
	scanf("%lld%lld%lld", &R, &k, &N);
	for (int i = 0; i < N; i++) {
		scanf("%lld", &val[i]);
		val[i+N] = val[i];
	}
	
	
}

void process() {
	
	long long temp;
	for (int i = 0; i < N; i++) {
		
		temp = 0;
		next[i] = -1;
		for (int j = 0; j < N; j++) {
			if (temp + val[i+j] > k) {
				next[i] = (i+j)%N;
				sum[i] = temp;
				break;
			} else {
				temp += val[i+j];
			}
		}
		
		if (next[i] == -1) {
			next[i] = i;
			sum[i] = temp;
		}
	}
	/*
	printf("next: ");
	for (int i = 0; i < N; i++) {
		printf("%lld ", next[i]);
	}
	printf("\nsum: ");
	for (int i = 0; i < N; i++) {
		printf("%lld ", sum[i]);
	}
	printf("\n");
	*/
	pd[0] = 0;
	memset(mark, -1, sizeof(mark));
	long long at = 0;
	mark[at] = 1;
	pd[1] = sum[at];
	long long posMax = 1;
	long long tam = 1;
	for (int i = 1; i < R; i++) { //parar antes!	
		
		if (mark[next[at]] != -1) {
			temp = pd[mark[at]]-pd[mark[next[at]]-1];
			tam = mark[at] - mark[next[at]] + 1;
		} else {
			at = next[at];
			mark[at] = i+1;
			pd[i+1] = pd[i] + sum[at]; 
			//printf("pd[%d] = %lld\n", i+1, pd[i+1]);
			posMax++;
		}
		
	}
	
	
	
	long long r = ((R-posMax)%tam);
	long long tot = pd[posMax] + temp*((R-posMax)/tam) + (pd[mark[next[at]]-1+r]-pd[mark[next[at]]-1]);
	
	printf("%lld\n", tot);
}

int main() {

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int casos;
	scanf("%d", &casos);
	for (int i = 1; i <= casos; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}