#include <stdio.h>
#include <algorithm>
using namespace std;


struct point {
	int A, B;
	bool operator<(const point& o)const {
		if (A != o.A) return A < o.A;
		return B < o.B;
	}
};

point P[1001];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int T, cases,N,i,j,k,ans;
	scanf("%d", &T);
	for (cases = 1; cases <= T; ++cases) {
		scanf("%d", &N);
		for (i=0; i<N; ++i) {
			scanf("%d%d", &P[i].A, &P[i].B);
		}
		sort(P, P+N);
		ans = 0;
		for (i=0; i<N; ++i) {
			for (j=i+1; j<N; ++j) {
				if (P[j].B < P[i].B) {
					++ans;
				}
			}
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	
	return 0;
}
