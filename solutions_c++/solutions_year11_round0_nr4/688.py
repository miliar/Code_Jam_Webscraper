#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for(int i=int(a);i<int(b);++i)
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	FOR(z,0,T) {
		int n, res = 0;
		scanf("%d", &n);
		FOR(i,1,n+1) {
		    int c; scanf("%d", &c);
		    if(c != i) ++res;
		}
		printf("Case #%d: %.6f\n", z + 1, double(res));
	}
	return 0;
}
