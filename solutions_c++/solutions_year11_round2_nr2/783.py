#include <stdio.h>

int d, c, n;
int p[1000000];
double pos[1000000];

int can(double t){
	int i, j;
	
	pos[0] = p[0] - t;
	for (i=1;i<n;i++) {
		pos[i] = pos[i-1] + d;
		if (p[i] - pos[i] > t){
			pos[i] = p[i] - t;
		} else if (pos[i] - p[i] > t) {
			break;
		}
	}
	if (i==n){
		return 1;
	}
	pos[n-1] = p[n-1]+t;
	for (i=n-2;i>=0;i--){
		pos[i] = pos[i+1] - d;
		if (pos[i] - p[i] > t){
			pos[i] = p[i] + t;
		} else if (p[i] - pos[i] > t ) {
			break;
		}
	}
	if (i==n){
		return 1;
	}
	return 0;
}

void solve() {
	int i, j, k, pos, v;
	double min, mid, max;
	scanf("%d%d", &c, &d);
	n=0;
	for (i=0;i<c;i++) {
		scanf("%d%d", &pos, &v);
		while(v--){
			p[n++]=pos;
		}
	}

	min = 0;
	max = 1000000000;
	while (min < max - 1e-9) {
		mid = (min + max) / 2;
		if (can(mid)) {
			max = mid;
		} else {
			min = mid;
		}
	}

	printf("%g\n", min);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i=1;i<=t;i++){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
