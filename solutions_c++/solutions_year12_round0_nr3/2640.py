#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int pots[] = {1, 10, 100,1000,10000, 100000, 1000000, 10000000};
int auxx[50];
int main(){
	
	int casos; scanf("%d", &casos);
	int caso = 0, A, B;
	while(casos--){ ++caso;
		int total = 0;
		int n, m, aux;
		scanf("%d%d", &A, &B);
		int tam = log10(A) + 1; bool ok;
		for(int i = A; i <= B; ++i){
			n = i;
			for(int a = 0; a < tam; ++a){
				aux = n%10;
				n /= 10;
				n += aux*pots[tam-1];
				ok =  true;
				auxx[a] = n;
				for(int j = 0; j < a; ++j) if(auxx[j] == n) {ok = false; break;}
				if(n > i && n <= B && ok){
					++total;
				}
				
			}
			
			
			
		}
		
		printf("Case #%d: %d\n", caso, total);
	}
	
	return 0;
}