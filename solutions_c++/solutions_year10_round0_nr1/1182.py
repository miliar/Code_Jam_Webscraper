#include <cstdio>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
using namespace std;

int main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,0,Z) {
		int n, k;
		scanf("%d%d", &n, &k);
		if(k % (1 << n) == (1 << n) - 1)
			printf("Case #%d: ON\n", z + 1);
		else	printf("Case #%d: OFF\n", z + 1);
	}
	return 0;
}
