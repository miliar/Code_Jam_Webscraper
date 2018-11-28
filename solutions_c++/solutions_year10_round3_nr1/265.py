
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

	int p[1000][2];

	for( int n=0; n<N; n++ ) {
		int PC;
		scanf("%d",&PC);

		for(int a=0; a<PC; a++) {
			scanf("%d %d",&p[a][0],&p[a][1]);
		}

		LL i=0;

		for(int a=0; a<PC-1; a++) {
			for(int b=a+1; b<PC; b++) {
				if( (p[a][0] > p[b][0] && p[a][1] < p[b][1]) || (p[a][0] < p[b][0] && p[a][1] > p[b][1]) ) {
					i++;
				}
			}
		}

		printf("Case #%d: %lld\n",n+1,i);
	}

	return 0;
}

