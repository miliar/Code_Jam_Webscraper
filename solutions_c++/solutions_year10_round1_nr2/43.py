#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define insertchain(x,y) (x==y?0:(M==0? 9999999: (inscost*((abs(x-y)-1)/M))))

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		int delcost, inscost, M, nPixels;
		int a[128];
		scanf("%d%d%d%d",&delcost,&inscost,&M,&nPixels);
		for (int i = 0; i < nPixels; i++) {
			scanf("%d",&a[i]);
		}
		
		int cost[128][256]; //last used and value
		for (int i = 0; i < nPixels; i++) {
			for (int k = 0; k < 256; k++) {
				if (i == 0) {
					cost[i][k] = min(delcost+inscost,abs(a[i]-k));
					continue;
				}
				
				cost[i][k] = min (delcost*i + min(delcost+inscost,abs(a[i]-k))
				, delcost + cost[i-1][k]); //just drop it
				for (int j = 0; j < 256; j++) {
					cost[i][k] = min(cost[i][k],
						min(abs(a[i]-k),delcost+inscost)+insertchain(j,k)+cost[i-1][j]
					);
				}
			}
		}
		int best=0;
		for (int k = 0; k < 256; k++) {
			if (k==0 || best > cost[nPixels-1][k]) {
				best = cost[nPixels-1][k];
			}
		}
		
		printf("Case #%d: %d\n",test,best);
	}
}
