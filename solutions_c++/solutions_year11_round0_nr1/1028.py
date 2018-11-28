#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i,a,b) for(int i=(a); i<(b); ++i)

int main() {
	int T;
	scanf("%d", &T);
	rep(t,0,T) {
		int N;
		scanf("%d", &N);
		int bb = 1, ob = 1, bt = 0, ot = 0, a = 0;
		rep(n,0,N) {
			char R; int P;
			scanf(" %c %d", &R, &P);
			if (R == 'B') {
				bt = a = max(bt+abs(bb-P), a)+1;
				bb = P;
			} else {
				assert(R == 'O');
				ot = a = max(ot+abs(ob-P), a)+1;
				ob = P;
			}
		}
		printf("Case #%d: %d\n", t+1, a);
	}
	return 0;
}