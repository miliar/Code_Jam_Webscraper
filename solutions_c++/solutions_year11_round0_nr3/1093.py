#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;


int main(){
	int caso = 0;
	int casos; scanf("%d", &casos);
	int n, values[1010], maior, xort, menor;
	while(casos--){
		scanf("%d", &n);
		xort = 0; menor = 0x63636363; maior = 0;
		for(int i = 0; i < n; ++i){
			scanf("%d", &values[i]);
			xort ^= values[i];
			maior += values[i];
			if(values[i] < menor) menor = values[i];
		}
		
		
		
		printf("Case #%d: ", ++caso);
		if(xort != 0) printf("NO\n");
		else printf("%d\n", maior-menor);
	}

	
	return 0;
}