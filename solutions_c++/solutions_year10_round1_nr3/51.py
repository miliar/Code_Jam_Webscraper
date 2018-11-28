#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

enum{ MAX = 1000001 };
int TABLE[ MAX ] = {
		0,
				0,
				1,
				1,
				2,
				3,
				3,
				4,
				4,
				5,
				6,
				6,
				7,
				8,
				8,
				9,
				9,
				10,
				11,
				11,
				12,
				12,
				13,
				14,
				14,
				15,
};

int main()
{
		int a1, a2, b1, b2;
		int ccN;
		scanf("%d", &ccN);
		for( int i=10;i<MAX;i++ ) {
				if( TABLE[ TABLE[i-1]+1 ] < i - (TABLE[i-1]+1) ) {
					TABLE[ i ] = TABLE[i-1]+1;
				} else {
					TABLE[ i ] = TABLE[i-1];
				}
		}
		for( int cc=0;cc<ccN;cc++ ) {
				scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
				long long int count = 0;
				for( int i=a1;i<=a2;i++ ) {
						count += max( min( TABLE[ i ], b2 ) - b1+1, 0 );
				}
				for( int i=b1;i<=b2;i++ ) {
						count += max( min( TABLE[ i ], a2 ) - a1+1, 0 );
				}
				printf("Case #%d: %lld\n", cc + 1, count);
		}
		return 0;
}
