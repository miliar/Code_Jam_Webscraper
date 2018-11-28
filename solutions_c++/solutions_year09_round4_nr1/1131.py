#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

int N, T;

int tab[100];

int c = 0;

void change(int x, int y) {
	int tmp = tab[x];
	tab[x] = tab[y];
	tab[y] = tmp;
	c++;
}

int main() {
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		scanf("%d", &N);		
		for(int j=0; j<N; j++) {
			char bufor[256];
			scanf("%s", bufor);
			tab[j] = -1;
			for(int k=0; k<strlen(bufor); k++) {
				if (bufor[k]=='1')
					tab[j] = k;
			}
			
		}	
		c = 0;
		for(int j=0; j<(N-1); j++) {
			if (tab[j]<=j)
				continue;
			
			if (tab[j+1]<=j) {
				change(j+1, j);
			} else {
				int k;
				for(k=j+1; k<N; k++)
					if (tab[k]<=j)
						break;
				for(int m=k; m>j; m--)
					change(m, m-1);
			}							
		}
		
		/*for(int j=0; j<N; j++)
			printf("%d ", tab[j]);*/
								
		
		printf("Case #%d: %d\n", (i+1), c);
	}
	return 0;
}
