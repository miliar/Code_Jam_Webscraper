#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

int main(void) {
	int T;
	int Cases = 1;
	int N, M, A;
	bool found;
	scanf("%d", &T);
	while(T--) {	
		//printf("T %d", T);
		scanf("%d%d%d", &N,&M,&A);
		found = false;
		for(int i = 0; i <= N && !found; ++i) {
			for(int j = 0; j <= M && !found; ++j) {
				if(i == 0 && j == 0) continue;
				for(int k = 0; k <= N && !found; ++k) {
					for(int l = 0; l <= M && !found; ++l) {
						if(k == 0 && l == 0) continue;
						if(k == i && l == j) continue;
						//printf("i %d j %d k %d l %d\n", i, j, k, l);
						if(abs(i*l - j*k) == A) {
							printf("Case #%d: 0 0 %d %d %d %d\n", Cases++, i , j, k, l);
							found = true;
						}
					}
				}
			}
		}
		if(!found) {
			printf("Case #%d: IMPOSSIBLE\n", Cases++);	
		}
	}	
	return 0;
}
