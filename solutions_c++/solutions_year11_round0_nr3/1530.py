# include <cstdio>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <map>
# include <set>
# include <algorithm>
# include <cstdlib>

using namespace std;

int vet[1024];

int main (void){
	int T, N;
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		scanf("%d", &N);
		int soma = 0;
		for(int i = 0 ; i < N; i++){
			scanf("%d", &vet[i]);
			soma += vet[i];
		}
		sort(vet, vet+N);
		int XOR = 0;
		for(int i = 0 ; i < N;i++) XOR ^= vet[i];
		if( XOR ) printf("Case #%d: NO\n", tc);
		else printf("Case #%d: %d\n", tc, soma - vet[0]);
	}
	return 0;
}