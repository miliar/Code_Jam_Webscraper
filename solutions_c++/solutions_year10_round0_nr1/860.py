#include <cstdio>
int main(){
	int t, n, k, i;
	scanf("%d", &t);
	for(i=0; i<t; ++i){
		scanf("%d %d", &n, &k);
		if((k+1) % (1<<n))
			printf("Case #%d: OFF\n", i+1);
		else
			printf("Case #%d: ON\n", i+1);
	}
}
