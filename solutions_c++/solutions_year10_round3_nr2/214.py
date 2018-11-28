
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <vector>
#include <algorithm>
#include <map>

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int U32;
typedef unsigned char U8;

using namespace std;
typedef pair<int, int> pii;

int main() {
	int N;
	scanf("%d",&N);

	for( int n=0; n<N; n++ ) {
		int L, P, C;
		scanf("%d %d %d",&L,&P,&C);

		int on = 0;
		for( int a=(P+C-1)/C; a>L; a=(a+C-1)/C ) {
			on++;
			//printf("%d %d\n",a,on);
		}

		int r = 0;
		if( on > 0 ) {
			r = log2(on) + 1.0;
		}

		printf("Case #%d: %d\n",n+1,r);
	}

	return 0;
}

