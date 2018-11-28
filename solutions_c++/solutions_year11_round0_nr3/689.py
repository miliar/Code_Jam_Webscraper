#include <cstdio>
#include <limits.h>
#include <vector>
using namespace std;

void run(int casenr) {
	int n; scanf("%d",&n);
	int smallest=INT_MAX,sum=0,xorval=0;
	for(int i=0;i<n;++i) {
		int x; scanf("%d",&x);
		xorval^=x;
		sum+=x;
		if(x<smallest) smallest=x;
	}
	if(xorval!=0) printf("Case #%d: NO\n",casenr); else printf("Case #%d: %d\n",casenr,sum-smallest);	
}

int main() {
	int n; scanf("%d",&n); for(int i=1;i<=n;++i) run(i);
	return 0;
}
