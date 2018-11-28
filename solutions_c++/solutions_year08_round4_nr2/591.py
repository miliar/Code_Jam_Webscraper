/* kaneko-B.cc
 */
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int C,N,M,A;
int area2(int x0, int y0, int x1, int y1, int x2, int y2) 
{
    return abs(x0*y1 - y0*x1 + y0*x2 - x0*y2 + x1*y2 - x2*y1);
}
void solve()
{
    int x0, y0, x1, y1;
    for (int i=0; i<N+1+M+1; ++i) {
	x0 = max(0, i - M - 1);
	y0 = min(M, i);
	for (int j=i+1; j<(N+1+M+1)*2; ++j) {
	    if (j < N+1+M+1) {
		x1 = max(0, j - M - 1);
		y1 = min(M, j);
	    } else if (j < N+1+(M+1)*2) {
		x1 = N;
		y1 = j - N-1-M-1;
	    }  else {
		x1 = (N+1+M+1)*2 - j -1;
		y1 = 0;
	    }
	    // cerr << x0 << " " << y0 << " " << x1 << " " << y1 << endl;
	    // lessfprintf(stderr, "try %d %d  %d %d %d %d\n", i, j, x0, y0, x1, y1);
	    for (int x2=0; x2<=N; ++x2) {
		for (int y2=0; y2<=M; ++y2) {
		    if (area2(x0, y0, x1, y1, x2, y2) == A) {
			printf("%d %d %d %d %d %d\n", 
			       x0, y0, x1, y1, x2, y2);
			return;
		    }
		}
	    }
	}
    }
    printf("IMPOSSIBLE\n");
}

int main()
{
    scanf("%d", &C);
    for (int t=0; t<C; ++t) {
	scanf("%d%d%d", &N, &M, &A);
	printf("Case #%d: ", t+1);
	solve();
    }
}

