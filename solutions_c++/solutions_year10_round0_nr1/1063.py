#include <cstdio>

int main(){
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		int n,k;
		scanf("%d %d", &n, &k);
		n=(1<<n);
		printf("Case #%d: ", T);
		if ( (k+1)%n==0 )
			printf("ON\n");
		else
			printf("OFF\n");
	}
}
