#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	int t;
	scanf("%d", &t);
	for (int ca=0; ca<t; ca++) {
		int n;
		scanf("%d", &n);
		
		char who[1000];
		int where[1000];
		for (int i=0; i<n; i++) {
			cin >> who[i] >> where[i];
//			printf("who[%d] = %c, where[%d] = %d\n", i, who[i], i, where[i]);
		}
		int op = 1, bp = 1;
		int p = 0;
		int ans = 0;
		while (p < n) {
			ans++;
			int o = p, b = p;
			while (who[o] != 'O' && o < n) o++;
			while (who[b] != 'B' && b < n) b++;
			
//			printf("p = %d\n", p);
//			printf("nextO = %d, nextB = %d\n", o, b);
			
			int nextp = p;
			
//			printf("o = %d, b = %d\n", o, b);
			if (o < n) {
				if (o == p && op == where[p] && who[p] == 'O')
					nextp++;
				else if (op < where[o]) op++;
				else if (op > where[o]) op--;
			}
			if (b < n) {
				if (b == p && bp == where[p] && who[p] == 'B')
					nextp++;
				else if (bp < where[b]) bp++;
				else if (bp > where[b]) bp--;
			}
			
			p = nextp;

//			printf("bp = %d, op = %d\n", bp, op);
			
//			if (ans > 5) break;
			
		}
		printf("Case #%d: %d\n", ca + 1, ans);
//		break;
	}
	
}
