#include <cstdio>

int main() {
	int t,n,a,k;
	double wynik;
	int tab[1001], visited[1001];
	scanf("%d", &t);
	for(int i = 1; i<= t; i++) {
		wynik = 0;
		scanf("%d", &n);
		for(int j = 1; j <= n; j++) {
			visited[j]=0;
			scanf("%d", &a);
			tab[j] = a;	
		}
		
		for(int j = 1; j <= n; j++) {
			
			if(visited[j] == 0 && tab[j] != j) {
					
					k = 0;
					
					a = tab[j];
					
					while( visited[j] == 0 ) {
						
						visited[a] = 1;
						k++;
						a = tab[a];

					}
					wynik += k;
				
			}
			
		}
		
		
		printf("Case #%d: %.6lf\n", i, wynik);
	}
	
	
}
