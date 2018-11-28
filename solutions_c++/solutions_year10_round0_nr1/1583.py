#include <stdio.h>

int twopw[31];

int main() {
	int i, t, n, k;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	twopw[0]=1;
	for(i=1;i<=30;i++) twopw[i] = twopw[i-1] << 1 ;
	
	scanf("%d", &t);
	for(i=1;i<=t;i++) {
		scanf("%d %d", &n, &k);
		n=twopw[n], k%=n;
		if(k==n-1) printf("Case #%d: ON\n", i);
		else printf("Case #%d: OFF\n", i);
	}	
	return 0;
}