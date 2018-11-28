#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

int main(void) {
	int T;
	int V;
	int tab[10010][2];
	int N[10010][2];
	int M;
	int Cases = 1;
	int tmp;
	int c1, c2;
	int min0;
	int min1;
	int min0tmp;
	int min1tmp;
	int sw;
	scanf("%d", &T);
	while(T--) {		
		for(int i = 0; i < 10010; ++i) {
			tab[i][0] = INT_MAX;
			tab[i][1] = INT_MAX;
		}
		scanf("%d%d", &M, &V);
		for(int i = 1; i <= (M-1)/2; ++i) {
			scanf("%d%d", &N[i][0], &N[i][1]);
		}
		for(int i = (M-1)/2 + 1; i <= M; ++i) {
			scanf("%d", &tmp);
			tab[i][tmp] = 0;
		}
		for(int j = (M-1)/2; j > 0 ; --j) {
			c1 = j * 2;
			c2 = j * 2 + 1;
			if(c1 > M || c2 > M) break;
			min0 = INT_MAX;
			min1 = INT_MAX;
			//printf("N[%d][0] = %d   N[%d][1] = %d\n", j, N[j][0], j, N[j][1]);
			if(N[j][0] == 0 || N[j][1] == 1) {
				if(tab[c1][0] < INT_MAX && tab[c2][0] < INT_MAX) {
					min0 = tab[c1][0] + tab[c2][0];
				}
				else {
					min0 = max(tab[c1][0], tab[c2][0]);
				}
				min1 = min(tab[c1][1], tab[c2][1]);
				if(N[j][0] == 1) {
					if(min0 < INT_MAX) min0++;
					if(min1 < INT_MAX) min1++;
				}				
			}
			if(N[j][0] == 1 || N[j][1] == 1) {	
				min0tmp = min(tab[c1][0], tab[c2][0]);
				if(tab[c1][1] < INT_MAX && tab[c2][1] < INT_MAX) {
					min1tmp = tab[c1][1] + tab[c2][1];
				}
				else {
					min1tmp = max(tab[c1][1], tab[c2][1]);
				}
				if(N[j][0] == 0) {
					if(min0tmp < INT_MAX) min0tmp++;
					if(min1tmp < INT_MAX) min1tmp++;
				}				
				min0 = min(min0, min0tmp);
				min1 = min(min1, min1tmp);
			}				
			tab[j][0] = min(tab[j][0], min0);
			tab[j][1] = min(tab[j][1], min1);
			//printf("children were %d and %d\n", c1, c2);
			//printf("setting j = %d to 0 = %d  1 = %d\n", j, tab[j][0], tab[j][1]);				
		}
		
		if(tab[1][V] == INT_MAX) {
			printf("Case #%d: IMPOSSIBLE\n", Cases++);			
		}
		else {
			printf("Case #%d: %d\n", Cases++, tab[1][V]);	
		}
	}	
	return 0;
}
