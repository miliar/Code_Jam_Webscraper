
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <vector>
#include <algorithm>

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int U32;

using namespace std;
typedef pair<int, int> pii;

int main() {
	int N;
	scanf("%d",&N);

	for( int n=0; n<N; n++ ) {
		int M;
		scanf("%d ",&M);

		int row[40];

		char tmp[100];
		for(int m=0; m<M; m++ ) {
			fgets(tmp,100,stdin);
			char *ri = rindex(tmp,'1');
			if( ri == NULL ) row[m] = -1;
			else row[m] = rindex(tmp,'1')-tmp;
		}

		int val=0;
		for(int m=0; m<M-1; m++ ) {
			if( row[m] > m ) {
				int l;
				for(l=m+1; l<M; l++ ) {
					if( row[l] <= m ) {
						break;
					}
				}
				for( ; l>m; l-- ) {
					int t = row[l];
					row[l] = row[l-1];
					row[l-1] = t;
					val++;
				}
			}
		}

		/*int oval = -1;
		int val = 0;
		while( oval != val ) {
			oval = val;
			for(int l=1; l<M; l++ ) {
				if( (row[l-1] > l-1 || row[l] > l)&& row[l-1] > row[l] ) {
					val++;
					int t = row[l];
					row[l] = row[l-1];
					row[l-1] = t;
				} else {
					printf(" ");
				}
			}
		}*/

		printf("Case #%d: %d\n",n+1,val);
	}

	return 0;
}

