#include<stdio.h>

int nCase;
int P[1000], np;
char isp[1024];

int main() {
	for(int i = 0; i <= 1000; ++i) isp[i] = 1;
	P[0] = 2;
	np = 1;
	for(int i = 3; i < 1000; i += 2) {
		if(isp[i] == 0) continue;
		P[np++] = i;
		for(int j = i*i; j < 1000; j += i) isp[j] = 0;
	}
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		int N, mx = 1, mn = 0;
		scanf("%d", &N);
		for(int i = 0; i < np && P[i] <= N; ++i) {
			++mn;
			for(int j = P[i]; j <= N; j *= P[i]) ++mx;
		}
		if(mn == 0) mn = 1;
		printf("Case #%d: %d\n", cs, mx-mn);
	}
}



