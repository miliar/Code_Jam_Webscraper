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

bool is_win(int a, int b) {
	if (a > b) swap(a,b);
	if (a == b) return 0;
	if (a*2 <= b) return 1;
	return !is_win(b-a,a);
}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		int a1, a2, b1, b2, tot=0;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		for (int i = a1; i <= a2; i++) {
		for (int j = b1; j <= b2; j++) {
			if (is_win(i,j)) {
				tot++;
			}
		}
		}
		
		printf("Case #%d: %d\n",test,tot);
	}
}
