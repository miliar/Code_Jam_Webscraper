#include <stdio.h>
int main () {
	int t, n, s, p, k;
	int r, count = 1;
	int temp, temp1;
	int tn[110];
	scanf("%d", &t);
	while(t--) {
		r = 0;
		scanf("%d %d %d", &n, &s, &p);
		k = 0;
		while(k < n) {
			scanf("%d", &tn[k]);
			temp = tn[k] / 3;
			temp1 = tn[k] - (temp * 3);
			if(temp1 == 1) {
				if(temp + 1 >= p)
					r++;
			} else if(temp1 == 2) {
				if(temp + 1 >= p) {
					r++;
				} else if(temp + 2 >= p && s >= 1) {
					r++;
					s--;
				} 
			} else {
				if(temp >= p) {
					r++;
				} else if(temp != 0 && temp != 10 && temp + 1 >= p && s >= 1) {
					r++;
					s--;
				}
			}
			k++;
		}
		printf("Case #%d: %d\n", count++, r);
	}
	return 0;
}