#include <stdio.h>

int n, c, l;
long long t;
int a[10000];

void solve() {
	int i, j, k, tt;
	int res, max, des, min;

	scanf("%d%lld%d%d", &l, &t, &n, &c);
	for (i=0;i<c;i++) {
		scanf("%d", a+i);
	}
	
	if (l==0){
		res = 0;
		for(i=0;i<n;i++){
			res += a[i%c];
		}
		res *= 2;
	} else if (l==1) {
		res = 0;
		max = 0;
		for (i=0;i<n;i++){
			des = 0;
			if (res >= t){
				des = a[i%c];
			} else if (res + a[i%c] * 2 > t ) {
				des = (res-t)/2+a[i%c];
			}
			if (des > max){
				max=des; 
			}
			res += a[i%c] * 2;
		}
		res -= max;
	} if (l==2){
		min = 1000000000;
		for (i=0;i<n;i++) {
				res = 0;
				max = 0;
				for (k=0;k<n;k++){
					des = 0;
					if (k==i){
						if (res >= t){
							des = a[k%c];
						} else if (res + a[k%c] * 2 > t ) {
							des = (res-t)/2+a[k%c];
						}
						
					}
								
					if (k>i){
						tt = 0;
						if (res >= t){
							tt = a[k%c];
						} else if (res + a[k%c] * 2 > t ) {
							tt = (res-t)/2+a[k%c];
						}
						if (tt > max){
							max=tt; 
						}
					}
					res += a[k%c] * 2 - des;
				}
//				printf("%d\n", max);
				res -= max;
				if (res < min ){
					min = res;
				}
		}
		res = min;
	}

	printf("%d\n", res);

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
