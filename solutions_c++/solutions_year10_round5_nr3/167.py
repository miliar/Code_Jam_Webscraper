#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int POS[ 4000001 ];
int CHECK[ 4000001 ];
int UU, UUNew;
int update1[ 1000000 ];
int update2[ 1000000 ];
int NUM = 2000000;
int C;

void update( int uu, int count )
{
}
int main()
{
	int ccN;
	scanf("%d", &ccN);
	for( int cc=0;cc<ccN;cc++ ) {
		scanf("%d", &C );
		UU = UUNew = 0;
		memset( CHECK, 0, sizeof(CHECK) );
		memset( POS, 0, sizeof(POS) );

		int p, v;
		for( int i=0;i<C;i++ ) {
			scanf("%d%d", &p, &v );
			POS[ p+NUM ] = v;
			if( v >= 2 ) {
				update1[ UU++ ] = p+NUM;
			}
		}
		int *uuu, *updateNew;
		uuu = update1;
		updateNew = update2;
		int count = 0;
		int count1 = 0;
		while(1) {
			if( UU == 0 ) break;
			count1++;
			//printf("%d\n", count );
			for( int i=0;i<UU;i++ ) {
				int u = uuu[ i ];
				if( POS[ u ] >= 2 ) {
					POS[ u-1 ]++;
					POS[ u+1 ]++;
					POS[ u ] -= 2;
					if( POS[ u ] >= 2  && CHECK[ u ] != count1 + 1 ) {
						updateNew[ UUNew++ ] = u;
						CHECK[ u ] = count1 + 1;
					}
					if( POS[ u-1 ] >= 2  && CHECK[ u-1 ] != count1 + 1 ) {
						updateNew[ UUNew++ ] = u-1;
						CHECK[ u-1 ] = count1 + 1;
					}
					if( POS[ u+1 ] >= 2  && CHECK[ u+1 ] != count1 + 1 ) {
						updateNew[ UUNew++ ] = u+1;
						CHECK[ u+1 ] = count1 + 1;
					}
					count++;
				}
			}
			int *tmp;
			tmp = uuu;
			uuu = updateNew;
			updateNew = tmp;
			UU = UUNew;
			UUNew = 0;
		}
		printf("Case #%d: %d\n", cc+1, count );
	}
	return 0;
}
