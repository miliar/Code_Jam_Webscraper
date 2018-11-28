#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cassert>
#include <utility>
using namespace std;
#define VAR(i,v) __typeof((v))i=(v)
#define FOREACH(i,v) for(VAR(i,(v).begin());i!=(v).end();i++)

int main() {
	int _T; scanf("%d",&_T);
	for(int _iT=1; _iT<=_T; _iT++) {
		int vsum = 0, vxor = 0, vmin = -1;
		int n; scanf("%d", &n);
		for(int i=0; i<n; i++) {
			int v; scanf("%d", &v);
			vxor ^= v;
			vsum += v;
			if(vmin<0 || v<vmin)
				vmin = v;
		}
		printf("Case #%d: ", _iT);
		if(vxor != 0) {
			printf("NO\n");
		} else {
			printf("%d\n", vsum-vmin);
		}
	}

	return 0;
}
