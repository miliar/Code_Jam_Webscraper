#include <stdio.h>

int min(int a, int b) {
	if (a<b) return a;
	return b;
}

int main() {
	int t;
	scanf("%d\n", &t);
	for(int it=1; it<=t; it++) {
		
		int n;
		scanf("%d", &n);
		int d[n];
		int l[n];
		int prev[n];
		
		for(int i=0; i<n; i++) {
			scanf("%d %d", &d[i], &l[i]);
			prev[i] = d[i];
		}
		
		prev[0] = 0;
		
		int fin;
		scanf("%d", &fin);
		bool succ = false;
	
		for(int i=0; i<n; i++) {
			
			//for(int j=0; j<n; j++)
			//	printf("%d ", prev[j]);
			//printf("\n");
			
			int skok = l[i];
			if(d[i] - prev[i] < skok)
				skok = d[i] - prev[i];
			
			if(d[i] + skok >= fin) {
				succ = true;
				break;
			}
			
			//printf("zas: %d\n", d[i]+skok);
			
			for(int j=i+1; j<n; j++) {
				if(d[i]+skok >= d[j]) {
					//printf("jestem\n");
					prev[j] = min(prev[j], d[i]);
					// printf("%d = %d\n", j
				}
				else
					break;
			}
		}
		
		if(succ)
			printf("Case #%d: YES\n", it);
		else
			printf("Case #%d: NO\n", it);
	}
	return 0;
}

