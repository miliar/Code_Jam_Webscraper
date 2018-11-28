#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define two(n) (1<<(n))

int TT,N,K;
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		scanf("%d %d",&N,&K);
		K=K%two(N);
		printf("Case #%d: %s\n",T,(K==two(N)-1)?"ON":"OFF");
	}

	return 0;
}
