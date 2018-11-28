#include <cstdio>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a);i<int(b);++i)
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    FOR(z,0,T) {
	long long sum = 0;
	int n, mn = 1234567, xsum = 0;
	scanf("%d", &n);
	FOR(i,0,n) {
	    int num;
	    scanf("%d", &num);
	    sum += num;
	    xsum ^= num;
	    mn = min(mn, num);
	}
	if(xsum != 0) printf("Case #%d: NO\n", z + 1);
	else printf("Case #%d: %lld\n", z + 1, sum - mn);
    }
    return 0;
}
