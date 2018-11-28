#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <map>

int groups[20], r, n, k, soma;

void process(){
	int ind = 0, total = 0, parcial;
	
	for(int i = 0; i < r; i++){
		parcial = 0;
		while(true){
			if(parcial + groups[ind] > k || parcial + groups[ind] > soma) break;
			parcial += groups[ind++];
			ind %= n;
		}
		total += parcial;
	}
	printf("%d\n", total);
}

void read(){
	scanf("%d%d%d", &r, &k, &n);
	soma = 0;
	for(int i = 0; i < n; i++){
		scanf("%d", &groups[i]);
		soma += groups[i];
	}
}

int main(){
	int casos, caso = 1;
	scanf("%d", &casos);
	freopen("./file.out", "w", stdout);
	while(casos--){
		printf("Case #%d: ", caso++);
		read();
		process();
	}
	
}