#include <stdio.h>
#include <stdlib.h>
long long fre[100000];
int n;

int func(long long f){
	int i;

	for (i=0;i<n;i++) {
		if (f%fre[i] != 0 && fre[i]%f != 0 ){
			return 0;
		}	
	}
	return 1;
}

long long gcd(long long a, long long b) {
	long long m;
	while ( a % b ) {
		m = a % b;
		b=a;
		a=m;
	}
	return b;
}

int cmp(const void *a, const void *b) {
	return *(long long*)a - *(long long*)b;
}

void solve() {
	int i, j;
	long long min, mid, max, res, m, ans;

	scanf("%d%lld%lld", &n, &min, &max);
	for (i=0;i<n;i++) {
		scanf("%lld", fre+i);
	}
	
	for (i=min; i<=max;i++){
		if (func(i)) {
			break;
		}
	}
	if (i>max){
		printf("NO\n");
	} else {
		printf("%d\n", i);
	}

}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i=1;i<=t;i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
