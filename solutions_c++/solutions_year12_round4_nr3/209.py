#include <cstdio>
#include <stack>

void test() {
	int n;
	scanf("%d", &n);
	std::stack<int> peeks;
	std::stack<int> big;
	int H[n+1];

	for( int i = n; i --> 1; ) {
		int h;
		scanf("%d", &h );
		peeks.push(h);
	}

	H[n] = 0;
	big.push( n );

	while( peeks.size() ) {
		int n = peeks.size();
		int p = peeks.top();
		
		while( p != big.top() ) {
			big.pop();
			if( big.size() == 0 ) {
				puts("Impossible");
				return; 
			}
		}

//		printf("%d * %d - 1 = %d\n", ( big.size() - 1 ),( p - n ), ( big.size() - 1 )*( p - n ) - 1 );
		H[n] = H[p] -( big.size() - 1 )*( p - n ) - 1;
		big.push( n );

		peeks.pop();
	}
	for( int i = 1; i <= n; i++ ) {
		printf("%d ", 1000000000+H[i] );
	}
	printf("\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for( int no = 1; no <= T; no++ ) {
		printf("Case #%d: ", no );
		test();
	}
	return 0;
}
