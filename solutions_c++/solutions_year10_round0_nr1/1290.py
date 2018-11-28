
#include <cstdio>

int main(){
	
	int n;
	int a, b;
	int sum;

	scanf("%d", &n);

	for(int i=1; i<=n; ++i){
		scanf("%d%d", &a, &b);
		sum = 0;
		for(int j=0; j<a; ++j){
			sum += b%2;
			b >>= 1;
		}
		if(sum == a){
			printf("Case #%d: ON\n", i);
		}else{
			printf("Case #%d: OFF\n", i);
		}
	}
	return 0;
}
