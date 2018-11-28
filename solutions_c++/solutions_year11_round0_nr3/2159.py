#include<cstdio>

int N,C;
int sum;
int min,cur;
int xorSum;
bool impossible;

int main() {
	scanf("%d",&N);
	for( int i=1; i<=N; i++ ) {
		scanf("%d", &C);
		xorSum = 0;
		min = 1000000;
		sum = 0;		

		for(int k=0; k<C; k++) {
			scanf("%d", &cur);
			xorSum = xorSum ^ cur;
			sum += cur;
			if( cur < min ) min = cur;
		}
		impossible = (xorSum != 0);
		if( impossible )
			printf("Case #%d: NO\n", i);
		else if( C == 0 )
			printf("Case #%d: 0\n", i);
		else
			printf("Case #%d: %d\n",i, sum-min);
	}

	return 0;
}
