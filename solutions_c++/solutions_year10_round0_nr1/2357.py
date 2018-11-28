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

#define MAX 31

int ciclos[MAX];

void preprocess(){
	ciclos[0] = 1;
	for(int i = 1; i < MAX; i++){
		ciclos[i] = ciclos[i-1]<<1;
	}
}

int main(){
	int casos, k, n, caso = 1;
	scanf("%d", &casos);
	preprocess();
	freopen("./file.out", "w", stdout);
	while(casos--){
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", caso++);
		if((k+1)%ciclos[n]){
			printf("OFF\n");
		}else{
			printf("ON\n");
		}
		
	}
	
}