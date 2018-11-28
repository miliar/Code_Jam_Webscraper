#include <iostream>
using namespace std;

int table[31][2];

void process() {
	for (int i = 0; i <= 30; i++) {
		int t = i / 3;
				
		if (i % 3 == 0) {
			table[i][0] = t;
			if (t > 0)
				table[i][1] = t + 1;
			else 
				table[i][1] = t;
		} else if (i % 3 == 1) {
			table[i][0] = t + 1;
			table[i][1] = t + 1;
		} else {
			table[i][0] = t + 1;
			table[i][1] = t + 2;
		}
	}
}

int main() {
	int t;
	process();
	
	scanf("%d\n", &t);
	
	for (int k = 0; k < t; k++) {
	
		int n, s, limit;
		int score;
		scanf("%d%d%d", &n, &s, &limit);
		
		int a[100];
		int res = 0;
		int x, y;
		
		for (int i = 0; i < n; i++) {
			scanf("%d", a + i);
			x = table[a[i]][0];
			y = table[a[i]][1];
		
			if (x >= limit) res++;
			else {
				if (y >= limit && s > 0) {
					s--;
					res++;
				} 
			}
		}
		
		printf("Case #%d: %d", k+1, res);
		if (k < t - 1) printf("\n");
	}
	
	return 0;
}