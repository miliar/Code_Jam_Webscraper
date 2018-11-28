#include <cstdio>
#include <cstdlib>
#include <vector>
#include <list>

using namespace std;

list<int> A;
list<int>::iterator j, k;

int wh[5010];

int main(void) {
	freopen("input.txt", "r", stdin);
	int i, v, N, M, test, T;
	
	scanf("%d", &T);
	for(test=1; test<=T; test++) {
		scanf("%d", &N);
		
		A.clear();
		for (i=1; i<=N; i++) A.push_back(i);
		
		j = A.begin();
		for (i=1; i<N; i++) {			
			for (v=1; v<i; v++) {
				j++;
				if ( j == A.end() ) j = A.begin();
			}
			
			wh[ *j ] = i;
			
			k = j; k++;
			if ( k == A.end() ) k = A.begin();
			A.erase(j);
			j = k;
		}
		
		wh[ *j ] = N;
		
		printf("Case #%d:", test);
		
		scanf("%d", &M);
		for (i=1; i<=M; i++) {
			scanf("%d", &v);
			
			printf(" %d", wh[v]);
		}
		printf("\n");
		
	}
	
	
	return 0;
}
