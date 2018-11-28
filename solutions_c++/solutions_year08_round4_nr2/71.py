#include <cstdio>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)

int main()
{
	int T;
	scanf("%d", &T);
	FOR(t, 1, T+1) {
		int N, M, a;
		scanf("%d %d %d", &N, &M, &a);
		int x1 = -1, x2 = -1, y1 = -1, y2 = -1;
		FOR(X1, 0, N+1) FOR(X2, 0, N+1) FOR(Y1, 0, M+1) FOR(Y2, 0, M+1)
			if(X1*Y2-X2*Y1 == a) { x1 = X1; y1 = Y1; x2 = X2; y2 = Y2; }
		printf("Case #%d: ", t);
		if(x1 >= 0) printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}

