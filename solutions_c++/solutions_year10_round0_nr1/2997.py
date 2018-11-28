#include<cstdio>

int cases, n,k;

int main() {

	scanf("%d", &cases);
	
	for( int i=0; i<cases; i++ ) {
		scanf("%d %d", &n, &k);
		
		int x = 1 << n;		
		printf("Case #%d: ", (i+1));
		if( (k%x) == (x-1) ) {
			printf("ON\n");
		} else {
			printf("OFF\n");
		}

	}
	
	return 0;
}
