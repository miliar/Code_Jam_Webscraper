#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;
struct chick {
       int x,v;
};       
chick C[100];
int V[100];

bool error=0;

bool _less(const chick & a, const chick & b) {
	return ( a.x < b.x);
}

int slv(int N, int K, int B, int T)
{
	if (K<=0) return 0;
	if (N<0 || N<(K-1)) { error=1; return 0;}
	int s=C[N].x+C[N].v*T;
	if (s >= B+K-1) {
		return slv(N-1, K-1, B, T);
	}
	if (s < B) {
		return K+slv(N-1, K, B, T);
	}
	else {
		return (s-B) + slv(N-1, K-1, B, T);
	}
}

int solve()
{
	error=0;
	int N,K,B,T;
	scanf("%d%d%d%d", &N,&K,&B,&T);
	for (int i=0; i<N; ++i) scanf("%d", &C[i].x);
	for (int i=0; i<N; ++i) scanf("%d", &C[i].v);
	sort(C, C+N, _less);

	return slv(N-1, K, B, T);
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	
	int M;
	scanf("%d", &M);
	for (int i=1; i<=M; ++i) {
		int tmp = solve();
		if (!error) printf("Case #%d: %d\n", i, tmp);	
			else printf("Case #%d: IMPOSSIBLE\n", i);
	}	
}

