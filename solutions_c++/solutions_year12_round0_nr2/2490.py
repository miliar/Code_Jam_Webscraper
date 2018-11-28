#include <cstdio>

int min(int a, int b) {
	return (a<b)?a:b;
}

int main() {
	int T;
	scanf("%d", &T);
	
	for(int t = 0; t<T; t++) {
		int N, n_surprising, least;
		scanf("%d %d %d", &N, &n_surprising, &least);
		
		int regular = 0;
		int surprising = 0;
		
		for(int i=0; i<N; i++) {
			int points;
			scanf("%d", &points);
			
			int p[3];
			p[0] = p[1] = p[2] = points/3;
			
			if(points%3 == 1) {
				p[2]++;
			} else if(points%3 == 2) {
				p[2]++;
				p[1]++;
			}
			
			if(p[2] >= least) {
				//printf("points:%d, p[0]=%d, p[1]=%d, p[2]=%d\n", points, p[0], p[1], p[2]);
				regular++;
			} else {
				if(points%3 != 1 && p[2]+1 == least) {
					if(points%3 == 0 && p[0] > 0)
						surprising++;
					else if(points%3 == 2 && p[1] > 0)
						surprising++;
				}
			}
		}
		
		printf("Case #%d: %d\n", t+1, regular + min(surprising, n_surprising));
		
		
	}
}