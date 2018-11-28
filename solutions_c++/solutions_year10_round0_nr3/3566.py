#include <iostream>
#include <cstdio>

using namespace std;

typedef long long int LL;

int gr[1010][3];

int main() {
	
	int t, turn, peo, gro, inx, nad, ludz, pocz;
	LL suma, tmp;
	
	scanf("%d", &t);
	
	for (int i = 1; i <= t; i++) {
		scanf("%d %d %d", &turn, &peo, &gro);
		for (int j = 0; j < gro; j++)
			scanf("%d", &gr[j][0]);
		
		inx = 0;
		nad = 1;
		suma = 0;
		
		while (gr[inx][1] == 0) {
			gr[inx][1] = nad++;
			gr[inx][2] = suma;
			ludz = 0;
			pocz = inx;
			
			do {
				if (ludz + gr[inx][0] <= peo) {
					ludz += gr[inx][0];
					suma += gr[inx][0];
				}
				inx++;
				if (inx >= gro)
					inx = 0;
			} while (ludz + gr[inx][0] <= peo && pocz != inx);
		}
		
		if (turn - (gr[inx][1] - 1) >= 0) {
			turn -= (gr[inx][1] - 1);
			tmp = (turn / (nad - gr[inx][1])) * (suma - gr[inx][2]);
			suma = tmp + gr[inx][2];
			
			turn %= (nad - gr[inx][1]);
			
			if (turn) {
				for (int j = 0; j < gro; j++) {
					if (gr[j][1] == gr[inx][1] + turn) {
						suma += (gr[j][2] - gr[inx][2]);
						break;
					}
				}
			}
		} else {
			for (int j = 0; j < gro; j++) {
				if (gr[j][1] == turn + 1) {
					suma = gr[j][1];
					break;
				}
			}
		}
		
		
		
		printf("Case #%d: %lld\n", i, suma);
		
		for (int j = 0; j < gro; j++)
			gr[j][0] = gr[j][1] = gr[j][2] = 0;
	}
	
	return 0;
	
}