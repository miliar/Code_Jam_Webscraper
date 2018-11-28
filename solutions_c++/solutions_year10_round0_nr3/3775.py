#include <cstdio>
#include <queue>

using namespace std ;

int main()
{
	freopen("C-small-attempt0.in", "r", stdin) ;
	freopen("C-small-attempt0.out", "w", stdout) ;

	queue <int> Q ;
	queue <int> Q1 ;
	int T, t, R, k, N, i, temp, sz, total, u, j ;
	scanf("%d", &T) ;	
	for (t = 1 ; t <= T ; t++){
		total = 0 ;
		scanf("%d %d %d", &R, &k, &N) ;
		for (i = 0 ; i < N ; i++){
			scanf("%d", &temp) ;
			Q.push(temp) ;
		}

		for (j = 1 ; j <= R ; j++){
			sz = 0 ;
			while (1){			
				if (Q.empty()) break ;
				u = Q.front() ;
				if (sz + u > k) break ;
				else{
				 	sz += u ; 
					Q.pop() ;
					Q1.push(u) ;
				}
				
			}
			while (!Q1.empty()){ Q.push(Q1.front()) ; Q1.pop() ;}	
			total += sz ;
		}
		printf("Case #%d: %d\n", t, total) ;
		while (!Q.empty()) Q.pop() ;
	}
	return 0;
}

