#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;



int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		
		printf("Case #%d: ", i);
		
		int xori = 0;
		int N;
		int val;
		int sum = 0;
		int menor = 1000001;
		scanf("%d", &N);
		
		for(int j = 1; j <= N; j++){
			scanf("%d", &val);
			xori ^= val;
			sum += val;
			menor = min(menor, val);
		}
		if(xori != 0){
			printf("NO\n");
		}else{
			printf("%d\n", sum-menor);
		}
	}
	
	return 0;
}
