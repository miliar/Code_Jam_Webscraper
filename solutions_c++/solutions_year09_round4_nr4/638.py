
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

double cap( int p1[3], int p2[3] ) {
	int dx = p1[0] - p2[0];
	int dy = p1[1] - p2[1];
	double r =  p1[2] + p2[2] + sqrt(dx*dx+dy*dy);
	return r;
}

int main() {
	int N;
	scanf("%d",&N);

	for( int n=0; n<N; n++ ) {
		int M;
		scanf("%d ",&M);

		int plnt[30][3];
		for(int m=0;m<M;m++ ) {
			scanf("%d %d %d",&plnt[m][0],&plnt[m][1],&plnt[m][2]);
		}

		if( M == 1 ) {
			printf("Case #%d: %d\n",n+1,plnt[0][2]);
		} else if( M == 2 ) {
			int max = (plnt[0][2]<plnt[1][2]) ? plnt[1][2] : plnt[0][2];
			printf("Case #%d: %d\n",n+1,max);
		} else if( M == 3 ) {
			double max1 = cap( plnt[0], plnt[1] );
			double max11 = (plnt[2][2]<max1) ? max1 : plnt[2][2];
			double max2 = cap( plnt[0], plnt[2] );
			double max21 = (plnt[1][2]<max2) ? max2 : plnt[1][2];
			double max3 = cap( plnt[2], plnt[1] );
			double max31 = (plnt[0][2]<max3) ? max3 : plnt[0][2];
			double min = max11;
			if( min > max21 ) min = max21;
			if( min > max31 ) min = max31;
			printf("Case #%d: %g\n",n+1,min/2);
		} else {
			printf("Case #%d: -\n",n+1);
		}
	}

	return 0;
}

