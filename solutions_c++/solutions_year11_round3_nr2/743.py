#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int a[1009];
int star[1000009];
int dosort[1000009];

bool cmp(int a, int b) {
	
	return b < a;
}

int main() {
	
	int T, t, n, C, L;
	
	scanf("%d", &T);
	
	for (int k = 1; k <= T; k++) {
		
		scanf("%d %d %d %d", &L, &t, &n, &C);
		
		for (int i = 0; i < C; i++)
			scanf("%d", &a[i]);
		
		for (int i = 0, j = 0; i < n; i++, j++) {
			
			if (j == C)
				j = 0;
			
			star[i] = a[j];
		}
		
		int inx = 0;
		
		long long int wyn = t;
		t /= 2;
		
		for (int i = 0; i < n; i++) {
			
			if (t && t < star[i]) {
				dosort[inx++] = star[i] - t;
				t = 0;
			} else if (t && t > star[i]) {
				t -= star[i];
			} else {
				dosort[inx++] = star[i];
			}
		}
		
		sort(dosort, dosort + inx, cmp);
		
		for (int i = 0; i < inx; i++) {
			
			if (i < L)
				wyn += dosort[i];
			else
				wyn += dosort[i] * 2;
		}
		
		printf("Case #%d: %lld\n", k, wyn);
	}
	
	return 0;
	
}
